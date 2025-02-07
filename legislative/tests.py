from django.test import TestCase
from .services.legislative_service import LegislativeService

class LegislativeServiceTests(TestCase):
    def setUp(self):
        self.service = LegislativeService()

    def test_legislator_statistics(self):
        legislators = self.service.get_legislator_statistics()
        
        don_bacon = next(l for l in legislators if l.id == 904789)
        self.assertEqual(don_bacon.supported_count, 1)
        self.assertEqual(don_bacon.opposed_count, 1)
        
        aoc = next(l for l in legislators if l.id == 1269767)
        self.assertEqual(aoc.supported_count, 1)
        self.assertEqual(aoc.opposed_count, 1)

    def test_bills_analysis(self):
        bills = self.service.get_bills_analysis()
        
        self.assertEqual(len(bills), 2)
        
        infrastructure = next(b for b in bills if 'Infrastructure' in b['title'])
        self.assertEqual(infrastructure['support_count'], 13)
        self.assertEqual(infrastructure['opposition_count'], 6)

    def test_bills_analysis_with_sponsor(self):
        bills = self.service.get_bills_analysis()
    
        bbb_act = next(b for b in bills if 'Build Back Better' in b['title'])
        self.assertEqual(bbb_act['sponsor_name'], 'Rep. John Yarmuth (D-KY-3)')
            
        infra_act = next(b for b in bills if 'Infrastructure' in b['title'])
        self.assertEqual(infra_act['support_count'], 13)
        self.assertEqual(infra_act['opposition_count'], 6)
