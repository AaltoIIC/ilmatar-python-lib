import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from crane import Crane

class Watchdog():
    def __init__(self, url, accesscode):
        self.accesscode = accesscode
        self.url = url
        self.crane = Crane(url)
        self.setAccesscode(accesscode)


    def setAccesscode(self, accesscode=None):
        if(accesscode == None):
            accesscode = self.accesscode
        if(type(accesscode) != int):
            return False
        self.accesscode = accesscode
        if(self.crane != None and self.accesscode != None):
            self.crane.set_accesscode(self.accesscode)
            return True
        return False


    def updateWatchdogLoop(self):
        while self.setAccesscode():
            self.crane.increment_watchdog()
            time.sleep(0.1)
            print("Incremented")


if(__name__ == "__main__"):
    def main():
        url = input("URL: ")
        accesscode = int(input("Accescode: "))
        while(not isinstance(accesscode, int)):
            print("Accescode needs to be integer")
            accesscode = int(input("Accescode: "))
        print("\nInitializing crane connection...\n--Make sure the device is connected to correct WiFi network!--")
        watchdog = Watchdog(url, accesscode)
        print("...crane connection initialized.\n")
        print("Starting watchdog")
        watchdog.updateWatchdogLoop()

    main()
