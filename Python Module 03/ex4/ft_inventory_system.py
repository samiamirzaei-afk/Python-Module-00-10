import sys
import time

def arg_checker(inventory: dict, name: str, count: str) -> bool:
        if count.isdigit() == False:
            print(f"\"{name}:{count}\" is ignored (non numbers for quantity Error)")
            return False
        if name.isdigit() == True:
            print(f"\"{name}:{count}\" is ignored (numbers as name Error)")
            return False
        if name.strip() == None:
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
    inventory = dict()
    i = 1
    
    while(i < argc):
        print(f"\nchecking:\"{sys.argv[i]}\".....")
        time.sleep(0.3)
        try:
            name, count = sys.argv[i].split(':', 1)
        except ValueError:
            print(f"\"{sys.argv[i]}\" is ignored, (wrong layout Error)")
            i += 1
            continue
        if arg_checker(inventory, name, count) == False:
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
    

if __name__ == "__main__":
    _ = main()

