import sys

DIGITS = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        }

def is_signed(value: str) -> tuple[bool, int]:
    if value[0] == '+':
        return True, 1
    if value[0] == '-':
        return True, -1
    return False, 1

def atoi(value: str) -> int:
    sign = 1
    has_sign = False
    number = 0;
    i = 0

    has_sign, sign = is_signed(value)
    if has_sign:
        i += 1

    while i < len(value):
        number = number * 10 + DIGITS[value[i]]
        i += 1
    return (number * sign)
        

def is_number(value: str) -> bool:
    if len(value) == 0:
        return(False)
    number = 0
    i = 0
    has_sign = False

    has_sign, _ = is_signed(value)
    if has_sign:
        i += 1

    while i < len(value):
        if value[i] not in DIGITS:
            return False
        i += 1
    return True


def main(argc: int) -> int:
    if(argc < 2):
        print("No score given, Use: python3.11 ft_score_analytics.py score1 score2 score3...")
    print("=== Score tab ===")
    
    argv = sys.argv
    score_list = []
    i = 1
    while(i < argc):
        if is_number(argv[i]) is True:
            score_list.append(atoi(argv[i]))
        else:
            print(f"{argv[i]} is not a number")
        i += 1
    
    print(score_list)
    return(1);

if __name__ == "__main__":
    argc = len(sys.argv)
    main(argc)
#    score_list.extend(argv)
