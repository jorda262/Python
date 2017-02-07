#This program defines lists and dictionaries and uses them to
#manipulate a wallet of items. The wallet contains items of
#cash, coupons, ids, credit cards, and items can be added
#or removed. It then prints out the various items in their
#category type.
def main():
    #Defining the wallet and the various items of the wallet
    quantity= {'twenties': 2, 'tens': 1, 'fives': 0, 'ones': 4}
    listOfCreditCards = ['Visa','Discover', 'Master Card']
    listOfIDs = ['Drivers License', 'Student ID']
    wallet = {'money':quantity, 'cards': listOfCreditCards, 'ids': listOfIDs}

    #Initial print out of the contents of the wallet
    print('Wallet Contents:')
    print('\nCredit Cards:')
    for i in range(0, len(listOfCreditCards)):
        print(listOfCreditCards[i])

    print('\nIDs:')
    for i in range(0, len(listOfIDs)):
        print(listOfIDs[i])

    totalAmount = (quantity['twenties']*20) + (quantity['tens']*10) + (quantity['fives']*5) + (quantity['ones']*1)

    print('\nTotal cash is: ${}'.format(totalAmount));

    #Creates a coupon dictionary and adds items to it,
    coupons = {}
    coupons['Target'] = 'toothpaste'
    coupons['Kohls'] = 'shirt'
    coupons['Cub'] = 'meat'

    wallet['coupons'] = coupons

    quantity['twenties'] = (quantity['twenties'] + 3)

    #Removes a card from the wallet
    listOfCreditCards.remove('Discover')

    #Prints the new contents of the wallet after additions and removals.\
    print('\nAfter changes, wallet contents are:')
    print('\nCredit Cards:')
    for i in range(0, len(listOfCreditCards)):
        print(listOfCreditCards[i])

    print('\nIDs:')
    for i in range(0, len(listOfIDs)):
        print(listOfIDs[i])

    print('\nCoupons:')
    for key in coupons:
        print (key, coupons[key])

    totalAmount = (quantity['twenties']*20) + (quantity['tens']*10) + (quantity['fives']*5) + (quantity['ones']*1)
    print('\nTotal cash is: ${}'.format(totalAmount));
    

if __name__ == "__main__": main()
