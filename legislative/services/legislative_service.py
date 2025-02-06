from ..repositories.legislator_repository import LegislatorRepository
from typing import Dict, List
import pandas as pd

class LegislativeService:
    def __init__(self):
        self.legislator_repository = LegislatorRepository()
        self._vote_results_df = None
        self._votes_df = None

    def _load_vote_data(self):
        if self._vote_results_df is None:
            self._vote_results_df = pd.read_csv('data/vote_results_(2).csv')
            self._votes_df = pd.read_csv('data/votes_(2).csv')

    def get_legislator_statistics(self):
        self._load_vote_data()
        legislators = self.legislator_repository.get_all()
        
        # Processar votos para cada legislador
        for legislator in legislators:
            legislator_votes = self._vote_results_df[
                self._vote_results_df['legislator_id'] == legislator.id
            ]
            
            # Mapear votos para bills
            legislator.supported_bills = []
            legislator.opposed_bills = []
            
            for _, vote in legislator_votes.iterrows():
                vote_id = vote['vote_id']
                bill_id = self._votes_df[
                    self._votes_df['id'] == vote_id
                ]['bill_id'].iloc[0]
                
                if vote['vote_type'] == 1:  # support
                    legislator.supported_bills.append(bill_id)
                else:  # oppose
                    legislator.opposed_bills.append(bill_id)
        
        return legislators 