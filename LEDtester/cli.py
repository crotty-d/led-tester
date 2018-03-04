# -*- coding: utf-8 -*-

"""Console script for led_sim."""

import time

import click
click.disable_unicode_literals_warning = True

from LEDtester import utils, LEDsimulator

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for LEDtester."""
    t1 = time.time()
    try:
        if input != None:
            
            # Parse instructions from text file
            print('input:', input)
            L, instructions = utils.parse_file(input)
            
            # Instantiate LED grid object
            grid = LEDsimulator.LEDgrid(L)
            
            # Apply instructions to grid object
            invalid_count = 0
            n_apply = 0
            for instruction in instructions:
                invalid_count += grid.apply(instruction) # applies instruction and then returns 0, or 1 if invalid instruction
                n_apply += 1
                print(n_apply)
                
            # Output number of lights that are on after all instructions carried out   
            print(grid.count(), 'LEDs are on')
            print('Number of invalid instructions:', invalid_count)
            # Output time taken to calculate
            t2 = time.time()
            print('Time to calculate:', t2 - t1, 'seconds')
            
        else:
            raise ValueError
    
    except ValueError:
        print("Error: No input argument was given. The command requires a single filepath or a URI as its argument.")
            
    return 0


if __name__ == "__main__":
    sys.exit(main())
