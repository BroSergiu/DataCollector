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

    # Use the __await__ method to make the class awaitable
    def __await__(self):
        # Call ls the constructor and returns the instance
        return self.create().__await__()

    # A method that creates an instance of the class asynchronously
    async def create(self):
        # Perform some asynchronous initialization tasks
        # Return the instance
        return self

    async def update(self):
        pidOutput = self.pid(self.currentValue)

        self.currentValue += 1 * pidOutput * self.deltaTime 

        # Some dissipation
        self.currentValue -= 0.01 * self.deltaTime 
        return self.currentValue

    def setSetpoint(self, setpoint):
        self.setpoint = setpoint
        self.pid.setpoint = setpoint