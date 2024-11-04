import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), # 16
            Player("Lemieux", "PIT", 45, 54), # 99
            Player("Kurri",   "EDM", 37, 53), # 90
            Player("Yzerman", "DET", 42, 56), # 98
            Player("Gretzky", "EDM", 35, 89) # 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_correct_name(self):
        self.assertEqual(
            self.stats.search("Semenko").name,
            "Semenko"
        )
    
    def test_search_invalid_name(self):
        self.assertEqual(
            self.stats.search("Selänne"),
            None
        )
    
    def test_team_edm_correct_players(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
        
        names = set([team[0].name, team[1].name, team[2].name])
        self.assertTrue("Semenko" in names)
        self.assertTrue("Kurri" in names)
        self.assertTrue("Gretzky" in names)
    
    def test_top_four_players_by_points(self):
        top = self.stats.top(4, SortBy.POINTS)
        self.assertEqual(len(top), 4)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")
        self.assertEqual(top[3].name, "Kurri")
    
    def test_top_four_players_by_goals(self):
        top = self.stats.top(4, SortBy.GOALS)
        self.assertEqual(len(top), 4)
        self.assertEqual(top[0].name, "Lemieux")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Kurri")
        self.assertEqual(top[3].name, "Gretzky")
    
    def test_top_four_players_by_assists(self):
        top = self.stats.top(4, SortBy.ASSISTS)
        self.assertEqual(len(top), 4)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Lemieux")
        self.assertEqual(top[3].name, "Kurri")