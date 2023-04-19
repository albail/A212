#Import relay-hat module
import sm_16relind
import time

# Define variables
h0 = sm_16relind.SM16relind(0)
h1 = sm_16relind.SM16relind(1)
h2 = sm_16relind.SM16relind(2)

pedal_1 = 0
pedal_2 = 0
pedal_3 = 0
pedal_4 = 0

# Turns all relays off.
print('Relays shutting off in 3 seconds.')
# time.sleep(3)
h0.set_all(0)
h1.set_all(0)
h2.set_all(0)

# define all possible orders' and corresponding relays
print('How would you like your pedals ordered? If direct out, click enter:')
order = input()

orderList = [int(i) for i in str(order)]

if len(orderList) > 4:
    print('Too many numbers, please try again.')
else:
    if len(orderList) != 0:
    #  Will control the inputted number     
        while len(orderList) >= 1:
            if len(orderList) == 4:
                pedal_4 = orderList.pop(3)
#                 print(pedal_4)
            if len(orderList) == 3:
                pedal_3 = orderList.pop(2)
#                 print(pedal_3)
            if len(orderList) == 2:
                pedal_2 = orderList.pop(1)
#                 print(pedal_2)
            if len(orderList) == 1:
                pedal_1 = orderList.pop(0)
#                 print(pedal_1)
#  This should send the signal for direct out
    else:
        h0.set(5,1)

print('Order:')
print(pedal_1)
print(pedal_2)
print(pedal_3)
print(pedal_4)