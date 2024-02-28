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
DriveLeftMotorPort1 = 23
DriveLeftMotorPort2 = 22
DriveRightMotorPort1 = 20
DriveRightMotorPort2 = 21
PickupMechansimMotorPort = 1
PickupAndFiringArmMotorPort = 4
ShootingMechansimMotorPort1 = 2
ShootingMechansimMotorPort2 = 3
LimitSwitchPort1 = 8
LimitSwitchPort2 = 6
LimitSwitchPort3 = 5
LimitSwitchPort4 = 4
LimitSwitchPort5 = 7
LimitSwitchPort6 = 9
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
        self.PickAndFiringArmMotor = rev.CANSparkMax(PickupAndFiringArmMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotor1 = rev.CANSparkMax(ShootingMechansimMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotor2 = rev.CANSparkMax(ShootingMechansimMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        #self.Endcoder = self.PickAndFiringArmMotor.getEncoder(rev.SparkMaxRelativeEncoder.EncoderType.kQuadrature, 42)
        #self.PIDArmMotor = self.PickAndFiringArmMotor.getPIDController()
        self.drive = wpilib.drive.DifferentialDrive(self.DriveLeftMotorControlGroup, self.DriveRightMotorControlGroup)
#Xbox Controlers
        self.Controler = wpilib.XboxController(XboxControlerPort)
#Extra Components / Variables
        self.TurnRatio = 1
        self.ShooterToggle = 0
        self.ShooterSpeed = 0
        self.SuckerToggle = -1
        self.SuckerSpeed = 1
        self.SuckerToggleRatio = 1/8
        self.ShooterRatio = 3/4
        self.CrossUp = 0
        self.CrossLeft = 270
        self.CrossRight = 90
        #self.kP = 0.1
        #self.kI = 0.1
        #self.kD = 0.1
        #self.PIDArmMotor.setP(self.kP)
        #self.PIDArmMotor.setI(self.kI)
        #self.PIDArmMotor.setD(self.kD)
        self.TargetPosition = 1000
        #rev.SparkMaxRelativeEncoder.setPositionConversionFactor(self.Endcoder, 1.0)
        #rev.SparkMaxRelativeEncoder.setVelocityConversionFactor(self.Endcoder, 1.0)
        # self.GrabChainState = False
        # self.CarryingNote = False
        # self.StableNote = False
        # self.kNoteAdjustmentForward = 0.01
        # self.kNoteAdjustmentBackward = -0.01

    def teleopExit(self):

        self.drive.stopMotor()

    def teleopPeriodic(self):
#Limit Switches
        #self.NoteLimSwitch1 = wpilib.DigitalInput(LimitSwitchPort1)
        #self.NoteLimSwitch2 = wpilib.DigitalInput(LimitSwitchPort2)
        #self.PickupLimSwitch3 = wpilib.DigitalInput(LimitSwitchPort3)
        #self.PickupLimSwitch4 = wpilib.DigitalInput(LimitSwitchPort4)
        #self.ShootLimSwitch5 = wpilib.DigitalInput(LimitSwitchPort5)
        #self.ShootLimSwitch6 = wpilib.DigitalInput(LimitSwitchPort6)
#Xbox Controls
        self.XboxRightBumperPressed = self.Controler.getRightBumperPressed()
        self.XboxBButtonPressed = self.Controler.getBButtonPressed()
        self.XboxBButton = self.Controler.getBButton()
        self.XboxAButtonPressed = self.Controler.getAButtonPressed()
        self.XboxAButton = self.Controler.getAButton()
        self.XboxLeftJoyStickY = self.Controler.getLeftY()
        self.XboxLeftJoyStickX = self.Controler.getLeftX()
        self.XboxCrossLeft = self.Controler.getPOV()
        self.XboxRightJoyStickY = self.Controler.getRightY()
#Toggles with Speed Calculations
        if self.XboxRightBumperPressed == True and self.ShooterToggle == 1:
            self.ShooterToggle = 0
            self.ShooterSpeed = self.ShooterToggle * self.ShooterRatio
        elif self.XboxRightBumperPressed == True and self.ShooterToggle == 0:
            self.ShooterToggle = 1
            self.ShooterSpeed = self.ShooterToggle * self.ShooterRatio
        if self.XboxBButtonPressed == True and self.SuckerToggle == 0:
            self.SuckerToggle = 1
            self.SuckSpeed = self.SuckerToggle * self.SuckerToggleRatio
        elif self.XboxBButtonPressed == True and self.SuckerToggle == 1:
            self.SuckerToggle = 0
            self.SuckSpeed = self.SuckerToggle * self.SuckerToggleRatio
        if self.XboxAButtonPressed == True and self.SuckerToggle == 0:
            self.SuckerToggle = -1
            self.SuckSpeed = self.SuckerToggle * self.SuckerToggleRatio
        elif self.XboxAButtonPressed == True and self.SuckerToggle == -1:
            self.SuckerToggle = 0
            self.SuckSpeed = self.SuckerToggle * self.SuckerToggleRatio
        print("X ", self.XboxLeftJoyStickX, "Y ", self.XboxLeftJoyStickY, "Right Bumper ", self.XboxRightBumperPressed, "B Button Pressed ", self.XboxBButtonPressed, "B Button ", self.XboxBButton)#, "Lim Switches 1, 2 ", self.NoteLimSwitch1, self.NoteLimSwitch2)#, "Encoder Position ", rev.RelativeEncoder.getPosition(self.Endcoder))
#Drive
        self.drive.tankDrive(-self.XboxLeftJoyStickY - self.XboxLeftJoyStickX, self.XboxLeftJoyStickY - self.XboxLeftJoyStickX, True)
#Shooting
        self.ShootingMechansimMotor1.set(self.ShooterSpeed)
        self.ShootingMechansimMotor2.set(-self.ShooterSpeed) 
#Arm
        #self.PIDArmMotor.setReference(self.TargetPosition, )
        self.PickAndFiringArmMotor.set(self.XboxRightJoyStickY) 
#Intake
        if self.XboxBButton == True or self.XboxAButton == True:
            self.PickupMechansimMotor.set(self.SuckerSpeed)
        else:
            self.PickupMechansimMotor.set(0) 
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


