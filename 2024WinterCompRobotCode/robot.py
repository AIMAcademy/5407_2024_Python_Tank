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
placeholder = 0
DriveLeftMotorPort1 = 23
DriveLeftMotorPort2 = 22
DriveRightMotorPort1 = 20
DriveRightMotorPort2 = 21
PickupMechansimMotorPort = 1
IntakeArmMotorPort = 4
ShootingMechansimMotorPortLeftUpper = 2
ShootingMechansimMotorPortRightUpper = 3
ShootingMechansimMotorPortLeftLower = 5
ShootingMechansimMotorPortRightLower = 6
HangerLeftMotorPort = 9
HangerRightMotorPort = 10
LimitSwitchPort1 = 8
LimitSwitchPort2 = 6
LimitSwitchPort3 = 5
LimitSwitchPort4 = 4
LimitSwitchPort5 = 7
LimitSwitchPort6 = 9
XboxControlerPort = 0
XboxControlerPort2 = 1
class robot(wpilib.TimedRobot):
    def robotInit(self):

#Motors + WPILIB drive
        self.DriveLeftMotor = rev.CANSparkMax(DriveLeftMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveRightMotor = rev.CANSparkMax(DriveRightMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveLeftMotor2 = rev.CANSparkMax(DriveLeftMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveRightMotor2 = rev.CANSparkMax(DriveRightMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveLeftMotorControlGroup = wpilib.MotorControllerGroup(self.DriveLeftMotor, self.DriveLeftMotor2) 
        self.DriveRightMotorControlGroup = wpilib.MotorControllerGroup(self.DriveRightMotor, self.DriveRightMotor2)
        self.PickupMechansimMotor = rev.CANSparkMax(PickupMechansimMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.PickAndFiringArmMotor = rev.CANSparkMax(IntakeArmMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.PickAndFiringArmMotorEncoder = self.PickAndFiringArmMotor.getEncoder()
        self.ShootingMechansimMotorLeftUpper = rev.CANSparkMax(ShootingMechansimMotorPortLeftUpper, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotorRightUpper = rev.CANSparkMax(ShootingMechansimMotorPortRightUpper, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotorLeftLower =  rev.CANSparkMax(ShootingMechansimMotorPortLeftLower, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotorRightLower =  rev.CANSparkMax(ShootingMechansimMotorPortRightLower, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.ShootingMechansimMotorGroupLeft = wpilib.MotorControllerGroup(self.ShootingMechansimMotorLeftUpper, self.ShootingMechansimMotorLeftLower)
        self.ShootingMechansimMotorGroupRight = wpilib.MotorControllerGroup(self.ShootingMechansimMotorRightUpper, self.ShootingMechansimMotorRightLower) 
        self.NoteLimSwitch1 = wpilib.DigitalInput(LimitSwitchPort1)
        self.NoteLimSwitch2 = wpilib.DigitalInput(LimitSwitchPort2)
        self.PickupLimSwitch3 = wpilib.DigitalInput(LimitSwitchPort3)
        self.PickupLimSwitch4 = wpilib.DigitalInput(LimitSwitchPort4)
        self.ShootLimSwitch5 = wpilib.DigitalInput(LimitSwitchPort5)
        self.ShootLimSwitch6 = wpilib.DigitalInput(LimitSwitchPort6)
        self.HangerLeftMotor = rev.CANSparkMax(HangerLeftMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.HangerRightMotor = rev.CANSparkMax(HangerRightMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.HangerMotorGroup = wpilib.MotorControllerGroup(self.HangerLeftMotor, self.HangerRightMotor)
        self.Timer = wpilib.Timer()
        self.PIDArmMotor = self.PickAndFiringArmMotor.getPIDController()
        self.drive = wpilib.drive.DifferentialDrive(self.DriveLeftMotorControlGroup, self.DriveRightMotorControlGroup)
#Xbox Controlers
        self.Controler = wpilib.XboxController(XboxControlerPort)
        self.Controler2 = wpilib.XboxController(XboxControlerPort2)
#Extra Components / Variables
        self.DriveSpeed = 0
        self.DriveToggle = 0
        self.DriveRatio = 0.5
        self.TurnRatio = 0.66
        self.ShooterToggle = 0
        self.ShooterSpeed = 0
        self.ShooterRatioLeft = .5
        self.ShooterRatioRight = .5
        self.SuckerToggle = 0
        self.SuckerSpeed = 0
        self.SuckerToggleRatio = 1 #0.5
        self.ArmSpeed = 0
        self.ArmRatio = 0.166
        self.CrossUp = 0
        self.CrossLeft = 270
        self.CrossRight = 90
        self.AutonomousDriveTime = 2
        #self.kP = 0.1
        #self.kI = 0.1
        #self.kD = 0.1
        #self.VelocityConbersionFactor = 1.0
        #self.PositionConversionFactor = 1.0
        #self.PIDArmMotor.setP(self.kP)
        #self.PIDArmMotor.setI(self.kI)
        #self.PIDArmMotor.setD(self.kD)
        #self.TargetPosition = 0
        #self.PickAndFiringArmMotorEncoder.setPositionConversionFactor(self.PositionConversionFactor)
        #self.PickAndFiringArmMotorEncoder.setVelocityConversionFactor(self.VelocityConbersionFactor)
        self.HangerLeftSpeed = 0
        self.HangerRightSpeed = 0
        self.HangerCombined = 0
        self.HangerRatio = 1 #0.2
        self.HangerRatioLeft = 1 #0.1
        self.HangerRatioRight = 1 #0.1
    def teleopExit(self):

        self.drive.stopMotor()

    def teleopPeriodic(self):
#Xbox Controls
        self.XboxCross = self.Controler2.getPOV()
        self.XboxRightBumperPressed = self.Controler2.getRightBumperPressed()
        self.XboxLeftBumperPressed = self.Controler.getLeftBumperPressed()
        self.XboxBButtonPressed = self.Controler2.getBButtonPressed()
        self.XboxBButton = self.Controler2.getBButton()
        self.XboxAButtonPressed = self.Controler2.getAButtonPressed()
        self.XboxAButton = self.Controler2.getAButton()
        self.XboxLeftJoyStickY = self.Controler.getLeftY()
        self.XboxLeftJoyStickX = self.Controler.getLeftX()
        self.XboxRightJoyStickY = self.Controler.getRightY()
        self.XboxRightJoyStickX = self.Controler.getRightX()
        self.Xbox2XButton = self.Controler2.getXButton()
        self.Xbox2YButton = self.Controler2.getYButton()
        self.Xbox2RightTrigger = self.Controler2.getRightTriggerAxis()
        self.Xbox2LeftTrigger = self.Controler2.getLeftTriggerAxis()
        self.Xbox2LeftBumper = self.Controler2.getLeftBumper()
#Toggles with Speed Calculations
        if (self.XboxLeftBumperPressed == True and self.DriveRatio == 1):
            self.DriveRatio = 0.5
        elif (self.XboxLeftBumperPressed == True and self.DriveRatio == 0.5):
            self.DriveRatio = 1
        if (self.XboxRightBumperPressed == True and self.ShooterToggle == 1):
            self.ShooterToggle = 0
            self.ShooterSpeed = self.ShooterToggle
        elif (self.XboxRightBumperPressed == True and self.ShooterToggle == 0):
            self.ShooterToggle = 1
            self.ShooterSpeed = self.ShooterToggle
        if (self.XboxBButtonPressed == True and self.SuckerToggle == 0) and (self.NoteLimSwitch1.get() == True and self.NoteLimSwitch2.get() == True):
            self.SuckerToggle = 1
            self.SuckerSpeed = self.SuckerToggle * self.SuckerToggleRatio
        elif (self.XboxBButtonPressed == True and self.SuckerToggle == 1) or (self.XboxBButtonPressed == True and self.SuckerToggle == -1) or (self.NoteLimSwitch1.get() == False and self.SuckerToggle == 1) or (self.NoteLimSwitch2.get() == False and self.SuckerToggle == 1):
            self.SuckerToggle = 0
            self.SuckerSpeed = self.SuckerToggle * self.SuckerToggleRatio
        if (self.XboxAButtonPressed == True and self.SuckerToggle == 0):
            self.SuckerToggle = -1
            self.SuckerSpeed = self.SuckerToggle * self.SuckerToggleRatio
        elif (self.XboxAButtonPressed == True and self.SuckerToggle == 1) or (self.XboxAButtonPressed == True and self.SuckerToggle == -1) :
            self.SuckerToggle = 0
            self.SuckerSpeed = self.SuckerToggle * self.SuckerToggleRatio
        if (self.XboxCross == self.CrossLeft):
            self.ArmSpeed = 1 * self.ArmRatio
        elif (self.XboxCross == self.CrossRight):
            self.ArmSpeed = -1 * self.ArmRatio
        else:
            self.ArmSpeed = 0 * self.ArmRatio
        if (self.PickupLimSwitch3.get() == True) or (self.PickupLimSwitch4.get() == True):
            self.PickupPosition = self.PickAndFiringArmMotorEncoder.getPosition()
        if (self.ShootLimSwitch5.get() == True) or (self.ShootLimSwitch6.get() == True):
            self.ShootPosition = self.PickAndFiringArmMotorEncoder.getPosition()
        if (self.Xbox2YButton == True):
            self.HangerCombined = 1 * self.HangerRatio #unsure what direction this moves it at the moment, supposed to go up. also, feel free to change speed
        elif (self.Xbox2XButton == True):
            self.HangerCombined = -1 * self.HangerRatio
        else:
            self.HangerCombined = 0 * self.HangerRatio
        if (self.Xbox2LeftBumper == True):
            self.HangerLeftSpeed = -self.Xbox2LeftTrigger * self.HangerRatioLeft
            self.HangerRightSpeed = -self.Xbox2RightTrigger * self.HangerRatioRight
        else:
            self.HangerLeftSpeed = self.Xbox2LeftTrigger * self.HangerRatioLeft
            self.HangerRightSpeed = self.Xbox2RightTrigger * self.HangerRatioRight
            #My brother called me "The medicated Terry Davis that this team deserves"

        #print("X ", self.XboxLeftJoyStickX, "Y ", self.XboxLeftJoyStickY, "Right Bumper ", self.XboxRightBumperPressed, "B Button Pressed ", self.XboxBButtonPressed, "B Button ", self.XboxBButton, "Sucker Toggle ", self.SuckerToggle, "Lim Switches 1, 2 ", self.NoteLimSwitch1.get(), self.NoteLimSwitch2.get())#, "Encoder Position ", rev.RelativeEncoder.getPosition(self.Encoder))

#Drive
        self.drive.tankDrive(-self.XboxLeftJoyStickY * self.DriveRatio - self.XboxRightJoyStickX * (-(self.TurnRatio)), self.XboxLeftJoyStickY * self.DriveRatio - self.XboxRightJoyStickX * (-(self.TurnRatio)), True)
#Shooting
        self.ShootingMechansimMotorGroupLeft.set(self.ShooterSpeed * self.ShooterRatioLeft)
        self.ShootingMechansimMotorGroupRight.set(-self.ShooterSpeed * self.ShooterRatioRight)

#Arm
#        self.PIDArmMotor.setReference()
        self.PickAndFiringArmMotor.set(self.ArmSpeed) 
#Intake
        self.PickupMechansimMotor.set(self.SuckerSpeed)
    def robotPeriodic(self) -> None:
        wpilib.SmartDashboard.putBoolean("NoteLim1", self.NoteLimSwitch1.get())
        wpilib.SmartDashboard.putBoolean("NoteLim2", self.NoteLimSwitch2.get())
        wpilib.SmartDashboard.putNumber("IntakeEncoder", self.PickAndFiringArmMotorEncoder.getPosition())
#        if limit:
#            self.PickAndFiringArmMotorEncoder.setPosition(0)
        
#Hanger
        self.HangerMotorGroup.set(self.HangerCombined)
        self.HangerLeftMotor.set(self.HangerLeftSpeed)
        self.HangerRightMotor.set(self.HangerRightSpeed)
    def autonomousInit(self):
       self.Timer.reset()
       self.Timer.start()
    def autonomousPeriodic(self):
        #print(self.Timer.get())
        if self.Timer.get() < 2:
            self.DriveSpeed = 1
        else:
            self.DriveSpeed = 0
        self.drive.tankDrive(self.DriveSpeed, -self.DriveSpeed)
            #self.ShooterToggle = 1
            #self.ShooterSpeed = self.ShooterToggle
        #elif self.Timer.get() > 2 and self.Timer.get() < 4:
            #self.ShooterToggle = 1
            #self.ShooterSpeed = self.ShooterToggle
            #self.SuckerToggle = 1
            #self.SuckerSpeed = self.SuckerToggle * self.SuckerToggleRatio
        #elif self.Timer.get() > 4 and self.Timer.get() < 6:
        #    self.ShooterToggle = 0
        #    self.ShooterSpeed = self.ShooterToggle
        #    self.SuckerSpeed = self.SuckerToggle * self.SuckerToggleRatio
        #    self.DriveSpeed = -1 * self.DriveRatio
        #    self.drive.tankDrive(self.DriveSpeed, -self.DriveSpeed, True)
        #elif self.Timer.get() > 4:
        #    self.ShooterToggle = 0
        #    self.SuckerToggle = 0
        #    self.DriveSpeed = 0
        #    self.drive.tankDrive(self.DriveSpeed, -self.DriveSpeed, True)
        #self.PickupMechansimMotor.set(self.SuckerSpeed)
        #self.ShootingMechansimMotorGroupLeft.set(self.ShooterSpeed * self.ShooterRatioLeft)
        #self.ShootingMechansimMotorGroupRight.set(-self.ShooterSpeed * self.ShooterRatioRight)

if __name__ == "__main__":
    wpilib.run(robot)
