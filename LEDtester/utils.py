# -*- coding: utf-8 -*-

import requests

def parseFile(input): #TODO: if/else to read into common variable, then parse this variable

    if input.startswith('http'):
        uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        r = requests.get(uri).text
        print('\n'.join(r.split('\n')[:5]))
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        # haven't written the code yet...
        return N, instructions
    return

if __name__ == '__main__':
    import sys
    sys.exit()