# -*- coding: utf-8 -*-

import requests

def parse_file(file_location):
    if file_location.startswith('http'):
        try:
            # Get uri
            uri = file_location
            r = requests.get(uri)
            # Get instructions text from uri if status code is 2xx; otherwise invalid response
            if not r.status_code // 100 == 2:
                content = requests.get(uri).text
                lines = content.split('\n')
                L = int(lines[0])
                instructions = lines[1:-1]
                
                return L, instructions
            
            else:
                print('Invalid response: {}'.format(r))
                return 0, ['invalid response']
        
        # Serious errors raised by requests module
        except requests.exceptions.RequestException as e:
            print('Error : {}'.format(e))
            return 0, ['error']
        
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