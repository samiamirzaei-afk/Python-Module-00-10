import sys
import time


def arg_checker(inventory: dict[str, int], name: str, count: str) -> bool:
    if not count.isdigit() is True:
        print(f"\"{name}:{count}\" is ignored"
              "(non numbers for quantity Error)")
        return False
    if name.isdigit() is True:
        print(f"\"{name}:{count}\" is ignored (numbers as name Error)")
        return False
    if name.strip() is None:
        print(f"\"{name}:{count}\" is ignored, (empty name Error)")
        return False
    if name in inventory:
        print(f"\"{name}:{count}\" is ignored, (duplicate name Error)")
        return False
    return(True)


def main() -> int:
    argc = len(sys.argv)
    if(argc < 2):
        print("no arguments given, example of layout: <item_name:quantity>")
        return(1)
    inventory: dict[str, int] = dict()
    i = 1

    while(i < argc):
        print(f"\nchecking:\"{sys.argv[i]}\".....")
        time.sleep(0.1)
        try:
            name, count = sys.argv[i].split(':', 1)
        except ValueError:
            print(f"\"{sys.argv[i]}\" is ignored, (wrong layout Error)")
            i += 1
            continue
        if arg_checker(inventory, name, count) is False:
            i += 1
            continue
        print(f"\"{sys.argv[i]}\" has been added to the list ✓")
        inventory[name] = int(count)
        i += 1
    print("current inventory:")
    print(inventory)
    total_name = len(inventory)
    total_count = sum(inventory.values())
    print(f"{total_name} unique items, {total_count} items total")

    for keys in inventory:
        current = inventory[keys]
        share = current * 100 / total_count
        print(f"{keys} is {round(share, 1)}% of items")

    i = 0
    min_value = min(inventory.values())
    max_value = max(inventory.values())

    for max_name in inventory:
        if inventory[max_name] == max_value:
            break
    for min_name in inventory:
        if inventory[min_name] == min_value:
            break
    print("lowest values:", min_name, min_value)
    print("highest values:", max_name, max_value)

    inventory.update({"gay": 100})
    print("updated inventory:")
    print(inventory)
    return(0)


if __name__ == "__main__":
    _ = main()
