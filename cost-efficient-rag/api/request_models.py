from pydantic import BaseModel, Field
from typing import Optional


class QueryRequest(BaseModel):
    query: str = Field(..., description="User question")
    top_k: Optional[int] = Field(default=5, ge=1, le=10)
    category: Optional[str] = None
    file_type: Optional[str] = None