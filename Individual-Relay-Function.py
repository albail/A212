#Import relay-hat module
import sm_16relind

# Define variables
h0 = sm_16relind.SM16relind(0)
h1 = sm_16relind.SM16relind(1)
h2 = sm_16relind.SM16relind(2)

# Run Code:
h0.set(1,1)
h1.set(5,1)
h2.set(10,1)

# ///
# 
# if set(num) > 12:
#     h = h + 1:
#     num = num - 12:
#     