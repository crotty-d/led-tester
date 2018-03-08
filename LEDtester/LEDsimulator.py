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
            coords = []
            for p in parts[1:]:
                p = int(p)
                if p >= 0:
                    coords.append(min(p, self.lights.shape[0] - 1)) # min used in case instruction out of grid bounds
                else:
                    coords.append(0) # negative always outside bounds
               
            x1, y1, x2, y2 = min(coords[0], coords[2]), min(coords[1], coords[3]), max(coords[0], coords[2]), max(coords[1], coords[3])
                 
            # Apply command to grid of lights
            if cmd == 'turn on':
                self.lights[y1:y2+1, x1:x2+1] = 1 # ranges are inclusive, hence +1
                return 0
            elif cmd == 'turn off':
                self.lights[y1:y2+1, x1:x2+1] = 0
                return 0
            elif cmd == 'switch':
                # Get indices of lights that are off (0) and then those that are on (1)
                idx_zeros = np.where(self.lights[y1:y2+1, x1:x2+1] == 0)
                idx_ones = np.where(self.lights[y1:y2+1, x1:x2+1] == 1)
                idx0_offset =(idx_zeros[0] + y1, idx_zeros[1] + x1)
                idx1_offset =(idx_ones[0] + y1, idx_ones[1] + x1)
                # Switch them to opposite value
                self.lights[idx0_offset] = 1
                self.lights[idx1_offset] = 0
                
                # Alternative simple iterative method (much slower)
#                 for x in range(y1, y2+1):
#                     for x in range(x1, x2+1):
#                         if self.lights[y, x] == 0:
#                             self.lights[y, x] = 1
#                         else:
#                             self.lights[x, y] = 0

                return 0
            
            else:
                # There should be no other possibility here, but just in case invalid cmd slips through
                return 1
   
        else:
            return 1
    
    def count(self):
        """Returns the number of lights currently turned on (1)"""
        return self.lights.sum()
    
    
    
