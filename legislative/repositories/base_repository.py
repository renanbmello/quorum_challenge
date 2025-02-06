import pandas as pd
from pathlib import Path
from typing import List, TypeVar, Generic, Type

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, model_class: Type[T], csv_file: str):
        self.model_class = model_class
        self.csv_file = csv_file
        self._data = None
        self._df = None

    def load_data(self) -> None:
        if self._df is None:
            csv_path = Path('data') / self.csv_file
            self._df = pd.read_csv(csv_path)
            self._data = [
                self.model_class.from_dict(row)
                for _, row in self._df.iterrows()
            ]

    def get_all(self) -> List[T]:
        self.load_data()
        return self._data
    
    def get_by_id(self, id: int) -> T:
        self._load_data()
        for item in self._data:
            if item.id == id:
                return item
        return None
