from pydantic import BaseModel
from typing import List, Optional


class Architecture(BaseModel):

    application_name: Optional[str] = None

    llm: Optional[str] = None

    retrieval: bool = False

    vector_database: Optional[str] = None

    memory: Optional[str] = None

    tools: List[str] = []

    authentication: Optional[str] = None

    deployment: Optional[str] = None

    logging: Optional[str] = None

    databases: List[str] = []

    external_apis: List[str] = []   