
#Program tells you how many different ways you can make change for a given amount of money
def main():
        cents = input("How much money would you change for (in cents)? ")
        print("There are", makeChange(int(cents)),  "ways to make change for", cents, "cents")

def makeChange(cents):
    return makeChangeHelp(cents, [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1], 0)  # basis values for money in cents

#return the number of ways a cent value can be arranged in a given basis
def makeChangeHelp(cents, basis, index):
    if(cents == 0):  # We have successfully found a way to create this amount of money
        return 1
    while (cents < basis[index]):  # if the basis element is too large, go to the next largest one
        index+=1
    if (index==len(basis)-1): # if we are down to just pennies, then we have found a way and we are done
        return 1
    numOfPaths = (cents // basis[index]) + 1  # number of times that basis element can be used to fill the amount of money we need
    counter = 0
    baseValue = basis[index]   # base value to subtract from our money
    index+=1  # move to the next basis element
    for i in range(numOfPaths):  # to get all the combinations, try every single way that the current basis element can
        counter+= makeChangeHelp(cents-i*baseValue,basis, index)  # contribute to the amount of money we have left
    return counter  # once done getting all the ways that the basis can help, go back up to the larger basis element
    # and complete the recursion



if __name__ == '__main__': main()
