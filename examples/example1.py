import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from crane import Crane

def connect_to_crane():
    url = input("URL: ")
    crane = Crane(url)

    accesscode = int(input("Accescode: "))
    while(not isinstance(accesscode, int)):
        print("Accescode needs to be integer")
        accesscode = int(input("Accescode: "))

    crane.set_accesscode(accesscode)

    return crane

def setTargetCurrentPosition(crane):
    crane.set_target_current_position()

def trolleyToTarget(crane):
    while not crane.move_trolley_to_target():
        print(crane.trolley_to_target())

def main():
    crane = connect_to_crane()
    crane.set_target_trolley(crane.get_motorcontroller_trolley_value() + 50)
    trolleyToTarget(crane)

main()
