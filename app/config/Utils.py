import time
import inspect
"""
this module contains useful tools
"""

##### stop program to reach certain time ######
def wait(nexttime):
    while (time.time() < nexttime):
        pass


##### return line of python code which is running useful for logging critical points ######
def lineno():
    return inspect.currentframe().f_back.f_lineno

