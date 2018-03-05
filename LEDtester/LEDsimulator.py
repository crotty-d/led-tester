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
               
            x1, y1, x2, y2 = coords
                 
            # Apply command to grid of lights
            if cmd == 'turn on':
                self.lights[x1:x2+1, y1:y2+1] = 1 # ranges are inclusive, hence +1
                return 0
            elif cmd == 'turn off':
                self.lights[x1:x2+1, y1:y2+1] = 0
                return 0
            elif cmd == 'switch':
                # Switch lights to opposite values
                self.lights[x1:x2+1, y1:y2+1][[self.lights[x1:x2+1, y1:y2+1] == 0]] = 1
                self.lights[x1:x2+1, y1:y2+1][[self.lights[x1:x2+1, y1:y2+1] == 1]] = 0 # FIXME undoes some of the 0-->1 flips; both need to operate on original grid and then compbine
                                
                # Alternative simple iterative method (much slower)
#                 for x in range(x1, x2+1):
#                     for y in range(y1, y2+1):
#                         if self.lights[x, y] == 0:
#                             self.lights[x, y] = 1
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
    
    
    
