#2024 Winter Compatition Robot

#imports
import rev
import wpilib
import wpilib.drive
import wpilib.interfaces
import wpilib.event
from wpilib.drive import DifferentialDrive
from wpilib.shuffleboard import Shuffleboard

#ports
#placeholder = 1
DriveLeftMotorPort1 = 23
DriveLeftMotorPort2 = 22
DriveRightMotorPort1 = 20
DriveRightMotorPort2 = 21
PickupMechansimMotorPort = 1
#PickupAndFiringArmMotorPort = placeholder
ShootingMechansimMotorPort1 = 2
ShootingMechansimMotorPort2 = 3
XboxControlerPort = 0
class robot(wpilib.TimedRobot):
    def robotInit(self):

#Motors + WPILIB drive
        self.DriveLeftMotor = rev.CANSparkMax(DriveLeftMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushed)
        self.DriveRightMotor = rev.CANSparkMax(DriveRightMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushed)
        self.DriveLeftMotor2 = rev.CANSparkMax(DriveLeftMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushed)
        self.DriveRightMotor2 = rev.CANSparkMax(DriveRightMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushed)
        self.DriveLeftMotorControlGroup = wpilib.MotorControllerGroup(self.DriveLeftMotor, self.DriveLeftMotor2) 
        self.DriveRightMotorControlGroup = wpilib.MotorControllerGroup(self.DriveRightMotor, self.DriveRightMotor2)
        self.PickupMechansimMotor = rev.CANSparkMax(PickupMechansimMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        #self.PickAndFiringArmMotor = rev.CANSparkMax(PickupAndFiringArmMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotor1 = rev.CANSparkMax(ShootingMechansimMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotor2 = rev.CANSparkMax(ShootingMechansimMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        #self.ShootingMechansimMotorControlGroup = wpilib.MotorControllerGroup(self.ShootingMechansimMotor1, self.ShootingMechansimMotor2)
        self.drive = wpilib.drive.DifferentialDrive(self.DriveLeftMotorControlGroup, self.DriveRightMotorControlGroup)
#Extra Components
        # self.AbsolutEncoder = placeholder
        # self.IRDetector1 = placeholder
        # self.IRDetector2 = placeholder
        self.TurnRatio = 1
        self.Toggle = 0
        self.ToggleRatio = 3/4
        # self.GrabChainState = False
        # self.CarryingNote = False
        # self.StableNote = False
        # self.kNoteAdjustmentForward = 0.01
        # self.kNoteAdjustmentBackward = -0.01
        # self.Error = 0 
        # self.PickUpZone = placeholder
        # self.ShootZone = placeholder

#Controller Inputs
        self.Controler = wpilib.XboxController(XboxControlerPort)
        self.XboxRightTrigger = wpilib.XboxController.getRightTriggerAxis(self.Controler)
        self.XboxLeftTrigger = wpilib.XboxController.getLeftTriggerAxis(self.Controler)
        self.XboxRightBumper = wpilib.XboxController.getRightBumper(self.Controler)
        self.XboxLeftBumper = wpilib.XboxController.getRightBumper(self.Controler)
        self.XboxA = self.Controler.getAButton()
        self.XboxB = self.Controler.getBButton()
        self.XboxLeftJoyStickY = self.Controler.getLeftY()
        self.XboxLeftJoyStickX = self.Controler.getLeftX()
        self.XboxLeftJoyStickY = wpilib.XboxController.getLeftY(self.Controler)
        self.XboxLeftJoyStickX = wpilib.XboxController.getLeftX(self.Controler)
        self.XboxRightJoyStickY = self.Controler.getRightY()
        self.XboxRightJoyStickX = self.Controler.getRightX()
    def teleopExit(self):

        self.drive.stopMotor()

    def teleopPeriodic(self):
        self.XboxRightBumper = self.Controler.getRightBumperPressed()
        self.XboxLeftJoyStickY = self.Controler.getLeftY()
        self.XboxLeftJoyStickX = self.Controler.getLeftX()
        self.XboxRightJoyStickY = self.Controler.getRightY()
        if self.XboxRightBumper == True and self.Toggle == 1:
            self.Toggle = 0
        elif self.XboxRightBumper == True and self.Toggle == 0:
            self.Toggle = 1

        print("X ", self.XboxLeftJoyStickX, "Y ", self.XboxLeftJoyStickY, "Right Bumper ", self.XboxRightBumper)
#Drive
        self.drive.tankDrive(
                 
                 -self.XboxLeftJoyStickY - self.XboxLeftJoyStickX,
                 self.XboxLeftJoyStickY - self.XboxLeftJoyStickX, True)
        self.ShootingMechansimMotor1.set(self.Toggle * self.ToggleRatio)
        self.ShootingMechansimMotor2.set(-self.Toggle * self.ToggleRatio) #0.9 was formerly here instead of ToggleRatio
        self.PickupMechansimMotor.set(self.XboxA or -(self.XboxB)) # this was formerly self.XboxRightJoyStickY
        self.PickAndFiringArmMotor.set(self.XboxRightJoyStickY) #i took this from commented section below lmao
        

        #self.ShootingMechansimMotor1.set(self.Toggle*self.ToggleRatio)
        #self.ShootingMechansimMotor2.set(self.Toggle*self.ToggleRatio)
                #0.5, -0.5, True)
        #self.PickupMechansimMotor.set(self.XboxRightJoyStickX)
        #self.PickAndFiringArmMotor.set(self.XboxRightJoyStickY)
        #self.ShootingMechansimMotorControlGroup.set(self.XboxLeftTrigger)
#Chain Grab
#         if self.XboxRightBumper == True and self.XboxLeftBumper == True:
#             self.GrabChainState = True
# #Intake
#         if self.IRDetector1 == True or self.IRDetector2 == True:
#             self.CarryingNote = True
#         else:
#             self.CarryingNote = False
#             #add timer to make it wait then run the check again then set state false
#         if self.CarryingNote == False:
#             self.PickupMechansimMotor.set(self.XboxLeftTrigger)
#         elif self.CarryingNote == True:
#             if self.IRDetector1 == True and self.IRDetector2 == True:
#                 self.StableNote = True
#             else:
#                 self.StableNote = False
#         if self.StableNote == False:
#             if self.IRDetector1 == False:
#                 self.PickupMechansimMotor.set(self.kNoteAdjustmentForward)
#             else:
#                 self.PickupMechansimMotor.set(self.kNoteAdjustmentBackward)
# #Intake Arm
#         if self.CarryingNote == False:
#             self.Error = self.PickUpZone - self.AbsolutEncoder
#             #add pid controller for motor set value
#             self.PickAndFiringArmMotor.set(placeholder)
#         else:
#             self.Error = self.ShootZone - self.AbsolutEncoder
#             #add pid controller for motor set value
#             self.PickAndFiringArmMotor.set(placeholder)
# #Shooting
#         if self.StableNote == True and self.AbsolutEncoder == self.ShootZone:
#             self.PickupMechansimMotor.set(-self.XboxRightTrigger)
#             self.ShootingMechansimMotorControlGroup.set(self.XboxRightTrigger)
if __name__ == "__main__":
    wpilib.run(robot)

