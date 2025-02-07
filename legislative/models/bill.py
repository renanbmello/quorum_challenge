from dataclasses import dataclass
from typing import Optional

@dataclass
class Bill:
    id: int
    title: str
    sponsor_id: int
    sponsor_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=int(data['id']),
            title=data['title'],
            sponsor_id=int(data['sponsor_id'])
        ) 