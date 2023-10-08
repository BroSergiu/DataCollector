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
        self.output = 0
        self.deltaTime = deltaTime
        self.setpoint = initialValue
        self.pid = PID(5, 0.005, 0.01, setpoint=initialValue)
        self.pid.output_limits = (-100, 100)

    def update(self):
        self.output = self.pid(self.currentValue)

        self.currentValue += 0.3 * self.output * self.deltaTime 

        # Some dissipation
        self.currentValue -= 0.005 * self.deltaTime 
        return self.currentValue

    def setSetpoint(self, setpoint):
        self.setpoint = setpoint
        self.pid.setpoint = setpoint

if __name__ == "__main__":
    deltaTime = 0.02
    totalTime = 0
    Speed = SimulatedSystem(deltaTime)
    while True:
        Speed.update()
        print ("Current value ", Speed.currentValue, " Setpoint: ", Speed.setpoint, " output: ", Speed.output)
        if totalTime <= 0:
            setpoint = input("select new setpoint: ")
            if setpoint != "":
              Speed.setSetpoint(float(setpoint))
            totalTime = 10
        totalTime -= deltaTime
        time.sleep(deltaTime)
