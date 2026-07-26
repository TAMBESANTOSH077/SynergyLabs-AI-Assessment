from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class Source(BaseModel):

    source: str

    chunk: int

    file_type: Optional[str] = None

    page: Optional[int] = None

    model_config = ConfigDict(extra="ignore")


class QueryResponse(BaseModel):

    question: str

    answer: str

    sources: List[Source]

    model_config = ConfigDict(extra="ignore")