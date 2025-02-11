import sys
import os
import time
from watchdog import Watchdog
import random
import threading


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

    def connect(self):
        """Connect for 5 seconds, then disconnect."""
        self.crane.connect()
        print("connected", self.crane.connect())
        time.sleep(5)
        self.crane.disconnect()
        print("disconnected", self.crane.disconnect())

    def watchdog(self):
        """Test watchdog related functions."""
        out = self.crane.get_watchdog()

        for i in range(10):
            self.crane.increment_watchdog()

        out = self.crane.get_watchdog()
        print("nyt:", out)

    def access(self):
        """Test access code related functions."""
        out = self.crane.get_accesscode()
        print("old: ", out)
        #self.crane.set_accesscode(55556666)
        #out = self.crane.get_accesscode()
        #print("new: ", out)

    def poses(self):
        """Receive poitions from laser and motor controller."""
        trol_pos_abs = self.crane.get_trolley_position_absolute()
        trol_pos_motor = self.crane.get_motorcontroller_trolley_value()

        bridge_pos_abs = self.crane.get_bridge_position_absolute()
        bridge_pos_motor = self.crane.get_motorcontroller_bridge_value()

        hoist_pos_abs = self.crane.get_hoist_position_absolute()
        hoist_pos_motor = self.crane.get_motorcontroller_hoist_value()

        coord_abs = self.crane.get_coordinates_absolute()
        coord_motor = self.crane.get_motorcontroller_all()

        print("Trolley abs: ", trol_pos_abs, "Trolley motor: ", trol_pos_motor)
        print("Bridge abs: ", bridge_pos_abs, "Bridge motor: ", bridge_pos_motor)
        print("Hoist abs: ", hoist_pos_abs, "Hoist motor: ", hoist_pos_motor)
        print("Abs coord: ", coord_abs, "Motor coord: ", coord_motor)

    def poses_timestamp(self):
        """Receive timestamps for positions."""
        trol_pos_motor = self.crane.get_motorcontroller_trolley_value_with_timestamp()
        bridge_pos_motor = self.crane.get_motorcontroller_bridge_value_with_timestamp()

        print("Trolley ts: ", trol_pos_motor, "Bridge ts: ", bridge_pos_motor)

    def speeds_timestamp(self):
        """Receive speeds with timestamps."""
        trol_spd_ts = self.crane.get_speed_trolley_value_with_timestamp()
        bridge_spd_ts = self.crane.get_speed_bridge_value_with_timestamp()
        hoist_spd_ts = self.crane.get_speed_hoist_value_with_timestamp()

        print("Trolley spd ts: ", trol_spd_ts, "Bridge spd ts: ", bridge_spd_ts, "Hoist spd ts: ", hoist_spd_ts)

    def set_target(self):
        """Set target to ready movement. Doesnt do anything by itself."""
        self.crane.set_target_trolley(1000)
        bridge_tg = self.crane.set_target_bridge(10000)
        hoist_tg = self.crane.set_target_hoist(500)
        moving = self.crane.set_moving_height(100)
        curr_pos_tg = self.crane.set_target_current_position()

        print(curr_pos_tg)

    def get_load(self):
        """Get load measurements from hoist."""
        print("Crane Load: ", self.crane.get_load())
        print("Crane Load tared: ", self.crane.get_load_tared())
        print("Get Datetime: ", self.crane.get_datetime())

    def dist_to_target(self):
        """Calculate distance to set target."""
        print("Starting!")
        self.crane.set_target_trolley(17000)
        print("Trolley to target: ", self.crane.trolley_to_target())

        self.crane.set_target_bridge(5000)
        print("Bridge to target: ", self.crane.bridge_to_target())

        self.crane.set_target_hoist(2000)
        print("Hoist to target: ", self.crane.hoist_to_target())

        self.crane.set_moving_height(2100)
        print("Moving height to target: ", self.crane.hoist_to_moving_height())

    def move_to_target(self):
        """Movement commands to reach target."""
        self.crane.set_target_trolley(5000)
        while not self.crane.move_trolley_to_target():
            time.sleep(1)

        self.crane.set_target_bridge(17000)
        while not self.crane.move_bridge_to_target():
            time.sleep(1)

        self.crane.set_target_hoist(1800)
        while not self.crane.move_hoist_to_target():
            time.sleep(1)

        #while not self.crane.move_hoist_to_target_precise(2000):
        #    time.sleep(1)
        self.crane.set_target_hoist(1600)
        print("Moving to target lift")
        while not self.crane.move_hoist_to_target_lift():
            time.sleep(1)

        self.crane.set_moving_height(3060)
        print("Moving to moving height")
        while not self.crane.move_hoist_to_moving_height():
            time.sleep(1)
        
    def move_home(self):
        """Move to set home location. Raise hoist before moving."""
        print("I am going home! \n Moving hoist up")
        self.crane.set_target_hoist(3060)
        while not self.crane.move_hoist_to_target():
            time.sleep(1)

        self.crane.set_target_trolley(6000)
        while not self.crane.move_trolley_to_target():
            time.sleep(1)

        self.crane.set_target_bridge(18000)
        while not self.crane.move_bridge_to_target():
            time.sleep(1)
        print("I am home now!")

    def move_to_target_slow(self):
        """Move to target but slowly."""
        print("Starting!")
        self.crane.set_target_trolley(5000)
        while not self.crane.move_trolley_to_target_p():
            time.sleep(1)
        
        print("Trolley on target!")

        self.crane.set_target_bridge(17000)
        while not self.crane.move_bridge_to_target_p():
            time.sleep(1)

        print("Bridge on target!")

        self.crane.set_target_hoist(1800)
        while not self.crane.move_hoist_to_target_p():
            time.sleep(1)

        print("Hoist on target!")

        self.crane.set_moving_height(3060)
        while not self.crane.move_hoist_to_moving_height_p():
            time.sleep(1)

        print("Hoist in moving height!")

    def zero_pos(self):
        """Zero current position, move to home and check position. Works until restart."""
        print("Current pos: ", self.crane.get_motorcontroller_all())
        self.crane.zero_trolley_position()
        self.crane.zero_bridge_position()
        self.crane.zero_hoist_position()
        #print("After zeroing pos: ", self.crane.get_motorcontroller_all())

        t = self.crane.get_zero_trolley_position()
        b = self.crane.get_zero_bridge_position()
        h = self.crane.get_zero_hoist_position()
        print("Zeroed position: ", t, b, h)

        self.move_home()

        # Differences
        td = self.crane.get_difference_trolley_to_zero()
        bd = self.crane.get_difference_bridge_to_zero()
        hd = self.crane.get_difference_hoist_to_zero()
        print("Pos from last zeroed to current: ", td, bd, hd)

        alld = self.crane.get_difference_all_to_zero()
        print("Pos from last zeroed to current all: ", alld)

    def set_movement_direction(self):
        """Move forwards for n sec, stop, then backwards on all axes.
        Needs "set_trolley_speed" or other to work."""

        # Trolley
        self.crane.set_trolley_speed(70)
        print("Trolley speed: ", self.crane.get_trolley_speed)
        self.crane.move_trolley_forward()
        #print(self.crane.get_trolley_forward())
        #print(self.crane.get_trolley_backward())
        time.sleep(2)
        self.crane.stop_trolley()
        time.sleep(1)
        self.crane.set_trolley_speed(70)
        self.crane.move_trolley_backward()
        #print(self.crane.get_trolley_backward())
        #print(self.crane.get_trolley_backward())
        time.sleep(2)
        self.crane.stop_trolley()
        print("Trolley done")

        # Bridge
        self.crane.set_bridge_speed(70)
        print("Brdige speed: ", self.crane.get_bridge_speed)
        self.crane.move_bridge_forward()
        #print(self.crane.get_bridge_forward())
        #print(self.crane.get_bridge_backward())
        time.sleep(2)
        self.crane.stop_bridge()
        time.sleep(1)
        self.crane.set_bridge_speed(70)
        self.crane.move_bridge_backward()
        #print(self.crane.get_bridge_forward())
        #print(self.crane.get_bridge_backward())
        time.sleep(2)
        self.crane.stop_bridge()
        print("Bridge done")

        # Hoist
        self.crane.set_hoist_speed(70)
        print("Hoist speed: ", self.crane.get_hoist_speed)
        self.crane.move_hoist_up()
        #print(self.crane.get_hoist_up())
        #print(self.crane.get_hoist_down())
        time.sleep(3)
        self.crane.stop_hoist()
        time.sleep(1)
        self.crane.set_hoist_speed(70)
        self.crane.move_hoist_down()
        #print(self.crane.get_hoist_up())
        #print(self.crane.get_hoist_down())
        time.sleep(3)
        self.crane.stop_hoist()
        print("Hoist done")
        print("Cycle done!")

    def move_with_speed(self):
        """More convenient way than "set_movement_direction".
         Could be run as thread, moving each axis simultaneously. """

        # Trolley
        self.crane.move_trolley_forward_speed(70)
        print("Trolley spd request: ", self.crane.get_trolley_speed_request)
        print("Trolley spd feedback: ", self.crane.get_trolley_speed_feedback)
        print("Trolley spd feedback m/min: ", self.crane.get_trolley_speed_feedback_mmin)
        print("Trolley status: ", self.crane.get_trolley_status)
        time.sleep(2)
        self.crane.stop_trolley()
        time.sleep(1)
        self.crane.move_trolley_backward_speed(70)
        time.sleep(2)
        self.crane.stop_trolley()
        print("Trolley done")

        # Bridge
        self.crane.move_bridge_forward_speed(70)
        print("Bridge spd request: ", self.crane.get_bridge_speed_request)
        print("Bridge spd feedback: ", self.crane.get_bridge_speed_feedback)
        print("Bridge spd feedback m/min: ", self.crane.get_bridge_speed_feedback_mmin)
        print("Bridge status: ", self.crane.get_bridge_status)
        time.sleep(2)
        self.crane.stop_bridge()
        time.sleep(1)
        self.crane.move_bridge_backward_speed(70)
        time.sleep(2)
        self.crane.stop_bridge()
        print("Bridge done")

        # Hoist
        self.crane.move_hoist_down_speed(70)
        print("Hoist spd request: ", self.crane.get_hoist_speed_request)
        print("Hoist spd feedback: ", self.crane.get_hoist_speed_feedback)
        print("Hoist spd feedback m/min: ", self.crane.get_hoist_speed_feedback_mmin)
        print("Hoist status: ", self.crane.get_hoist_status)
        time.sleep(2)
        self.crane.stop_hoist()
        time.sleep(1)
        self.crane.move_hoist_up_speed(70)
        time.sleep(2)
        self.crane.stop_hoist()
        print("Hoist done")

        #self.crane.stop_all()

    def subscribe(self):
        """Not sure what subscribe functions are supposed to do.
        Doesnt work though."""

        t = self.crane.sub_trolley_speed(1000, 5)
        #print(t)

    #Motion profile testing functions!
    def s_curve_testing_combo(self):
        """S-curve test for rectangle track. Used to compare speed against
        old motion profile."""

        s = time.time()
        print("Moving trolley")
        self.crane.set_target_trolley(5000)
        dist_to_target = int(self.crane.trolley_to_target())
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = self.crane.speed_profile_trolley(dist_to_target) # Create speed profile
            while not self.crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command

        time.sleep(3)

        print("Bridge")
        self.crane.set_target_bridge(16000)
        dist_to_target = int(self.crane.bridge_to_target())
        if abs(float(dist_to_target)) > 1:
            speed_profile, remaining_distances = self.crane.speed_profile_bridge(dist_to_target)
            while not self.crane.move_bridge_to_target_s(speed_profile, remaining_distances):
                time.sleep(0.01) # every 10 ms update the velocity command

        time.sleep(3)

        print("Trolley")
        self.crane.set_target_trolley(6000)
        dist_to_target = int(self.crane.trolley_to_target())
        if abs(dist_to_target) > 1:
            speed_profile, remaining_distances = self.crane.speed_profile_trolley(dist_to_target)
            while not self.crane.move_trolley_to_target_s(speed_profile, remaining_distances):
                time.sleep(0.01) # every 10 ms update the velocity command

        time.sleep(3)

        print("Bridge")
        self.crane.set_target_bridge(15000)
        dist_to_target = int(self.crane.bridge_to_target())
        if abs(dist_to_target) > 1:
            speed_profile, remaining_distances = self.crane.speed_profile_bridge(dist_to_target)
            while not self.crane.move_bridge_to_target_s(speed_profile, remaining_distances):
                time.sleep(0.01) # every 10 ms update the velocity command
                
        e = time.time()
        print("Time elapsed: ", round((e-s), 3))
        time.sleep(3)

    def old_testing_combo(self):
        """Old combo does a rectangle of 1 meters using trolley and bridge.
            This code works as comparison against new s-curve.
            Old time is 100.6 seconds."""
        
        print("Starting old testing combo!")
        s = time.time()
        self.crane.set_target_trolley(5000)
        while not self.crane.move_trolley_to_target(): #Move trolley back to starting spot corner 1
            time.sleep(0.01)

        time.sleep(3)

        self.crane.set_target_bridge(16000)
        while not self.crane.move_bridge_to_target(): #Move bridge to corner 4
            time.sleep(0.01)

        time.sleep(3)

        self.crane.set_target_trolley(6000)
        while not self.crane.move_trolley_to_target(): #Move trolley back to starting spot corner 1
            time.sleep(0.01)

        time.sleep(3)

        self.crane.set_target_bridge(15000)
        while not self.crane.move_bridge_to_target(): #Move bridge to corner 4
            time.sleep(0.01)

        e = time.time()
        print("Old time: ", round((e-s), 3))

    def watchdog_test(self):
        """Runs watchdog in same code. Kinda works, but not very good."""
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
        while True:
            watchdog.updateWatchdogLoop()

    def move_trolley(self):
        """Code for threading testing"""
        self.crane.set_target_trolley(5500)
        while not self.crane.move_trolley_to_target():
            time.sleep(1)

        time.sleep(3)

        self.crane.set_target_trolley(6500)
        while not self.crane.move_trolley_to_target():
            time.sleep(1)
        print("Trolley ready!")

    def move_bridge(self):
        """Code for threading testing"""

        self.crane.set_target_bridge(18000)
        while not self.crane.move_bridge_to_target():
            time.sleep(1)

        time.sleep(3)

        self.crane.set_target_bridge(17000)
        while not self.crane.move_bridge_to_target():
            time.sleep(1)
        print("Bridge ready!")


    def s_curve_random(self):
        """Used for demo. Test s-curve movement by taking random point inside cage as target."""

        s = time.time()
        print("Moving trolley")
        target = random.randint(5000, 8000)
        self.crane.set_target_trolley(target)
        dist_to_target = int(self.crane.trolley_to_target())
        if dist_to_target > 1:
            speed_profile, remaining_distances = self.crane.speed_profile_trolley(dist_to_target)
            while not self.crane.move_trolley_to_target_s(speed_profile, remaining_distances):
                time.sleep(0.01) # every 10 ms update the velocity command


        time.sleep(3)
        finish = self.crane.trolley_to_target()
        print("Accuracy: ", abs(target-finish/target))

        print("Bridge")
        self.crane.set_target_bridge(19000)
        dist_to_target = int(self.crane.bridge_to_target())
        if abs(float(dist_to_target)) > 1:
            speed_profile, remaining_distances = self.crane.speed_profile_bridge(dist_to_target)
            while not self.crane.move_bridge_to_target_s(speed_profile, remaining_distances):
                time.sleep(0.01) # every 10 ms update the velocity command

        time.sleep(3)

        print("Trolley")
        self.crane.set_target_trolley(6000)
        dist_to_target = int(self.crane.trolley_to_target())
        if abs(dist_to_target) > 1:
            speed_profile, remaining_distances = self.crane.speed_profile_trolley(dist_to_target)
            while not self.crane.move_trolley_to_target_s(speed_profile, remaining_distances):
                time.sleep(0.01) # every 10 ms update the velocity command

        time.sleep(3)

        print("Bridge")
        self.crane.set_target_bridge(18000)
        dist_to_target = int(self.crane.bridge_to_target())
        if abs(dist_to_target) > 1:
            speed_profile, remaining_distances = self.crane.speed_profile_bridge(dist_to_target)
            while not self.crane.move_bridge_to_target_s(speed_profile, remaining_distances):
                time.sleep(0.01) # every 10 ms update the velocity command
                


def main(): 
    
    # Read access information
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

    # Threading test with watchdog
    def watchdog_test():

        print("Async library in use, watchdog code")
        print("\nInitializing crane connection...\n--Make sure the device is connected to correct WiFi network!--")
        watchdog = Watchdog(url, accesscode)
        print("...crane connection initialized.\n")
        print("Starting watchdog")
        while True:
            watchdog.updateWatchdogLoop()

    

    #threading.Thread(target=watchdog_test).start()
    crane = Crane1(url, accesscode)
    # TESTS
    #crane.connect()
    #crane.watchdog()
    #crane.access()
    #crane.poses()
    #crane.poses_timestamp()
    #crane.speeds_timestamp()
    #crane.set_target()
    #crane.get_load()
    #crane.dist_to_target()
    #crane.move_to_target()
    #crane.move_home()
    #crane.move_to_target_slow()
    #crane.zero_pos()
    #crane.set_movement_direction()
    #crane.move_with_speed()
    #crane.subscribe()

    # Motion profile testing
    crane.s_curve_testing_combo()
    crane.old_testing_combo()
    #crane.s_curve_random()

    # Thread test, move both axes NOT WORKING!
    #crane.move_trolley()
    #threading.Thread(target=move_trolley, args=crane)

    print("Movement done!")



if __name__== "__main__": 
    main()  
