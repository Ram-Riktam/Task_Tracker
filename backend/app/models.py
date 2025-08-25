from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Card(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True, index=True)
    Title: str
    Description: Optional[str] = None
    added_by: str
    comments: Optional[str] = None
    status: str = Field(default="todo")  # todo, inprogress, completed, deployed
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
