from time import sleep
import threading
import sys

delay = 0.5
notImaging = True

def processImg():
    i = 0
    while getattr(thread1, "notImaging", True):
        print("Processed img " + str(i+1))
        i += 1
        sleep(delay)
    print("Quit processing")

def updateIMU(updates):
    for n in range(updates):
        print("IMU update " + str(n+1))
        sleep(delay)
    print("on imaging leg")
    thread1.notImaging = False

thread1 = threading.Thread(target=processImg)
thread2 = threading.Thread(target=updateIMU, args=(5,))

thread1.notImaging = True

thread1.start()
sleep(0.1)
thread2.start()

thread1.join()
thread2.join()

print("--------------------")
