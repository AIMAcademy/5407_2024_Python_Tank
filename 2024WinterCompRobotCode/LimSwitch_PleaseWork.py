if (self.XboxRightJoyStickY < 0 ) and (self.PickupLimSwitch3 or self.PickupLimSwitch4 == False):
    self.PickAndFiringArmMotor.set(self.XboxRightJoyStickY) 
elif (self.XboxRightJoyStickY > 0) and (self.ShootLimSwitch5 or self.ShootLimSwitch6 == False):
    self.PickAndFiringArmMotor.set(self.XboxRightJoyStickY)
    #this probably could be done better, I programmed this shit like i'm playing baba is you