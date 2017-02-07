#This program utilizes three dictionaries. One for a shopping list,
#another for the grocers inventory, and a last one for the prices.
#The program takes these dictionaries and uses two methods. One
#to display inventory and prices and then another to show what
#the user wants to purchase and then calculates the bill and
#notifies the user for any items that are not in stock.
def main():
    #predefined dictionaries
    shoppingList = {'potatoes': 2, 'onions': 1, 'lettuce': 5}
    inventory = {'potatoes': 6, 'lettuce': 0, 'onions': 32, 'carrots': 15}
    prices = {'potatoes': 4, 'lettuce': 2,'onions': 1.5, 'carrots': 3}

    #method calls
    printInventory(inventory, prices)
    computeBill(shoppingList, inventory, prices)
    
#print inventory method
def printInventory(stock, pricing):
    print('*********CUB Foods Inventory**********')
    print('**************************************')
    print('Items    Price       Quantity   Value ')
    print('Carrot   ${}           {}         ${}'.format(pricing['carrots'],stock['carrots'], (pricing['carrots']*stock['carrots'])))
    print('Lettuce  ${}           {}          ${}'.format(pricing['lettuce'],stock['lettuce'], (pricing['lettuce']*stock['lettuce'])))
    print('Onion    ${}         {}         ${}'.format(pricing['onions'],stock['onions'], (pricing['onions']*stock['onions'])))
    print('Potato   ${}           {}          ${}'.format(pricing['potatoes'],stock['potatoes'], (pricing['potatoes']*stock['potatoes'])))

#compute the bill method
def computeBill(buyer, stock, pricing):
    amount = 0
    
    print('\nYour shopping bill is:\n')

    #loop for going through the various keys of the dicitonary.
    for key in buyer.keys():
        if key in stock.keys() and stock[key] > 0:
            print('{} {} at $ {} each   - total ${}'.format(buyer[key],key , pricing[key], (buyer[key]*pricing[key])))
            amount += buyer[key]*pricing[key]
        else:
            print('{}                  - out of stock.'.format(key))

    print('\nThe total bill is $ {}'.format(amount))
           
if __name__ == "__main__": main()
