# -*- coding: utf-8 -*-

import requests

def parseFile(file_location):
    if file_location.startswith('http'):
        # Get instructions text from uri
        uri = file_location
        r = requests.get(uri).text
        lines = r.split('\n')
        L = int(lines[0])
        instructions = lines[1:-1]
        
        return L, instructions
    
    else:
        # Read from local file                       
        L, instructions = None, []
        with open(file_location, 'r') as f:
            L = int(f.readline())
            for line in f.readlines():
                instructions.append(line.rstrip())
                                
        return L, instructions

if __name__ == '__main__':
    import sys
    sys.exit()