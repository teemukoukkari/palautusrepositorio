from enum import IntEnum

class TennisGame:
    SCORE_LOVE = 0
    SCORE_FIFTEEN = 1
    SCORE_THIRTY = 2
    SCORE_FOURTY = 3
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    MIN_FOR_ADVANTAGE = 4
    MIN_WIN_DIFF = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self._player1_score = 0
        self._player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self._player1_score += 1
        elif player_name == self.player2_name:
            self._player2_score += 1
        else:
            raise Exception("Invalid player name")

    def _get_score_tied(self):
        if self._player1_score <= self.SCORE_THIRTY:
            return self.SCORE_NAMES[self._player1_score] + "-All"
        else:
            return "Deuce"

    def _get_score_advantage(self):
        score_difference = self._player1_score - self._player2_score
        leading_player = self.player1_name if score_difference > 0 else self.player2_name

        if abs(score_difference) >= self.MIN_WIN_DIFF:
            return "Win for " + leading_player
        else:
            return "Advantage " + leading_player

    def _get_score_normal(self):
        return self.SCORE_NAMES[self._player1_score] + "-" + self.SCORE_NAMES[self._player2_score] 

    def get_score(self):
        if self._player1_score == self._player2_score:
            return self._get_score_tied()
        elif max(self._player1_score, self._player2_score) >= self.MIN_FOR_ADVANTAGE:
            return self._get_score_advantage()
        else:
            return self._get_score_normal()
