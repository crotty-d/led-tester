# -*- coding: utf-8 -*-

import requests

# TODO 3 functions?: parse_file calls parse_lines and parse_instructions (regex parse); instruction_parser class as part of LSDtester?

def parseFile(input): #TODO: if/else to read into common variable, then parse this variable

    if input.startswith('http'):
        uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        r = requests.get(uri).text
        print('\n'.join(r.split('\n')[:5]))
    else:
        # Read from local file
        L, instructions = None, []
        with open(input, 'r') as f:
            L = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
                                
        return L, instructions
    return

if __name__ == '__main__':
    import sys
    sys.exit()