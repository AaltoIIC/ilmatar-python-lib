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


    def craneToTarget(self): 
        self.crane.set_target_bridge(15000)
        dist_to_target = abs(int(self.crane.bridge_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = self.crane.speed_profile_bridge(dist_to_target) # Create speed profile
            while not self.crane.move_bridge_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        print("Crane at corner 2")

        self.crane.set_target_trolley(4600)
        dist_to_target = abs(int(self.crane.trolley_to_target())) 
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = self.crane.speed_profile_trolley(dist_to_target) # Create speed profile
            while not self.crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        print("Crane at corner 3")

        self.crane.set_target_hoist(2200)
        while not self.crane.move_hoist_to_target(): #Lower the hoist at corner 3 (1162)
            time.sleep(1)
        print("Hoist lowered")

        self.crane.set_target_hoist(3060)
        while not self.crane.move_hoist_to_target(): #Bring the hoist back up at corner 3
            time.sleep(1)
        print("Hoist back up")

        self.crane.set_target_bridge(18000)
        dist_to_target = abs(int(self.crane.bridge_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = self.crane.speed_profile_bridge(dist_to_target) # Create speed profile
            while not self.crane.move_bridge_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        print("Crane at corner 4")

        self.crane.set_target_trolley(8500)
        dist_to_target = abs(int(self.crane.trolley_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = self.crane.speed_profile_trolley(dist_to_target) # Create speed profile
            while not self.crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        
        print("Crane at starting point")
        print("Example 2 finished")
        

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
        crane.craneToTarget()

        

main()