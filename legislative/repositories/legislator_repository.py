from .base_repository import BaseRepository
from ..models.legislator import Legislator

class LegislatorRepository(BaseRepository[Legislator]):
    def __init__(self):
        super().__init__(Legislator, 'legislators_(2).csv')