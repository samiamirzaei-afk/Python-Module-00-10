def ft_putnbr(current_day: int, max_days: int) -> None:
    if current_day <= max_days:
        print(f"Day {current_day}")
        ft_putnbr(current_day + 1, max_days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    i = 1
    ft_putnbr(i, days)
