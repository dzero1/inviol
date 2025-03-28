from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional, Dict
from datetime import datetime

class Event(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    device_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now())
    description: Optional[str]

    # Keep any additional metadata
    meta: Optional[Dict] = Field(default_factory=dict, sa_column=Column(JSON))

    # Needed for Column(JSON)
    # class Config:
        # arbitrary_types_allowed = True


class EventUpdate(SQLModel):
    device_id: Optional[str]
    timestamp: Optional[datetime]
    description: Optional[str]
    meta: Optional[Dict]