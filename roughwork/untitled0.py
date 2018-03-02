import numpy as np
import re

lights = np.zeros((10, 10), np.int8)
instruct = 'turn on 0,0 through 9,9\n'

#parse instruction via regular expressions
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
parts = pat.match(instruct).groups()

coord = [int(i) for i in parts[1:]]

if parts[0] == 'turn on':
    lights[coord[0]:coord[2], coord[1]:coord[3]] = 1
elif parts[0] == 'turn off':
    lights[coord[0]:coord[2], coord[1]:coord[3]] = 0
elif parts[0] == 'switch':
    # Get indices of lights that are off (0) and then those that are on (1)
    idx_zeros = np.where(lights == 0)
    idx_ones = np.where(lights == 1)
    # Switch them to opposite value
    lights[idx_zeros] = 1
    lights[idx_ones] = 0
    
    

print(lights.sum())
print(lights)


