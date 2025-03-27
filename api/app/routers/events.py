from typing import Annotated

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from ..dependencies import SessionDep
from ..models.event import Event
from ..cli.datagen import generate_data

router = APIRouter()

# Create Event
@router.post("/events/", tags=["Event"])
def create_event(event: Event, session: SessionDep) -> Event:

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
    
    command = select(Event).offset(offset).limit(limit)
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
def update_event(event_id: int, data: Event, session: SessionDep) -> Event:
    Event = session.get(Event, event_id)

    if not Event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    event_data = data.model_dump(exclude_unset=True)
    Event.sqlmodel_update(event_data)
    session.add(Event)
    session.commit()
    session.refresh(Event)

    return Event

# Delete Event
@router.delete("/events/{event_id}", tags=["Event"])
def delete_event(event_id: int, session: SessionDep):
    Event = session.get(Event, event_id)

    if not Event:
        raise HTTPException(status_code=404, detail="Event not found")

    session.delete(Event)
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