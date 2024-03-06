from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str