# -*- coding: utf-8 -*-

import numpy as np
import re

class LEDgrid:
    """
    Class to represent grid of LEDs that be turned on and off in response to certain instructions
    """
    # Class variables
    lights = None
    
    # Constructor
    def __init__(self, L):
        """Constructs an instance of a LED light grid"""
        self.lights = np.zeros((L,L), np.int8)
    
    # Methods    
    def apply(self, instruction):
        """Apply an instruction to the grid, turning on/off lights as specified"""
        
        # Parse instruction via regular expressions
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        parts = pattern.match(instruction).groups()
        
        cmd = parts[0]
        coord = [int(i) for i in parts[1:]]
        
        if cmd == 'turn on':
            self.lights[coord[0]:coord[2]+1, coord[1]:coord[3]+1] = 1
        elif cmd == 'turn off':
            self.lights[coord[0]:coord[2]+1, coord[1]:coord[3]+1] = 0
        elif cmd == 'switch':
            # Get indices of lights that are off (0) and then those that are on (1)
            idx_zeros = np.where(self.lights == 0)
            idx_ones = np.where(self.lights == 1)
            # Switch them to opposite value
            self.lights[idx_zeros] = 1
            self.lights[idx_ones] = 0
        else:
            print("The instruction ({}) contained an invalid command; only 'turn on', 'turn off' and 'switch' are permitted".format(instruction))
    
    def count(self):
        """Returns the number of lights currently turned on (1)"""
        return self.lights.sum()
    
    
    
