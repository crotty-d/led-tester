# -*- coding: utf-8 -*-

"""Console script for LEDtester."""

import click
click.disable_unicode_literals_warning = True

from LEDtester import utils, LEDtester

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for LEDtester."""
    print('input', input)
    N, instructions = utils.parseFile(input)

    ledTester = LEDtester(N)

    for instruction in instructions:
        ledTester.apply(instruction)

    print('Number occupied: ', ledTester.countOccupied()) 
        
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
