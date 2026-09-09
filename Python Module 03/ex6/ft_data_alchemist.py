import random
import sys


def main() -> list[str]:
    l_players = ["Mihrdat", "Claudio", "Djehuti", "merse", "Frans",
               "Bohdana", "corona", "Áurea", "Paraskeve", "Helēna",
               "katharina", "Yaniel", "navy"]
    player_all_cap = [player.capitalize() for player in l_players]
    player_only_cap = [player for player in l_players if 
                       player == player.capitalize()]


    print("all players list\n", l_players)
    print("\nOG_caps\n", player_only_cap)
    print("\nall_caps\n", player_all_cap)

    return player_all_cap


def main1(l_all_caps: list[str]) -> int:
    
    d_scores = dict()
    d_scores = {player: random.randint(1, 1000) for player in l_all_caps}
    
    print(d_scores)

    total_score = 0
    for player in l_all_caps:
        total_score += d_scores[player]
    avrage = total_score / (len(l_all_caps))

    d_high_scores = {player: d_scores[player] for player in l_all_caps if d_scores[player] > avrage}

    print(f"avrage score: {round(avrage, 2)}")
    print(f"high scores:\n", d_high_scores)



if __name__ == "__main__":
    result = main()
    _ = main1(result)

