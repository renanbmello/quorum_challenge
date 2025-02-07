from ..repositories.legislator_repository import LegislatorRepository
import pandas as pd

class LegislativeService:
    def __init__(self):
        self.legislator_repository = LegislatorRepository()
        self._vote_results_df = None
        self._votes_df = None
        self._bills_df = None

    def _load_vote_data(self):
        if self._vote_results_df is None:
            self._vote_results_df = pd.read_csv('data/vote_results_(2).csv')
            self._votes_df = pd.read_csv('data/votes_(2).csv')
            self._bills_df = pd.read_csv('data/bills_(2).csv')

    def get_legislator_statistics(self):
        self._load_vote_data()
        legislators = self.legislator_repository.get_all()
        
        vote_to_bill = dict(zip(self._votes_df['id'], self._votes_df['bill_id']))
        bill_to_title = dict(zip(self._bills_df['id'], self._bills_df['title']))
        
        for legislator in legislators:
            legislator_votes = self._vote_results_df[
                self._vote_results_df['legislator_id'] == legislator.id
            ]
            
            legislator.supported_bills = []
            legislator.opposed_bills = []
            
            for _, vote in legislator_votes.iterrows():
                bill_id = vote_to_bill[vote['vote_id']]
                bill_title = bill_to_title[bill_id]
                
                if vote['vote_type'] == 1:  
                    legislator.supported_bills.append(bill_title)
                elif vote['vote_type'] == 2:  
                    legislator.opposed_bills.append(bill_title)
        
        return legislators 

    def get_bills_analysis(self):
        self._load_vote_data()
        bills_analysis = []
        
        legislators = self.legislator_repository.get_all()
        legislator_names = {l.id: l.name for l in legislators}
        
        for _, bill in self._bills_df.iterrows():
            votes_for_bill = self._vote_results_df[
                self._vote_results_df['vote_id'].isin(
                    self._votes_df[self._votes_df['bill_id'] == bill.id]['id']
                )
            ]
            
            support_count = len(votes_for_bill[votes_for_bill['vote_type'] == 1])
            opposition_count = len(votes_for_bill[votes_for_bill['vote_type'] == 2])
            
            sponsor_name = legislator_names.get(bill['sponsor_id'], 'Unknown')
            
            bills_analysis.append({
                'title': bill['title'],
                'support_count': support_count,
                'opposition_count': opposition_count,
                'sponsor_name': sponsor_name
            })
        
        return bills_analysis 