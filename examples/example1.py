import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from new_crane import Crane

class Crane1(): 
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

    def setTargetCurrentPosition(self):
        self.set_target_current_position()

    def set_target_trolley(self):
        self.crane.set_target_trolley(self.crane.get_motorcontroller_trolley_value() - 500) 


    def trolleyToTarget(self):
        while not self.crane.move_trolley_to_target():
            print(self.crane.trolley_to_target())
        

if(__name__== "__main__"): 
    def main(): 
        try: 
            f = open("accesscode_url.txt")
            try: 
                url = f.readline()
                accesscode = int(f.readline())
            except: 
                print("Something went wrong with reading the file")
            finally: 
                f.close()
        except: 
            print("Something went wrong with opening the file")
        
        crane = Crane1(url, accesscode)
        print("Async library in use, example code")
        print("...crane connection initialized. \n")
        print("Starting movement")
        crane.set_target_trolley()
        crane.trolleyToTarget()
        

main()