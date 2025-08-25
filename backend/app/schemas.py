from pydantic import BaseModel
from typing import Optional


class CardCreate(BaseModel):
    Title: str
    Description: Optional[str] = None
    added_by: str
    comments: Optional[str] = None
    status: Optional[str] = "todo"

class CardUpdate(BaseModel):
    Title: Optional[str] = None
    Description: Optional[str] = None
    added_by: Optional[str] = None
    comments: Optional[str] = None
    status: Optional[str] = None