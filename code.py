from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ============================================================
# FLL BIOGLOW — Shared Robot Base Program (robot.py)
# ============================================================
# WHAT THIS IS
# ------------
# The ONE program every team starts from. It handles all the
# boring-but-essential setup — motors, the drive base, the gyro,
# and the run menu — so your only real job is to write mission
# code inside the run_1(), run_2(), ... functions near the bottom.
#
# HOW TO USE IT
# -------------
# 1. Open this file in Pybricks Code (https://code.pybricks.com)
#    with Pybricks firmware already installed on your hub.
# 2. Edit the "ROBOT CONFIG" section to match YOUR chassis
#    (motor ports, wheel size, sensor ports).
# 3. Write mission code inside run_1(), run_2(), etc.
# 4. Add each run to the RUNS list so it shows up in the menu.
# 5. At the hub: LEFT / RIGHT buttons pick a run, CENTER launches it.
#    When a run finishes, the menu jumps to the NEXT run automatically
#    — so at the table you just tap CENTER, swap attachments, tap again.
#
# HOW TO ADD A NEW RUN (the workflow your team repeats all season)
# ----------------------------------------------------------------
# def run_4():
#     drive.straight(400)
#     drive.turn(90)
#     ...then add ("4", run_4) to the RUNS list below.
# ============================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# ============================================================
# ROBOT CONFIG — *** CHANGE THESE TO MATCH YOUR ROBOT ***
# ============================================================
hub = PrimeHub()

# --- Drive motors ---------------------------------------------------
# Use the ports your motors are plugged into. If a wheel spins the
# WRONG way, flip its Direction between CLOCKWISE and COUNTERCLOCKWISE.
left_motor = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, positive_direction=Direction.CLOCKWISE)

# --- Attachment motors (optional) -----------------------------------
# Delete these lines if you aren't using attachment motors yet.
left_arm = Motor(Port.B)
right_arm = Motor(Port.A)

# --- Chassis measurements (in MILLIMETERS) --------------------------
# WHEEL_DIAMETER: measure a drive wheel (tire included) across the middle.
# AXLE_TRACK: distance between the centers of the two drive wheels.
# Getting these right is what makes straight() and turn() accurate.
WHEEL_DIAMETER = 55  # tire 32019 (62.4 x 20) on rim 86652 — measure to confirm
AXLE_TRACK = 99   # *** MEASURE YOURS and update this ***

# ============================================================
# DRIVE BASE — the thing that drives accurately
# ============================================================
drive = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

# Turn the gyro ON. This is the whole reason we're on Pybricks:
# straight lines stay straight and turns actually hit their angle.
drive.use_gyro(True)

# Movement settings. Keep speeds LOW while testing so crashes are1
# gentle; raise them once your runs are reliable.
# straight_speed = mm/s, turn_rate = degrees/s
drive.settings(
    straight_speed=900,
    straight_acceleration=300,
    turn_rate=600,
    turn_acceleration=400,
)

# ============================================================
# STARTUP — calibrate the gyro before doing anything
# ============================================================
def calibrate_gyro():
    """Hold the robot STILL until the gyro is ready, then zero it.
    The display shows '-' while you must keep it still; a beep means
    the gyro is calibrated and you can pick the robot up."""
    hub.display.char("-")
    while not hub.imu.ready():
        wait(50)
    while not hub.imu.stationary():
        wait(50)
    hub.imu.reset_heading(0)
    hub.speaker.beep()

# ============================================================
# HELPER FUNCTIONS — reusable moves your runs can call
# ============================================================
def square_to_wall(speed=200, seconds=1.0):
    """Drive backward into a wall to reset the robot's position.
    Open-loop on purpose: pushing flat against the wall straightens
    the robot. Use it as the first move of a run to fix alignment.
    NOTE: motor speed here is in degrees/second (not mm/s)."""
    seconds = 1.0
    drive.stop()
    left_motor.run(-speed)
    right_motor.run(-speed)
    wait(int(seconds * 1000))
    left_motor.brake()
    right_motor.brake()
    drive.reset()  # forget the wall-push so odometry stays clean


def drive_until_line(sensor, speed=150, darkness=20):
    """Drive forward until a color sensor sees a dark line.
    'darkness' is a reflection threshold (0 = black ... 100 = white)."""
    drive.reset()
    while sensor.reflection() > darkness:
        drive.drive(speed, 0)  # speed mm/s, 0 deg/s turn = go straight
        wait(5)
    drive.stop()


def beep_done():
    """Quick double-beep so the driver knows a run finished."""
    hub.speaker.beep(1000, 100)
    hub.speaker.beep(1500, 100)

# ============================================================
# MISSION RUNS — *** THIS IS WHERE YOUR TEAM WRITES CODE ***
# ============================================================
# Each run is one trip out from base and back. Keep them short and
# reliable. Call the helpers above whenever they save you work.

def run_1():
    drive.settings
    straight_speed=11000,
    straight_acceleration=600,
    turn_rate=600,
    turn_acceleration=400,
    seconds = 1.0
    calibrate_gyro()
    index = 0
    drive.straight(220)
    drive.turn(-75)
    drive.straight(250)
    drive.turn(33)
    drive.straight(170)
    right_arm.run_angle(90,100)
    drive.turn(-30)
    drive.straight(90)
    right_arm.run_angle(90,-24)
    wait(int(seconds * 15))
    drive.straight(-180)
    right_arm.run_angle(90,73)
    drive.turn(30)
    drive.straight(60)
    drive.turn(-32)
    drive.straight(120)
    left_arm.run_angle(90,-100)


   
    

    



def run_2():
    drive.straight(500)
    left_arm.run_angle(500, 180)  # spin attachment motor 180 deg at 500 deg/s
    drive.straight(-500)


def run_3():
    # Empty for now — your team fills this one in.
    pass

# ============================================================
# RUN MENU — add each run here so it shows up on the hub
# ============================================================
# Format: ("label shown on hub", function_to_run)
RUNS = [
    ("1", run_1),
    ("2", run_2),
    ("3", run_3),
]

# ============================================================
# MENU ENGINE — you usually won't need to touch below here
# ============================================================
def wait_for_button():
    """Wait for one clean button press and return which button(s)."""
    while hub.buttons.pressed():  # let any old press clear first
        wait(10)
    while True:
        pressed = hub.buttons.pressed()
        if pressed:
            buttons = pressed                # remember what was pressed
            while hub.buttons.pressed():     # wait for release (debounce)
                wait(10)
            return buttons
        wait(10)


def main():
    drive.settings
    straight_speed=11000,
    straight_acceleration=600,
    turn_rate=600,
    turn_acceleration=400,
    seconds = 1.0
    calibrate_gyro()
    index = 0
    left_arm.run_angle(140,400)
    wait(int(seconds * 3))
    left_arm.run_angle(140,-300)
    drive.straight(540)
    drive.turn(-12)
    right_arm.run_angle(90,60)
    drive.straight(79)
    right_arm.run_angle(90,200)
    wait(int(seconds * 3))
    drive.straight(-97)
    drive.turn(-44)
    drive.straight(393)
    drive.turn(90)
    drive.straight(60)
    drive.straight(135)
    drive.straight(90)
    drive.straight(-127)
    drive.turn(108)
    drive.straight(220)
    drive.straight(-100)
    drive.turn(-56)
    drive.straight(103)
    left_arm.run_angle(90,300)
    drive.turn(15)
    left_arm.run_angle(-90,260)
    drive.turn(-10)
    drive.straight(118)
    drive.turn(20)
    
    drive.turn(20)
    wait(int(seconds * 2))
    wait(int(seconds * 2))
    drive.turn(20)
    drive.turn(20)
    drive.straight(750)


   

    

    


    


    """while True:
        # Show the selected run's label on the hub display
        hub.display.char(RUNS[index][0])
        buttons = wait_for_button()

        if Button.LEFT in buttons:
            index = (index - 1) % len(RUNS)  # scroll to previous run
        elif Button.RIGHT in buttons:
            index = (index + 1) % len(RUNS)  # scroll to next run
        elif Button.CENTER in buttons:
            label, run_function = RUNS[index]
            run_function()                   # <-- run the mission
            drive.stop()
            beep_done()
            index = (index + 1) % len(RUNS)  # auto-advance to next run"""


# Start the program
run_1()