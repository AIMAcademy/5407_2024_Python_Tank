#Robotics Practice Driving Robot Controls
#Goals:
#Be able to send and recieve packets from robot
#Control motors settings and output through spark motor controls
#Let inputs from an xbox controler be able to exicute code
#Map specific xbox controler inputs to specific functions
#Make defalt speed setting for motors
#Make slow and fast mode for robot
#Allow for adjustment of motor power for turning based on annolog input
#Todo:
#Download robot connection and control libraries   ///
#Write basic control code      ///
#Write basic xbox input code detection           ///
#Map motor controls to xbox controller inputs        ///
#Set ratio for anolog input to motor side power ratio    ///
#Set ratio for anolog input to overall motor power based on speed mode      ///  
#Decide what default, fast, and slow modes motor power should be        ///
#Write kill switch     ///
#Write code for adjusting turn_ratio value using xbox controller inputs
#ToChange:
#Change button detection to button pressed detection depending on if the button pressed detection checks if the input went from a false value to a true and returns a true value making the button press only return #true when the button goes from not pressed to pressed and not just giving a true value on if it is currently pressed down or the button input is just giving a true.
#Change placeholders with actual values

#imports

import wpilib
import wpilib.drive
import wpilib.interfaces
import wpilib.event
from wpilib.drive import DifferentialDrive

#Ports for inputs add new variables for an appropriate new port.
#Values are currently just placeholders.

left_motor_port = 7 #placeholder
left_motor_port2 = 4
right_motor_port = 5 #placeholder
right_motor_port2 = 1
xbox_controler_port = 0 #placeholder
#Constants:

#Xbox_Joy_Stick_Max is the radius of the joystick range circle; 1 is currently just a placeholder number until I can get the actual radius.

Xbox_Joy_Stick_Max = 1 #dont need radius because the x and y values are interpretted as between 1 and -1 being 100% and -100%

#Turn_Ratio is how much the value x will impact motor speeds, basically the higher the number the higher the ratio is. Current x value / Xbox_Joy_Stick_Max * Turn_Ratio is the equation for
#the x values output which controls the difference in motor speed for turning so effectively the turn ratio makes it so it takes the turn ratios number of x input to match the normal x input.
#The turn ratio is currently a placeholder.

Turn_Ratio = 1 
#The robot class which is what will execute functions and store values for the robot to use.

class robot(wpilib.TimedRobot):
#RobotInit function initializes the robot and only runs on the start up of the robot, basically storing the objects variables.

    def robotInit(self):

#Motors can be listed here, for any new motors make sure to add them to the appropriate motor group side

        self.left_motor = wpilib.Spark(left_motor_port)
        self.right_motor = wpilib.Spark(right_motor_port)
        self.left_motor2 = wpilib.Spark(left_motor_port2)
        self.right_motor2 = wpilib.Spark(right_motor_port2)
        self.left_motor_group = wpilib.MotorControllerGroup(self.left_motor, self.left_motor2)
        self.right_motor_group = wpilib.MotorControllerGroup(self.right_motor, self.right_motor2)

#self.drive controls the motor groups through the differentialDrive function 

        self.drive = DifferentialDrive(self.left_motor_group, self.right_motor_group)

#self.Speed_Mode is a list of multiples for the motor speed allowing for adjustments in overall #motor power output. 1 = 100% of calculated output 0.75 = 75% of calculated output 0.25 = 25% of calculated output

        self.Speed_Mode = [1,0.75,0.5,0.25,0]

#self.SPV is the Speed_Mode selection variable it tells the speed_mode list the index to return.    
#SPV value meanings: Fast Mode = 0, Normal Mode = 1, Slow Mode = 2.

        self.SPV = 0

#self.controler is the xbox controller in the given xbox controller port and is used for asking for specific button inputs of the specified controller in the listed port.

        self.controler = wpilib.XboxController(xbox_controler_port)

#Input variables to be called when used.

        self.Xbox_A_Button = wpilib.XboxController.getAButton(self.controler)
        self.Xbox_B_Button = wpilib.XboxController.getBButton(self.controler)
        self.Xbox_X_Button = wpilib.XboxController.getXButton(self.controler)
        self.Xbox_Y_Button = wpilib.XboxController.getYButton(self.controler)
        self.Xbox_Start_Button = wpilib.XboxController.getStartButton(self.controler)
        self.Xbox_Joy_Stick = wpilib.XboxController(xbox_controler_port)
        self.Xbox_Left_Trigger = wpilib.XboxController.getLeftBumper(self.controler)
        self.Xbox_Right_Trigger = wpilib.XboxController.getRightBumper(self.controler)


    def teleopExit(self):

#self.drive.stopMotor stops the motor using the self.drive which has the value of the previously stored DifferentialDrive function.

        self.drive.stopMotor()

#teleopPeriodic runs 50 times a second.

    def teleopPeriodic(self):

#The if statement checks to see if the self,Xbox_Left_Trigger is true which means its been pressed and if self.SPV > 0 so that it doesn't get a value of -1 which can't be an index on the self.Speed_Mode list.
            #if self.Xbox_Left_Trigger == True and self.SPV > 0:

#self.SPV -= 1 or self.SPV = self.SPV - 1.

                #self.SPV -= 1

#The if statement checks to see if the self.Xbox_Right_Trigger is true which means the right trigger has been pressed and if self.SPV < 2 which stops self.SPV from having a value greater than 2 because it would not
#be an index on the self.Speed_Module list.

            #if self.Xbox_Right_Trigger == True and self.SPV < len(self.Speed_Mode)-1:

#self.SPV += 1 or self.SPV = self.SPV + 1.
                #self.SPV +=1

#self.drive.tankDrive is a function that when given a DifferentialDrive function which is what self.drive's value is tied to with motor control groups attched will set the motors output to the % input corresponding #to the left and right sides. There is also an inverse thing future but I didn't use that.

            self.drive.tankDrive(

#The inputs can be explained as the selected speed mode with the SPV variable multiplied by the result of the joystick y value/ radius of the joysticks range + or - (left and right) joystick x value/ radius of #joysticks range * the selected turn speed ratio or more simply the speed mode * ( y value % of max + or - x value % of max * the turn ratio). This equation results in an appropriate motor power % value in the form #of 1 as 100% and -1 as -100% .

                self.Speed_Mode[self.SPV] * ((self.Xbox_Joy_Stick.getLeftY/Xbox_Joy_Stick_Max) + (self.Xbox_Joy_Stick.getLeftX/Xbox_Joy_Stick_Max * Turn_Ratio)),
                self.Speed_Mode[self.SPV] * ((self.Xbox_Joy_Stick.getLeftY/Xbox_Joy_Stick_Max) - (self.Xbox_Joy_Stick.getLeftX/Xbox_Joy_Stick_Max * Turn_Ratio)))

#when the computer runs the code looks at the code bellow and only runs that

if __name__ == "__main__":


#runs the robot class code as the object robot.

    wpilib.run(robot)

