from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional, Dict
from datetime import datetime

class Event(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    device_id: str
    timestamp: Optional[datetime] = Field(default='CURRENT_TIMESTAMP')
    description: str  # do we need text datatype here??

    # Keep any additional metadata
    meta: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True
