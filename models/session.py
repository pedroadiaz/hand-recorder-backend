from dataclasses import dataclass, field
from typing import Optional
from utils.get_new_date import get_new_date
from utils.get_new_id import get_new_uuid

@dataclass
class Session:
    userId: str
    stackSize: int
    smallBlind: int
    bigBlind: int
    cashOutAmount: Optional[int] = None
    location: Optional[str] = None
    id: str = field(init=True, default_factory=get_new_uuid)
    created: str = field(init=False, default_factory=get_new_date)
