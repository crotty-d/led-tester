# -*- coding: utf-8 -*-

import requests

def parse_file(file_location):
    if file_location.startswith('http'):
        try:
            # Get file from uri
            uri = file_location
            r = requests.get(uri)
                   
        # Serious errors raised by requests module
        except requests.exceptions.RequestException as e:
            print('Error : {}'.format(e))
            return 0, ['error']
        
        else:
            # Get instructions text from file if status code is 2xx; otherwise invalid response
            if r.status_code // 100 == 2:
                content = r.text
                lines = content.split('\n')
                L = int(lines[0])
                instructions = lines[1:-1]
                
                return L, instructions
            
            else:
                print('Invalid response: {}'.format(r))
                return 0, ['invalid response']
        
    else:
        try: 
            # Read from local file                       
            L, instructions = None, []
            with open(file_location, 'r') as f:
                L = int(f.readline())
                for line in f.readlines():
                    instructions.append(line.rstrip())
                                    
            return L, instructions
        
        except IOError as e:
                print('Error: {}'.format(e))
                return 0, ['error']

if __name__ == '__main__':
    import sys
    sys.exit()