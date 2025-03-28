from typing import Annotated

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select
from datetime import datetime
import dateutil.parser as parser
import json

from ..dependencies import SessionDep
from ..models.event import Event, EventUpdate
from ..cli.datagen import generate_data

router = APIRouter()

# Create Event
@router.post("/events/", tags=["Event"])
def create_event(event: Event, session: SessionDep) -> Event:

    print(event.meta)
    try:
        json.loads(event.meta if isinstance(event.meta, str) else json.dumps(event.meta))
    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid meta data format")

    try:
        event.timestamp = parser.parse(event.timestamp)
    except ValueError:
        raise HTTPException(400, "Invalid date time format")

    # Create an Event
    session.add(event)
    session.commit()
    session.refresh(event)

    return event

# Read Event
@router.get("/events/", response_model=list[Event], tags=["Event"])
def read_events(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Event]:
    
    command = select(Event).order_by(Event.timestamp.desc()).offset(offset).limit(limit)
    events = session.exec(command).all()

    return events

# Read Single Event
@router.get("/events/{event_id}", response_model=Event, tags=["Event"])
def read_event(event_id: int, session: SessionDep) -> Event:

    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event

# Update Event
@router.put("/events/{event_id}", tags=["Event"])
def update_event(event_id: int, data: EventUpdate, session: SessionDep) -> Event:
    event = session.get(Event, event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    event_data = data.model_dump(exclude_unset=True)
    event.sqlmodel_update(event_data)

    session.add(event)
    session.commit()
    session.refresh(event)

    return event

# Delete Event
@router.delete("/events/{event_id}", tags=["Event"])
def delete_event(event_id: int, session: SessionDep):
    events = session.get(Event, event_id)

    if not events:
        raise HTTPException(status_code=404, detail="Event not found")

    session.delete(events)
    session.commit()
    return {"ok": True}


# Make fake data
@router.get("/events/fake/", tags=["Fake Data"])
def generate_fake_events(
    session: SessionDep,
    limit: Annotated[int, Query(le=10000)] = 1000,
):
    
    events = generate_data(limit)

    for event in events:
        session.add(event)

    session.commit()

    return {"ok": True}