from .base_repository import BaseRepository
from ..models.bill import Bill

class BillRepository(BaseRepository[Bill]):
    def __init__(self):
        super().__init__(Bill, 'bills_(2).csv') 