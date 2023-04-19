#Import relay-hat module
import sm_16relind

# Define variables
h0 = sm_16relind.SM16relind(0)
h1 = sm_16relind.SM16relind(1)
h2 = sm_16relind.SM16relind(2)

# turn all relays off
h0.set_all(0)
h1.set_all(0)
h2.set_all(0)

# ask for order input
# read back order
order = input('How would you like your pedals ordered? enter ord_xxxx: ')
print(order)

# only use variable called on by input
# if ord = 1234: h0.set(6,1)
#h0.set(2,1)
#h1.set(3,1)
#h2.set(4,1)
#h2.set(5,1)
     
# define all possible orders' and corresponding relays
ord_1234 = h0.set(6,1)
h0.set(2,1)
h1.set(3,1)
h2.set(4,1)
h2.set(5,1)

ord_2341 = h0.set(7,1)
h1.set(3,1)
h2.set(4,1)
h2.set(6,1)
h2.set(5,1)

ord_3412 = h1.set(5,1)
h2.set(4,1)
h2.set(6,1)
h0.set(2,1)
h1.set(1,1)

ord_4123 = h1.set(6,1)
h2.set(6,1)
h0.set(2,1)
h1.set(3,1)
h2.set(1,1)

ord_1324 = h0.set(6,1)
h0.set(3,1)
h1.set(3,1)
h1.set(4,1)
h2.set(5,1)

ord_2413 = h0.set(7,1)
h1.set(4,1)
h2.set(6,1)
h0.set(3,1)
h2.set(1,1)

ord_1243 = h0.set(6,1)
h0.set(2,1)
h1.set(4,1)
h2.set(8,1)
h2.set(1,1)

ord_1342 = h0.set(6,1)
h0.set(3,1)
h2.set(4,1)
h2.set(6,1)
h1.set(1,1)

ord_1423 = h0.set(6,1)
h0.set(4,1)
h2.set(7,1)
h1.set(3,1)
h2.set(1,1)

ord_1432 = h0.set(6,1)
h0.set(4,1)
h2.set(7,1)
h2.set(3,1)
h1.set(1,1)

ord_2134 = h0.set(7,1)
h1.set(2,1)
h0.set(3,1)
h2.set(4,1)
h2.set(5,1)

ord_2143 = h0.set(7,1)
h1.set(2,1)
h0.set(4,1)
h2.set(7,1)
h2.set(1,1)

ord_2314 = h0.set(7,1)
h1.set(3,1)
h2.set(2,1)
h0.set(4,1)
h2.set(5,1)

ord_2431 = h0.set(7,1)
h1.set(4,1)
h2.set(7,1)
h2.set(2,1)
h0.set(1,1)

ord_3124 = h1.set(5,1)
h2.set(2,1)
h0.set(2,1)
h1.set(4,1)
h2.set(5,1)

ord_3142 = h1.set(5,1)
h2.set(2,1)
h0.set(4,1)
h2.set(7,1)
h1.set(1,1)

ord_3241 = h1.set(5,1)
h1.set(3,1)
h1.set(4,1)
h2.set(6,1)
h0.set(1,1)

ord_3214 = h1.set(5,1)
h1.set(3,1)
h1.set(2,1)
h0.set(4,1)
h2.set(5,1)

ord_3421 = h1.set(5,1)
h2.set(4,1)
h2.set(7,1)
h1.set(2,1)
h0.set(1,1)

ord_4123 = h2.set(6,1)
h2.set(6,1)
h0.set(2,1)
h1.set(3,1)
h2.set(1,1)

ord_4132 = h2.set(6,1)
h2.set(6,1)
h0.set(3,1)
h1.set(3,1)
h1.set(1,1)

ord_4231 = h2.set(6,1)
h2.set(7,1)
h0.set(2,1)
h2.set(2,1)
h0.set(1,1)

ord_4213 = h2.set(6,1)
h2.set(7,1)
h1.set(2,1)
h0.set(3,1)
h2.set(1,1)

ord_4312 = h2.set(6,1)
h2.set(7,1)
h2.set(2,1)
h0.set(2,1)
h1.set(1,1)