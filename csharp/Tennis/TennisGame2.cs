using System.Collections.Generic;

namespace Tennis
{
    public class TennisGame2 : ITennisGame
    {
        private int p1point;
        private int p2point;

        private string player1Name;
        private string player2Name;

        private static readonly string[] pointDescriptions = { "Love", "Fifteen", "Thirty", "Forty" };

        // Historique des points
        private List<string> scoreHistory;

        public TennisGame2(string player1Name, string player2Name)
        {
            this.player1Name = player1Name;
            this.player2Name = player2Name;
            p1point = 0;
            p2point = 0;
            scoreHistory = new List<string>();
            RecordScore(); // Enregistrer le score initial
        }

        public string GetScore()
        {
            string score;
            if (p1point == p2point)
            {
                score = p1point < 3 ? $"{pointDescriptions[p1point]}-All" : "Deuce";
            }
            else if (p1point >= 4 || p2point >= 4)
            {
                int scoreDifference = p1point - p2point;
                if (scoreDifference == 1) score = "Advantage player1";
                else if (scoreDifference == -1) score = "Advantage player2";
                else if (scoreDifference >= 2) score = "Win for player1";
                else score = "Win for player2";
            }
            else
            {
                score = $"{pointDescriptions[p1point]}-{pointDescriptions[p2point]}";
            }

            RecordScore();
            return score;
        }

        private void RecordScore()
        {
            scoreHistory.Add($"{pointDescriptions[Math.Min(p1point, 3)]}-{pointDescriptions[Math.min(p2point, 3)]}");
        }

        public void SetP1Score(int number)
        {
            p1point += number;
            RecordScore();
        }

        public void SetP2Score(int number)
        {
            p2point += number;
            RecordScore();
        }

        private void P1Score()
        {
            p1point++;
            RecordScore();
        }

        private void P2Score()
        {
            p2point++;
            RecordScore();
        }

        public void WonPoint(string player)
        {
            if (player == "player1")
                P1Score();
            else
                P2Score();
        }

        // Nouvelle fonctionnalité : Affichage de l'historique des scores
        public List<string> GetScoreHistory()
        {
            return new List<string>(scoreHistory);
        }

        // Nouvelle fonctionnalité : Réinitialisation du jeu
        public void ResetGame()
        {
            p1point = 0;
            p2point = 0;
            scoreHistory.Clear();
            RecordScore(); // Enregistrer le score initial après la réinitialisation
        }
    }
}
