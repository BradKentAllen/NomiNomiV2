# config_boat.py

'''
Fixed parameters set for boat

'''

# Rev 0.0.2  NomiNomi initial dev


#### Navigation and Course Correction factors
COURSE_TOLERANCE = 5  # helm corrects when beyond +/-
DISTANCE_TO_START = 30  # feet boat sails before navigation begins

#### boat parameters
RUDDER_ANGLE_MAX = 35  # physical limitation of boat or desired max, not servo
SERVO_ANGLE_MAX = 90  # corresponds to servo angle at 1 or -1
RUDDER_ROLL_SWITCH = 15 # angle at which only one rudder operates
RUDDER_PORT_DIR = True  # True if rudder is to port when servo is 1
RUDDER_STARBOARD_DIR = True  # True if rudder is to port when servo is 1


PORT_ROLL_POSITVE = True   # roll to port is positive number
ROLL_ANGLE_TARGET = 10  # sheet in under this
ROLL_ANGLE_MAX = 45  # take urgent action to correct over this

IRONS_ANGLE = 1 # this angle or less including A0 will be treated as irons
CLOSE_ANGLE = 2  # will target P2 or S2 for close reach
RUN_ANGLE = 6  # this angle or greater, including Z8,  will be a straight run

SAIL_SERVO_PULSE_MIN = 1000
SAIL_SERVO_PULSE_MAX = 2400

# Compass adjusters are subtracted from reading to get true bearing
# e.g. declination of 11 means true North is at 349 degrees
COMPASS_DECLINATION = 15  # nature of the area
COMPASS_OFFSET = 0  # calibration value for magnemometer