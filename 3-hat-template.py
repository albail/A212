import sm_16relind
import time
import numpy

def allOff():
    hat0.set_all(0)
    hat1.set_all(0)
    hat2.set_all(0)

hat0 = sm_16relind.SM16relind(0)
hat1 = sm_16relind.SM16relind(1)
hat2 = sm_16relind.SM16relind(2)

# To change the first hat:
# hatNum.set(relay number, open/closed)
hat0.set(5,1)
# To change the second hat:
hat1.set(16,1)
# To change the third hat:
hat2.set(1,1)

# Time pause (seconds)
time.sleep(2)

allOff()