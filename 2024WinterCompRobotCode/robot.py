#2024 Winter Compatition Robot

#imports
import rev
import wpilib
import wpilib.drive
import wpilib.interfaces
import wpilib.event
from wpilib.drive import DifferentialDrive

#ports
placeholder = 1
DriveLeftMotorPort1 = placeholder
DriveLeftMotorPort2 = placeholder
DriveRightMotorPort1 = placeholder
DriveRightMotorPort2 = placeholder
PickupMechansimMotorPort = placeholder
PickupAndFiringArmMotorPort = placeholder
ShootingMechansimMotorPort1 = placeholder
ShootingMechansimMotorPort2 = placeholder
XboxControlerPort = placeholder 
class robot(wpilib.TimedRobot):
    def robotInit(self):

#Motors can be listed here, for any new motors make sure to add them to the appropriate motor group side
        self.DriveLeftMotor = rev.CANSparkMax(DriveLeftMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveRightMotor = rev.CANSparkMax(DriveRightMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveLeftMotor2= rev.CANSparkMax(DriveLeftMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveRightMotor2 = rev.CANSparkMax(DriveRightMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.DriveLeftMotorControlGroup = wpilib.MotorControllerGroup(self.DriveLeftMotor, self.DriveLeftMotor2) 
        self.DriveRightMotorControlGroup = wpilib.MotorControllerGroup(self.DriveRightMotor, self.DriveRightMotor2)
        #self.PickupMechansimMotor = rev.CANSparkMax(PickupMechansimMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        #self.PickAndFiringArmMotor = rev.CANSparkMax(PickupAndFiringArmMotorPort, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        #self.ShootingMechansimMotor1 = rev.CANSparkMax(ShootingMechansimMotorPort1, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        #self.ShootingMechansimMotor2 = rev.CANSparkMax(ShootingMechansimMotorPort2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        #self.AbsolutEncoder = 1
        self.drive = wpilib.drive.DifferentialDrive(self.DriveLeftMotorControlGroup, self.DriveRightMotorControlGroup)

        self.TurnRatio = placeholder

        self.Controler = wpilib.XboxController(XboxControlerPort)


        self.XboxAButton = wpilib.XboxController.getAButton(self.Controler)
        self.XboxBButton = wpilib.XboxController.getBButton(self.Controler)
        self.XboxXButton = wpilib.XboxController.getXButton(self.Controler)
        self.XboxYButton = wpilib.XboxController.getYButton(self.Controler)
        self.XboxLeftJoyStickY = self.Controler.getLeftY()
        self.XboxLeftJoyStickX = self.Controler.getLeftX()
        self.XboxRightJoyStickY = self.Controler.getRightY()
        self.XboxRightJoyStickX = self.Controler.getRightX()



    def teleopExit(self):

        self.drive.stopMotor()

    def teleopPeriodic(self):

        self.drive.tankDrive(
                 (self.XboxLeftJoyStickY + (self.XboxLeftJoyStickX * self.TurnRatio)),
                 (self.XboxLeftJoyStickY - (self.XboxLeftJoyStickX * self.TurnRatio)) )

if __name__ == "__main__":
    wpilib.run(robot)

