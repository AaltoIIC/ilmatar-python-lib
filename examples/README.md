Table of contents
====
* [Table of contents](#table-of-contents)
* [Example1](#example1)
  * [Running](#running)
  * [Creating crane object](#creating-crane-object)
  * [Setting crane's target](#setting-cranes-target)
  * [Distance to target](#distance-to-target)
  * [Moving to target](#moving-to-target)
* [Watchdog](#watchdog)

# Example1

This is example program that creates crane object and moves trolley for 30 mm and prints trolleys distance to target until it achieves it and then stops trolley.

## Running
Watchdog can be started from repository's root directory with command:  
`python3 examples/watchdog.py`  
Demo can be started from repository's root directory with command:  
`python3 examples/example1.py`  

## Creating crane object
First Crane class needs to be imported from the crane.py file.  
```
from crane import Crane
```
Crane object needs to be initialized by giving it url for cranes opcua  
```
url = input("URL: ")
crane = Crane(url)
```
To be able to set values to cranes opcua accescode needs to be given
```
accesscode = int(input("Accescode: "))
crane.set_accesscode(accesscode)
```
Function for creating crane object
```
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
```
## Cranes current location
Cranes current location can be get with following functions:
* get_motorcontroller_trolley_value
* get_motorcontroller_bridge_value
* get_motorcontroller_hoist_value

## Setting crane's target
Cranes current position can be saved by:  
```
crane.set_target_current_position()
```
or target position can be given as parameter for following functions:  
* set_target_bridge
* set_target_trolley
* set_target_hoist

and it can be set to be 50mm from current location by
```
crane.set_target_trolley(crane.get_motorcontroller_trolley_value() + 50)
```

## Distance to target
Distance to target can be get with following functions:
* bridge_to_target
* trolley_to_target
* hoist_to_target

## Moving to target
crane can be moved back to target location with following functions:
* move_trolley_to_target
* move_bridge_to_target
* move_hoist_to_target_precise

```
while not crane.move_trolley_to_target():
  pass
```

# Watchdog
To be able to control crane watchdog needs to be updated constantly.  
This can be done in different process than process where crane is controlled.  
Premade watchdog class can be found from file [watchdog.py](/watchdog.py).  

First crane object must be created and accescode for crane must be set. Tutorial for this can be found from [Creating crane object](#creating-crane-object).  
After that watchdog can be updated by calling function `increment_watchdog`.
```
import time

def updateWatchdogLoop(self):
      while self.setAccesscode():
          self.crane.increment_watchdog()
          time.sleep(0.1)
          print("Incremented")
```
