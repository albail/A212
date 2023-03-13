#Import relay-hat module
import sm_16relind
import numpy

# Make a function that swaps the first and second half of list.
def listSwap(input):
    L = len(input)//2
    
    for i in range(L):
        temp = input[i]
        input[i] = input[i+L]
        input[i+L] = temp

# Initialize list of hats in binary
blankHatList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Prompt for relay hat ID number
print('Which hat ID would you like to control?')
chosenID = (input())

# Control hats on board ID:0 with rel.set command
rel = sm_16relind.SM16relind(int(chosenID))

#  Turn all hats off.
rel.set_all(0)

# Ask for what hats to turn on.
print('Which relays would you like to turn on? Seperate by adding a comma, no space.')
chosenHats = (input())

# Seperates user entries into list.
hatsList = chosenHats.split(',')

# Takes each entry and sets the binary correctly to turn the designated hat on.
for hatFromList in hatsList:
    if int(hatFromList) > 0:
        blankHatList[int(hatFromList)-1] = 1

# Reverses list... not sure why but the board goes backwards in binary/16-bit.
blankHatListClean = list(reversed(blankHatList))

# Flips 1-8 and 9-16... not sure why but the board flips these in binary/16-bit.
listSwap(blankHatListClean)

# print(blankHatListClean)

bitmapHatList = numpy.packbits(blankHatListClean).view(numpy.uint16)

# print(bitmapHatList)

rel.set_all(bitmapHatList)