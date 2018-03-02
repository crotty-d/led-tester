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

    ledgrid = LEDsimulator.LEDgrid(L)

    for instruction in instructions:
        ledgrid.apply(instruction)

    print(ledgrid.count(), 'LEDs are on.') 
        
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
