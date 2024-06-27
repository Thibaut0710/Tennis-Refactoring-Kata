import os
import unittest

from StringBuilderConsole import StringBuilderConsole
from tennis1 import TennisGame1


class GoldenMasterTest(unittest.TestCase):
    DIR = "golden_master_files"

    def run_a_game(self, player1_name, player2_name, actions):
        output_console = StringBuilderConsole()
        game = TennisGame1(player1_name, player2_name)

        for action in actions:
            if action.startswith("P1"):
                game.won_point(player1_name)
            else:
                game.won_point(player2_name)
            output_console.write(game.score())

        return output_console.get_output()

    def generate_file_name(self, player1_name, player2_name, actions):
        return f"{player1_name}_{player2_name}-{'-'.join(actions)}.txt"

    def record(self, player1_name, player2_name, actions):
        output = self.run_a_game(player1_name, player2_name, actions)
        file_name = self.generate_file_name(player1_name, player2_name, actions)

        if not os.path.exists(self.DIR):
            os.makedirs(self.DIR)

        with open(os.path.join(self.DIR, file_name), 'w', encoding='utf-8') as file:
            file.write(output)

    def replay(self, player1_name, player2_name, actions):
        output = self.run_a_game(player1_name, player2_name, actions)
        file_name = self.generate_file_name(player1_name, player2_name, actions)

        with open(os.path.join(self.DIR, file_name), 'r', encoding='utf-8') as file:
            expected_output = file.read()

        self.assertEqual(expected_output, output)


# Génération des fichiers Golden Master
if __name__ == "__main__":
    test_instance = GoldenMasterTest()

    test_instance.record("Alice", "Bob", ["P1", "P2", "P1", "P1", "P2", "P1", "P2"])
    test_instance.record("John", "Jane", ["P2", "P1", "P2", "P2", "P1", "P1", "P2"])
    test_instance.record("Chris", "Pat", ["P1", "P1", "P2", "P1", "P2", "P2", "P2"])
    test_instance.record("Mika", "Alex", ["P2", "P1", "P2", "P1", "P2", "P2", "P1"])
    test_instance.record("Sam", "Jordan", ["P1", "P2", "P1", "P2", "P2", "P1", "P2"])
    test_instance.record("Taylor", "Jamie", ["P2", "P1", "P2", "P2", "P1", "P2", "P1"])
    test_instance.record("Casey", "Morgan", ["P1", "P2", "P1", "P1", "P2", "P2", "P2"])
    test_instance.record("Robin", "Drew", ["P2", "P1", "P2", "P2", "P2", "P1", "P1"])
    test_instance.record("Jordan", "Blake", ["P1", "P1", "P2", "P2", "P1", "P2", "P1"])
    test_instance.record("Alexis", "Jesse", ["P2", "P2", "P1", "P2", "P1", "P1", "P1"])