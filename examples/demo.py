import pygame as pg
import thorpy as tp 
import sys
from pygame.locals import *

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from new_crane import Crane

def connect_to_crane(): 
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

    crane = Crane(url)
    crane.set_accesscode(accesscode)
    print("Crane connection initialized!")
    return crane

def crane_to_target_demo(crane):        #Moving the bridge, trolley and hoist according to the pre-defined demo route
        print("Crane moving!")
        crane.set_target_bridge(18000)  #Move bridge to starting point 1
        dist_to_target = abs(int(crane.bridge_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = crane.speed_profile_bridge(dist_to_target) # Create speed profile
            while not crane.move_bridge_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)

        crane.set_target_trolley(8525)  #Move trolley to starting spot point 1
        dist_to_target = abs(int(crane.trolley_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = crane.speed_profile_trolley(dist_to_target) # Create speed profile
            while not crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        print("Crane at starting point")

        crane.set_target_bridge(15250)  #Move bridge to corner 2 
        dist_to_target = abs(int(crane.bridge_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = crane.speed_profile_bridge(dist_to_target) # Create speed profile
            while not crane.move_bridge_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        print("Crane at corner 2")

        crane.set_target_trolley(4600)  #Move trolley to corner 3 
        dist_to_target = abs(int(crane.trolley_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = crane.speed_profile_trolley(dist_to_target) # Create speed profile
            while not crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        print("Crane at corner 3")

        crane.set_target_hoist(2200)    #Lower the hoist at corner 3
        while not crane.move_hoist_to_target(): 
            time.sleep(1)
        print("Hoist lowered")

        crane.set_target_hoist(3060)    #Raise the hoist at corner 3
        while not crane.move_hoist_to_target(): 
            time.sleep(1)
        print("Hoist back up")

        crane.set_target_bridge(18000)  #Move bridge to corner 4
        dist_to_target = abs(int(crane.bridge_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = crane.speed_profile_bridge(dist_to_target) # Create speed profile
            while not crane.move_bridge_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)
        print("Crane at corner 4")

        crane.set_target_trolley(8525)  #Move trolley back to starting spot corner 1
        dist_to_target = abs(int(crane.trolley_to_target()))
        if dist_to_target > 1: # If distance to target more than 1 mm
            speed_profile, remaining_distances = crane.speed_profile_trolley(dist_to_target) # Create speed profile
            while not crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                time.sleep(0.01) # every 10 ms update the velocity command
        time.sleep(3)

        print("Crane at starting point")
        print("Demo 1 finished")

def crane_to_target_user_given_route(crane):       #Moving the bridge, trolley and hoist according to the user input
    print("Starting crane movement according to user given route input.")
    toggable_value = toggable.get_value()
    for value in crane_values: 
        if value < 10000: 
            crane.set_target_trolley(value)
            dist_to_target = abs(int(crane.trolley_to_target()))
            if dist_to_target > 1: # If distance to target more than 1 mm
                speed_profile, remaining_distances = crane.speed_profile_trolley(dist_to_target) # Create speed profile
                while not crane.move_trolley_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                    time.sleep(0.01) # every 10 ms update the velocity command
            time.sleep(3)

            if toggable_value == 'At every check point':        # User input from toggable 
                crane.set_target_hoist(2200)                    # Lower the hoist                   
                while not crane.move_hoist_to_target():
                    time.sleep(1)
                crane.set_target_hoist(3060)                    # Raise the hoist                   
                while not crane.move_hoist_to_target():
                    time.sleep(1)
        else: 
            crane.set_target_bridge(value)                      # Move bridge to target
            dist_to_target = abs(int(crane.bridge_to_target()))
            if dist_to_target > 1:                              # If distance to target more than 1 mm
                speed_profile, remaining_distances = crane.speed_profile_bridge(dist_to_target) # Create speed profile
                while not crane.move_bridge_to_target_s(speed_profile, remaining_distances): # Use speed profile to move
                    time.sleep(0.01)                            # every 10 ms update the velocity command
        time.sleep(3)

    if toggable_value == 'Only at the end': 
        crane.set_target_hoist(2200)                            # Move hoist down 
        while not crane.move_hoist_to_target():
            time.sleep(1)
        crane.set_target_hoist(3060)                            # Move hoist back up 
        while not crane.move_hoist_to_target():
            time.sleep(1)

    elif toggable_value == 'Never':                    
            pass
        
    print("Demo finished!")
    crane_values.clear()

def refresh_window(screen, bck):        # Handles the background of the GUI 
    screen.blit(bck, (0,0))


def start_button_at_unclick(): 
    global start_true
    start_true = True 
    global demo_on
    global screen
    global bck
    #pg.quit()
    print("Start button pressed")
    print("Crane values in user given order:")
    print(*crane_values)
    text5 = tp.Text("CRANE MOVING")
    skyblue = (135, 206, 235)
    text5.set_font_color(skyblue)
    text5.set_font_size(44)
    group5 = tp.Group([text5])
    updater5 = group5.get_updater()
    screen_colour = (255,255,255)
    screen.fill(screen_colour)
    events = pg.event.get()
    mouse_rel = pg.mouse.get_rel()
    updater5.update(events=events, mouse_rel=mouse_rel)
    pg.display.update()
    crane = connect_to_crane()                     # *** UNCOMMENT WHEN RUNNING WITH THE CRANE *** (see also rows 572 & 573)
    crane_to_target_user_given_route(crane)        # *** UNCOMMENT WHEN RUNNING WITH THE CRANE *** (see also rows 572 & 573)

def quit_button_at_unclick(): 
    pg.quit()
    sys.exit()

def mode_button_at_unclick(): 
    global screen
    global bck
    refresh_window(screen, bck)
    global choice0
    choice0.launch_alone()

def erase_button_at_unlick(): 
    global top_values
    global left_values
    global crane_values
    top_values = []
    left_values = []
    crane_values = []


def drawing_rect():                                     # Function for mapping the clicks of the user in the grid (not working)
    numbers = []
    for n in range(1, 100): 
        numbers.append(n)
    blue = (0,0,128)                                    # Background colour of the number and colour of the square 
    white = (255,255,255)                               # Colour of the number 
    font = pg.font.Font('freesansbold.ttf', 25)         # Assigning the name and size of the font 
    a = 0                                               # Variable used for iterating the numbers 
    for l in range(len(top_values)): 
        pg.draw.rect(screen, blue, pg.Rect(top_values[l], left_values[l], 81, 75))
        number = str(numbers[a])
        text = font.render(number, True, white, blue)
        textRect = text.get_rect()
        textRect.center = (top_values[l] + 40, left_values[l] + 37)
        screen.blit(text, textRect)
        a = a + 1
    pg.display.update()

def main(): 
    # *** Initlializing the pygame window ***
    pg.init()

    # *** Building the infrastructure of the window ***
    global screen
    screen = pg.display.set_mode((1100, 550), pg.RESIZABLE)
    global bck
    bck = pg.image.load('crane.jpg')
    bck = pg.transform.smoothscale(bck, screen.get_size())

    # *** Setting up the default style ***
    tp.set_default_font(("arialrounded", "arial", "calibri", "century"), font_size=20)
    tp.init(screen, tp.theme_round2) # *** Binding screen to gui elements and setting the theme ***

    tp.call_before_gui(refresh_window(screen, bck))

    font_colour = (0,0,0)

    # *** Declaring the UI elements ***
    title0 = ""
    message0 = "Choose the mode"
    global choice0
    choice0 = tp.AlertWithChoices(title0, ("AUTO", "MANUAL"), message0)
    title = "AUTO MODE"
    message = "What do you want to do?"
    choice1 = tp.AlertWithChoices(title, ("START", "QUIT"), message)
    text4 = tp.Text("Choose the route for the \ncrane by clicking the grid.")
    text4.set_font_color(font_colour)
    text5 = tp.Text("MANUAL")
    text3 = tp.Text("Start the demo by clicking START!")
    text3.set_font_color(font_colour)
    button3 = tp.Button("START")
    text8 = tp.Text("Stop the demo by clicking QUIT")
    text8.set_font_color(font_colour)
    button8 = tp.Button("QUIT")
    text6 = tp.Text("Change the mode by clicking below")
    text6.set_font_color(font_colour)
    button6 = tp.Button("CHOOSE MODE")
    text9 = tp.Text("Erase all checkpoints")
    text9.set_font_color(font_colour)
    button9 = tp.Button("ERASE")

    global toggable
    text_toggable = tp.Text("When do you want the \nhook to be lowered?")
    text_toggable.set_font_color(font_colour)
    toggable = tp.TogglablesPool('', ['Never', 'Only at the end', 'At every check point'], 'Never', 'checkbox')
    toggable.set_font_color((235,85,128), states=['normal', 'pressed', 'locked'], apply_to_children=True)
    toggable.set_font_color((0,0,0), states='hover', apply_to_children=True)
    toggable.set_bck_color((240,240,240), apply_to_children=True)
    

    # *** Grouping UI elements ***
    group2 = tp.Group([text5])
    group2.set_topleft(0,0)
    group3 = tp.Group([text4])
    group3.set_topleft(300, 0)
    updater3 = group3.get_updater()
    updater2 = group2.get_updater()
    group4 = tp.Group([text3, button3, text9, button9, text_toggable, toggable, text6, button6, text8, button8])
    group4.sort_children("v")
    group4.set_topleft(700, 5)
    updater4 = group4.get_updater()

    global demo_on
    demo_on = False
    screen_color = (255,255,255)

    # *** Lists for storing the values for moving the crane *** 
    global bridge_values
    global trolley_values
    global crane_values
    global left_values
    global top_values
    bridge_values = []      #User input values stored for the bridge (not used)
    trolley_values = []     #User input values stored for the trolley (not used)
    crane_values = []       #User input values stored for both the bridge and the trolley, used for moving the crane in correct order 
    top_values = []         #User input values used for tracking the clicks of the user 
    left_values = []        #User input values used for tacking the clicks of the user 
    
    # *** Variables for clicks
    global route_ok
    global start_true
    route_ok = False
    start_true = False

    while True: 
        button3.at_unclick = start_button_at_unclick
        button8.at_unclick = quit_button_at_unclick
        button6.at_unclick = mode_button_at_unclick
        button9.at_unclick = erase_button_at_unlick
        events = pg.event.get()
        mouse_rel = pg.mouse.get_rel()
        if demo_on == False: 
            choice0.launch_alone()
        for event in events: 
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos() #Storing the poisition of the user input

                if 0 <= x <= 650 and 75 <= y <= 525: 
                    print("x: " + str(x) + " y: " + str(y))
                    # *** Determing in which square the click is and appending predefined values 
                    # to the crane_values list to be used when moving the crane via OPC UA ***
                    if 0 <= x <= 81: 
                        print("Bridge -> 1")
                        bridge_values.append(20394)
                        crane_values.append(20394)
                        top_values.append(0)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    elif 82 <= x <= 162: 
                        print("Bridge -> 2")
                        bridge_values.append(19582)
                        crane_values.append(19582)
                        top_values.append(81)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    elif 163 <= x <= 243: 
                        print("Bridge -> 3")
                        bridge_values.append(18770)
                        crane_values.append(18770)
                        top_values.append(162)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    elif 244 <= x <= 324:
                        print("Bridge -> 4")
                        bridge_values.append(17953)
                        crane_values.append(17953)
                        top_values.append(243)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    elif 325 <= x <= 405:
                        print("Bridge -> 5")
                        bridge_values.append(17146)
                        crane_values.append(17146)
                        top_values.append(324)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    elif 406 <= x <= 486:
                        print("Bridge -> 6")
                        bridge_values.append(16334)
                        crane_values.append(16334)
                        top_values.append(405)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    elif 487 <= x <= 567:
                        print("Bridge -> 7")
                        bridge_values.append(15522)
                        crane_values.append(15522)
                        top_values.append(486)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    elif 568 <= x <= 650: 
                        print("Bridge -> 8")
                        bridge_values.append(14708)
                        crane_values.append(14708)
                        top_values.append(567)
                        if 75 <= y <= 150: 
                            print("Hoist -> A")
                            trolley_values.append(8817)
                            crane_values.append(8817)
                            left_values.append(75)
                        elif 151 <= y <= 225: 
                            print("Hoist -> B")
                            trolley_values.append(8051)
                            crane_values.append(8051)
                            left_values.append(150)
                        elif 226 <= y <= 300: 
                            print("Hoist -> C")
                            trolley_values.append(7285)
                            crane_values.append(7285)
                            left_values.append(225)
                        elif 301 <= y <= 375: 
                            print("Hoist -> D")
                            trolley_values.append(6519)
                            crane_values.append(6519)
                            left_values.append(300)
                        elif 376 <= y <= 450: 
                            print("Hoist -> E")
                            trolley_values.append(5753)
                            crane_values.append(5753)
                            left_values.append(375)
                        elif 451 <= y <= 525: 
                            print("Hoist -> F")
                            trolley_values.append(4985)
                            crane_values.append(4985)
                            left_values.append(450)
                    

        if choice0.get_value() == "AUTO": 
            refresh_window(screen, bck)
            choice1.launch_alone()
            if choice1.get_value() == "START": 
                demo_on = True
                refresh_window(screen, bck)
                print("Starting crane initialization!")

                # *** Creating the window shown when the crane is moving ***
                text7 = tp.Text("CRANE MOVING")
                skyblue = (135, 206, 235)
                text7.set_font_color(skyblue)
                text7.set_font_size(44)
                group7 = tp.Group([text7])
                updater7 = group7.get_updater()
                screen_colour = (255,255,255)
                screen.fill(screen_colour)
                events = pg.event.get()
                mouse_rel = pg.mouse.get_rel()
                updater7.update(events=events, mouse_rel=mouse_rel)
                pg.display.update()

                crane = connect_to_crane()             # *** UNCOMMENT WHEN RUNNING WITH THE CRANE *** (see also rows 121 & 122)
                crane_to_target_demo(crane)            # *** UNCOMMENT WHEN RUNNING WITH THE CRANE *** (see also rows 121 & 122)

                refresh_window(screen, bck)
                demo_on = False

            elif choice1.get_value() == "QUIT":
                pg.quit()
                sys.exit()
                
        elif choice0.get_value() == "MANUAL": 
            demo_on = True
            refresh_window(screen, bck)
            screen.fill(screen_color)
            updater2.update(events=events, mouse_rel=mouse_rel)
            updater3.update(events=events, mouse_rel=mouse_rel)
            updater4.update(events=events, mouse_rel=mouse_rel)

            # ***Variables for drawing lines ***
            line_color = (162,162,162)
            width = 650

            # *** drawing vertical lines for the grid ***
            pg.draw.line(screen, line_color, (0, 75), (0, 525), 7)
            pg.draw.line(screen, line_color, (width / 8, 75), (width / 8, 525), 3)
            pg.draw.line(screen, line_color, (width / 8 * 2, 75),(width / 8 * 2, 525), 3)
            pg.draw.line(screen, line_color, (width / 8 * 3, 75),(width / 8 * 3, 525), 3)
            pg.draw.line(screen, line_color, (width / 8 * 4, 75),(width / 8 * 4, 525), 3)
            pg.draw.line(screen, line_color, (width / 8 * 5, 75),(width / 8 * 5, 525), 3)
            pg.draw.line(screen, line_color, (width / 8 * 6, 75),(width / 8 * 6, 525), 3)
            pg.draw.line(screen, line_color, (width / 8 * 7, 75),(width / 8 * 7, 525), 3)
            pg.draw.line(screen, line_color, (width, 75), (width, 525), 7)

            # *** drawing horizontal lines for the grid ***
            pg.draw.line(screen, line_color, (0, 75), (width, 75), 7)  
            pg.draw.line(screen, line_color, (0, 75 + 75), (width, 75 + 75), 3)
            pg.draw.line(screen, line_color, (0, 75 + (2*75)),(width, 75 + (2*75)), 3)
            pg.draw.line(screen, line_color, (0, 75 + (3*75)),(width, 75 + (3*75)), 3)
            pg.draw.line(screen, line_color, (0, 75 + (4*75)),(width, 75 + (4*75)), 3)
            pg.draw.line(screen, line_color, (0, 75 + (5*75)),(width, 75 + (5*75)), 3)
            pg.draw.line(screen, line_color, (0, 75 + (6*75)),(width, 75 + (6*75)), 7)
            #print("In manual mode!")

            drawing_rect()      #Calling drawing rect function for mapping the user clicks in the grid


        pg.display.flip()

main()