import random


def gen_player_achievements(achievements: list[str]) -> set[str]:

    total = len(achievements)
    skill = random.randint(0, total)
    result = set(random.sample(achievements, skill))
    return result


def main() -> int:
    '''
    print(achievements)
    if "Nether" in achievements:
        print("correct")
    if "Gond" not in  achievements:
        print("correct")
    '''
    achievements = ["Getting Wood", "Minecraft",
                    "Stone Age", "Acquire Hardware", "Suit Up", "Take Aim",
                    "Hot Stuff", "DIAMONDS", "Nether", "Into Fire",
                    "Local Brewery",
                    "The End", "Free the End", "Enchanter", "Top Notch"]

    claude = gen_player_achievements(achievements)
    chatgpt = gen_player_achievements(achievements)
    deepseek = gen_player_achievements(achievements)
    kimi = gen_player_achievements(achievements)
    print(f"{claude=},\n total of {len(claude)}")
    print(f"{chatgpt=},\n total of {len(chatgpt)}")
    print(f"{kimi=},\n total of {len(kimi)}")
    print(f"{deepseek=},\n total of {len(deepseek)}")
    print(f"{achievements=},\n total of {len(achievements)}\n")
    all_players = set.intersection(claude, chatgpt, deepseek, kimi)
    print(f"common achievements:{all_players}\n")
    claude_only = set.difference(claude, chatgpt, deepseek, kimi)
    chatgpt_only = set.difference(chatgpt, claude, deepseek, kimi)
    deepseek_only = set.difference(deepseek, chatgpt, claude, kimi)
    kimi_only = set.difference(kimi, deepseek, chatgpt, claude)
    print(f"{claude_only=}")
    print(f"{chatgpt_only=}")
    print(f"{deepseek_only=}")
    print(f"{kimi_only=}\n")
    claude_missing = set.difference(set(achievements), claude)
    chatgpt_missing = set.difference(set(achievements), chatgpt)
    deepseek_missing = set.difference(set(achievements), deepseek)
    kimi_missing = set.difference(set(achievements), kimi)
    print(f"{claude_missing=}")
    print(f"{chatgpt_missing=}")
    print(f"{deepseek_missing=}")
    print(f"{kimi_missing=}\n")
    return(1)

if __name__ == "__main__":
    _ = main()
