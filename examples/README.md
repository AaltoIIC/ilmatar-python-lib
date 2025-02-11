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

This is example program that creates crane object and moves trolley for 50 mm and prints trolleys distance to target until it achieves it and then stops trolley.

## Running
Watchdog can be started from repository's root directory with command:  
`python3 examples/watchdog.py`  
Demo can be started from repository's root directory with command:  
`python3 examples/example1.py`  

## Creating crane object
First Crane class needs to be imported from the crane.py file.  
```
from new_crane import Crane
```
The Crane object needs to be initialized by giving it the url for the cranes opcua. To be able to set values to the cranes opcua the accesscode needs to be given. These values are read from a text file called accesscode_url.txt.  
```
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
```
After the values have been successfully read from the file they are set and the crane object is created. 
```
crane = Crane1(url, accesscode)
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
* move_bridge_to_target_s 

these use different ways to ramp the speed of the crane

```
while not crane.move_trolley_to_target():
  pass

```
while not crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
  pass

``` 
The speed profile is created by: 

``` 
speed_profile, remaining_distances = crane.speed_profile_trolley(dist_to_target)

```
``` 

# Example2

This is an example program that moves the trolley in a square formation and lowers and brings the hoist in one corner before resuming movement to the start position. The cran eobject and movement is otherwise identital as in example1. See example1 for further information. 

## Running
Watchdog can be started from repository's root directory with command:  
`python3 examples/watchdog.py`  
Demo can be started from repository's root directory with command:  
`python3 examples/example2.py` 


# Demo

This is a program that has a graphical interface for controlling the cranes movement. To run this program the following libraries need to be installed: pygame and thorpy. These libraries can be installed with the command:
* 'pip install pygame' and 'pip install thorpy'.   


## Running
Watchdog can be started from repository's root directory with command:  
`python3 examples/watchdog.py`  
Demo can be started from repository's root directory with command:  
`python3 examples/demo.py` 

## Connect_to_crane function 
In this function the connection to the crane is secured. First the Crane class needs to be imported from the crane.py file.  
```
from new_crane import Crane
```
The Crane object needs to be initialized by giving it the url for cranes opcua. To be able to set values to cranes opcua, the accesscode needs to be given. This is done by reading the url and the accesscode from the accesscode_url.txt file. 
```
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
```
After reading the url and the accesscode from the text file these values are set and the crane object is returned. 
```
crane = Crane(url)
crane.set_accesscode(accesscode)
print("Crane connection initialized!")
return crane
```

## Main function 
The pygame window, its infrastructure, style and all of the UI elements are created. Some variables are created that are used in the functions. The while loop takes care of the user input handling. 

## Drawing_rect function 
This function is used for mapping the users click on the grpahical grid that represents the cranes allowed area of movement. 

## xx_at_unclick function
The four unclick functions are used for handling the users input from clicking the elements in the graphical window. 

## Crane_to_targeet_user_given_route function 
This function is used to move the crane according to the user given input. The user clicks the grid to indicate what route they want the crane to take and set is they want the hoist to be lowered at every check point, at the end or not at all. 

## Crane_to_target_demo function 
This function moves the crane in a predetermined fashion. The movement pattern is identical to that of example2. More information about it can be found from [Example2] (#Example2)



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
