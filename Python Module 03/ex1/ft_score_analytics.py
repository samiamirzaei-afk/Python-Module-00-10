import sys

def is_number(value: int) -> bool:
    try:
        _ = int(value)
        return True
    except(TypeError, ValueError):
        return False

def main(argc: int) -> int:
    if(argc < 2):
        print("No score given, Use: python3.11 ft_score_analytics.py score1 score2 score3...")
        return(1)
    print("=== Score tab ===")
    
    argv = sys.argv
    score_list = []
    j = 1

    while(j < argc):
        if is_number(argv[j]) is True:
            score_list.append(int(argv[j]))
        else:
            print(f"{argv[j]} is not a number")
        j += 1
    print(score_list)
    print(f"total players: {len(score_list)}")
    print(f"total score: {sum(score_list)}")
    print(f"highest score: {max(score_list)}")
    print(f"smallest score: {min(score_list)}")
    print(f"avrage score: {(sum(score_list) / len(score_list))}")
    print(f"range score: {(max(score_list) - min(score_list))}")




    ''' 
    temp = score_list.__sizeof__()
    print(score_list)
    print(f"{temp}")
    '''
if __name__ == "__main__":
    argc = len(sys.argv)
    main(argc)
#    score_list.extend(argv)
