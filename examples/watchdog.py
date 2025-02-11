import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from new_crane import Crane

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

    #def stop_all(): 



if(__name__ == "__main__"):
    def main():
        try: 
            f = open("accesscode_url.txt")
            try: 
                url = str(f.readline())
                accesscode = int(f.readline())
            except: 
                print("Something went wrong with reading the file")
            finally: 
                f.close()
        except: 
            print("Something went wrong with opening the file")


        print("Async library in use, watchdog code")
        print("\nInitializing crane connection...\n--Make sure the device is connected to correct WiFi network!--")
        watchdog = Watchdog(url, accesscode)
        print("...crane connection initialized.\n")
        print("Starting watchdog")
        watchdog.updateWatchdogLoop()

    main()
