import random
import time

for i in range(10):
    print(i)
    sleep_time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    time.sleep(random.choice(sleep_time))
