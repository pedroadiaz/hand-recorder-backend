from dataclasses import dataclass, field
from typing import Optional
from utils.get_new_date import get_new_date
from utils.get_new_id import get_new_uuid

@dataclass
class Hand:
    sessionId: str
    stackSize: int
    position: str
    holeCards: str
    preFlopNotes: Optional[str] = None
    foldedPreflop: Optional[str] = None
    flopCards: Optional[str] = None
    flopNotes: Optional[str] = None
    foldedFlop: Optional[bool] = None
    turnCard: Optional[str] = None
    turnNotes: Optional[str] = None
    foldedTurn: Optional[bool] = None
    riverCard: Optional[str] = None
    riverNotes: Optional[str] = None
    foldedRiver: Optional[bool] = None
    wonHand: Optional[bool] = None
    otherNotes: Optional[str] = None
    id: str = field(init=True, default_factory=get_new_uuid)
    created: str = field(init=False, default_factory=get_new_date)

