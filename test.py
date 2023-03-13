import sm_16relind
import time

rel = sm_16relind.SM16relind(1)
print("================Turn on one by one  =====================")
for i in range(16):
    rel.set(i+1, 1)
    print("Relay " + str(i + 1) + " set to " + str(rel.get(i + 1)))
    print("All relays value: " + str( rel.get_all()))
    time.sleep(0.15)
print("================Turn off one by one  =====================")
for i in range(16):
    rel.set(i+1, 0)
    print("Relay " + str(i + 1) + " set to " + str(rel.get(i + 1)))
    print("All relays value: " + str(rel.get_all()))
    time.sleep(0.15)
print("================Turn all on  =====================")
time.sleep(1)
rel.set_all(65535)
print("All relays: " + str(rel.get_all()))
time.sleep(1)
print("================Turn all off  =====================")
rel.set_all(0)
print("All relays: " + str(rel.get_all()))
