# -*- coding: utf-8 -*-

import numpy as np
import re

class LEDgrid:
    """
    Class to represent grid of LEDs that be turned on and off in response to certain instructions
    """
    # Class variables
    __lights = None
    
    # Constructor
    def __init__(self, L):
        """Creates an instance of the LED light grid"""
        self.lights = np.zeros((L,L), np.int8)
    
    # Methods    
    def apply(self, instruction):
        """Apply an instruction to the grid, turning on/off lights as specified"""
        
        # Parse instruction via regular expressions
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        parsed = pattern.match(instruction)
        
        # Apply instruction if parsing produced a valid command and coordinates
        if parsed != None:       
            # Assign the command to apply and the coordinates of the effected lights
            parts = parsed.groups()
            cmd = parts[0]
            coords = [min(int(p), self.lights.shape[0] - 1) for p in parts[1:]] # min used in case instruction out of grid bounds
            x1, y1, x2, y2 = coords
                 
            # Apply command to grid of lights
            if cmd == 'turn on':
                self.lights[x1:x2+1, y1:y2+1] = 1 # ranges are inclusive, hence +1
            elif cmd == 'turn off':
                self.lights[x1:x2+1, y1:y2+1] = 0
            elif cmd == 'switch':
                # Get indices of lights that are off (0) and then those that are on (1)
                idx_zeros = np.where(self.lights[x1:x2+1, y1:y2+1] == 0)
                idx_ones = np.where(self.lights[x1:x2+1, y1:y2+1] == 1)
                # Switch them to opposite value
                self.lights[idx_zeros] = 1
                self.lights[idx_ones] = 0
            else:
                # There should be no other possibility here, but just in case invalid cmd slips through
                print("Error: The instruction ({}) contained an invalid command; only 'turn on', 'turn off' and 'switch' are permitted".format(instruction))
    
        else:
            print("Error: The instruction ({}) is not valid, so it was not applied; only 'turn on', 'turn off' and 'switch' are permitted as commands, and coordinates must be given in the format 'x1,y1 through x2,y2', where x1, y1, x2 and y2 are numerical values (will be converted to integers)".format(instruction))
    
    def count(self):
        """Returns the number of lights currently turned on (1)"""
        return self.lights.sum()
    
    
    
