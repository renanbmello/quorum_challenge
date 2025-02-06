from dataclasses import dataclass
from typing import List

@dataclass
class Legislator:
    id: int
    name: str
    supported_bills: List[int] = None
    opposed_bills: List[int] = None

    @property
    def supported_count(self) -> int:
        return len(self.supported_bills) if self.supported_bills else 0

    @property
    def opposed_count(self) -> int:
        return len(self.opposed_bills) if self.opposed_bills else 0

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=int(data['id']),
            name=data['name'],
            supported_bills=[],
            opposed_bills=[]
        ) 