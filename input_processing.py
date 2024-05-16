# input_processing.py
# Thomas Wilson, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# 

import string
from enum import Enum

# No global variables are permitted

# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:
    
    # Initialize variables to default sensor values
    pedestrian_status = False
    vehicle_status = False
    light_status = "green"

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        pass

##  Provide a driver instruction depending on the status of the vehicle, pedestrian and light sensor values.
#   If light is red, or either pedestrian and vehicle are detected, STOP.
#   If light is yellow and no pedestrian or vehicle, Caution.
#   If light is green and no pedestrian or vehicle, Proceed.
    def driver_instruction(self):
        if self.pedestrian_status or self.vehicle_status or (self.light_status == "red"):
            return "STOP"
        elif (self.light_status == "yellow"):
            return "Caution"
        else:
            return "Proceed"

##  Update all status variables and then print the driver insteruction
# Replace these comments with your function commenting
    def update_status(self, pedestrian_status: bool, vehicle_status: bool, light_status: string): # You may decide how to implement the arguments for this function
        self.pedestrian_status = pedestrian_status
        self.light_status = light_status
        self.vehicle_status = vehicle_status
        print()
        print(self.driver_instruction())
        print()

## convert boolean to "yes"/"no" string
def yes_no_string(boolean):
    return "yes" if boolean else "no"

# The sensor object should be passed to this function to print the action message and current status
# For a provided Sensor class, print the light, pedestrian and vehicle status.
def print_message(sensor: Sensor):
    print("Light = " + sensor.light_status + ", Pedestrian = " + yes_no_string(sensor.pedestrian_status) + ", Vehicle = " + yes_no_string(sensor.vehicle_status))

# Ask the user to make a selection from the menu. return as a string
def prompt_user_for_menu_selection():
    print("Are changes detected in the vision input?")
    return input("Select 1 for Light, 2 for Pedestrian, 3 for Vehicle, or 0 to end the program:")

# Ask the yser to make a selection for the sensor value, and return as a string
def prompt_user_for_sensor_value():
    return input("What change has been identified?:")

# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # create instance variables
    quit = False
    sensor = Sensor()
    # Iterate here until user decides to quit.
    # Ask user to select menu option, check their selection, and then depending on selection, ask them to specify sensor value, again checking their choice.
    # After their selection has been made, return the current driver instruction and report the system state, before beginning the next iteration.
    while not quit:
        menu_selection = prompt_user_for_menu_selection()
        try:
            match menu_selection:
                # User has quit
                case "0":
                    quit = True
                    print("Quitting...")
                    continue

                # user wishes to update Light
                case "1":
                    value = prompt_user_for_sensor_value()
                    match value:
                        case "green" | "yellow" | "red":
                            sensor.update_status(sensor.pedestrian_status, sensor.vehicle_status, value)
                        case _:
                            raise ValueError("Unable to parse light status selection, please try again...")

                # user wishes to update pedestrian
                case "2":
                    value = prompt_user_for_sensor_value()
                    match value:
                        case "yes" | "no":
                            sensor.update_status(True if value == "yes" else False, sensor.vehicle_status, sensor.light_status)
                        case _:
                            raise ValueError("Unable to parse pedestrian status selection, please try again...")

                # user wishes to update vehicle
                case "3":
                    value = prompt_user_for_sensor_value()
                    match value:
                        case "yes" | "no":
                            sensor.update_status(sensor.pedestrian_status, True if value == "yes" else False, sensor.light_status)
                        case _:
                            raise ValueError("Unable to parse vehicle status selection, please try again...")
       
                # invalid input
                case _:
                    raise ValueError("Unable to parse menu selection, please try again...")

        # If error was encountered, print it.
        except ValueError as err:
            print()
            print(err)
            print()
            continue
        finally:
            # Show the updated state of the system.
            print_message(sensor)
        


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

