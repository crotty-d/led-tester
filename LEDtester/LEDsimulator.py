# -*- coding: utf-8 -*-

import numpy as np

class LEDgrid:
    """
    Class to represent grid of LEDs that be turned on and off in response to certain instructions
    """
    
    lights = None
    
    def __init__(self, L):
        self.lights = np.zeros((L,L), np.int8)
        
    def apply(self, instruction):
        pass
    
    def count(self):
        return self.lights.sum()
    
    
    
