#!/usr/bin/env python3
# 
# Filename: runSelected.py
#

import os
# from re import A
import sys
# import config

from time import sleep, time
from defineRobot import *
from myBlocks import *


def runSelected():

    if (True):        
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)

        myTest = FrontMotor.count_per_rot()
        print("count_per_rot = %.2f" % myTest, file=sys.stderr)    
        motorStall('A', 10, 5)
        sleep(2.0)
        motorStall('A', -10, -5)
        sleep(2.0)
