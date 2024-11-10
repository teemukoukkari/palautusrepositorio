class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = int(dict['assists'])
        self.goals = int(dict['goals'])
        self.points = self.assists + self.goals
        self.team = dict['team']
        self.games = int(dict['games'])
        
    def __str__(self):
        return f"{self.name:20} {self.team:3}  {self.goals:2} + {self.assists:2} = {self.points:3}"