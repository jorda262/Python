def main():
    costOfShare = 35.0
    numberOfShares = 750
    commissionPercentage = 0.02
    stockCost = costOfShare * numberOfShares
    commissionCost = stockCost * commissionPercentage
    totalCost = stockCost + commissionCost
    print('Stock cost: $',stockCost)
    print('Commission Cost: $', commissionCost)
    print('Total cost: $', totalCost)
    
if __name__ == "__main__": main()
