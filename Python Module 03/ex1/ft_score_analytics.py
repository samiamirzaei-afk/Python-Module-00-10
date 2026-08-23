import sys

def is_number(value: int) -> bool:
    try:
        value += 1
        return True
    except(TypeError, ValueError):
        return False
def main(argc: int) -> int:
    if(argc < 2):
        print("No score given, Use: python3.11 ft_score_analytics.py score1 score2 score3...")
    print("=== Score tab ===")
    
    argv = sys.argv
    score_list = []
    j = 1
    k = 0
    tester = 100

    print(f"{len(argv[1])}")
    print(f"{len(argv[2])}")
    print(f"{len(argv[3])}")
    print(f"{len(argv[4])}")
    print(f"{len(argv[5])}")
    while(j < argc):
        if is_number(argv[j]) is True:
            score_list.append(argv[j])
        else:
            print(f"{argv[j]} is not a number")
        j += 1
    
    print(score_list)
    return(1);

    i = 1
    all_scores = ""
    while(i < argc):
        all_scores += argv[i]
        i += 1
        if(i < argc):
            all_scores += ", "
    print(f"[{all_scores}]")

if __name__ == "__main__":
    argc = len(sys.argv)
    main(argc)
#    score_list.extend(argv)
