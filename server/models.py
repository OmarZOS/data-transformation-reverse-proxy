from pydantic import BaseModel
from typing import Optional

# ---------- Data models: ---------------------------------------

class Transformation(BaseModel):
    name: str
    url: str
    description: Optional[str] = None
    # tax: Optional[float] = None

class Query(BaseModel):
    api:str
    content: dict
    roadmap: Optional[list] = None