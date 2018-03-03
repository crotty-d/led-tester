# -*- coding: utf-8 -*-

import requests

# TODO 3 functions?: parse_file calls parse_lines and parse_instructions (regex parse); instruction_parser class as part of LSDtester?

def parseFile(file_location): #TODO: if/else to read into common variable, then parse this variable

    if file_location.startswith('http'):
        uri = file_location
        r = requests.get(uri).text
        instructions = '\n'.join(r.split('\n'))
        L = instructions[0]
        
        return L, instructions
    else:
        # Read from local file                       
        L, instructions = None, []
        with open(file_location, 'r') as f:
            L = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
                                
        return L, instructions

if __name__ == '__main__':
    import sys
    sys.exit()