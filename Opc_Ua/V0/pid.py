import os
import sys
import time
import asyncio
from simple_pid import PID

#set PID system speed
systemClock = 0.1

class SimulatedSystem:
    """
    Simple simulation of a value with some dissipation
    """

    def __init__(self, deltaTime, initialValue = 100):
        self.currentValue = initialValue
        self.deltaTime = deltaTime
        self.setpoint = initialValue
        self.pid = PID(1, 0.01, 0.1, setpoint=initialValue)
        self.pid.output_limits = (-100, 100)

    def update(self):
        pidOutput = self.pid(self.currentValue)

        self.currentValue += 1 * pidOutput * self.deltaTime 

        # Some dissipation
        self.currentValue -= 0.01 * self.deltaTime 
        return self.currentValue

    def setSetpoint(self, setpoint):
        self.setpoint = setpoint
        self.pid.setpoint = setpoint