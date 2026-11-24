from pydantic import BaseModel
from datetime import date
from typing import Literal


class Ticket(BaseModel):
    ticket_id: int
    customer_name: str
    equipment: str
    issue_description: str
    priority: Literal["Low", "Medium", "High"]
    status: Literal["Open", "In Progress", "Closed"]
    created_at: date