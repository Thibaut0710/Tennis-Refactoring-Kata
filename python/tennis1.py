class TennisGame1:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    SCORE_NAMES = {
        "EN": {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
            "All": "All",
            "Deuce": "Deuce",
            "Advantage": "Advantage",
            "Win": "Win"
        },
        "FR": {
            0: "Zéro",
            1: "Quinze",
            2: "Trente",
            3: "Quarante",
            "All": "Égalité",
            "Deuce": "Égalité",
            "Advantage": "Avantage",
            "Win": "Victoire"
        }
    }

    def __init__(self, player1Name, player2Name, language="FR"):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.language = language

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        elif playerName == self.player2Name:
            self.p2points += 1
        else:
            raise ValueError(f"Unknown player name: {playerName}")

    def _is_tie(self):
        return self.p1points == self.p2points

    def _is_endgame(self):
        return self.p1points >= 4 or self.p2points >= 4

    def _get_tie_score(self):
        if self.p1points in [0, 1, 2]:
            return f"{self.SCORE_NAMES[self.language][self.p1points]}-{self.SCORE_NAMES[self.language]['All']}"
        else:
            return self.SCORE_NAMES[self.language]["Deuce"]

    def _get_endgame_score(self):
        minusResult = self.p1points - self.p2points
        if minusResult == 1:
            return f"{self.SCORE_NAMES[self.language]['Advantage']} {self.player1Name}"
        elif minusResult == -1:
            return f"{self.SCORE_NAMES[self.language]['Advantage']} {self.player2Name}"
        elif minusResult >= 2:
            return f"{self.SCORE_NAMES[self.language]['Win']} {self.player1Name}"
        else:
            return f"{self.SCORE_NAMES[self.language]['Win']} {self.player2Name}"

    def _get_standard_score(self):
        return f"{self.SCORE_NAMES[self.language][self.p1points]}-{self.SCORE_NAMES[self.language][self.p2points]}"

    def score(self):
        if self._is_tie():
            return self._get_tie_score()
        elif self._is_endgame():
            return self._get_endgame_score()
        else:
            return self._get_standard_score()
