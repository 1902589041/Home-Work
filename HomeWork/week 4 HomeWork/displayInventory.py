inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def TotalNumInventory(inventory) :
    result = 0;
    for i, j in inventory.items() :
        result += j;
    print("Total number of items: " + str(result))
TotalNumInventory(inventory)