# -*- coding: utf-8 -*-

"""Console script for led_sim."""

import click
click.disable_unicode_literals_warning = True

from LEDtester import utils, LEDsimulator

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_sim."""
    print('input', input)
    L, instructions = utils.parseFile(input)

    led_sim = LEDsimulator(L)

    for instruction in instructions:
        led_sim.apply(instruction)

    print('Number occupied: ', led_sim.countOn()) 
        
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
