=========
LEDtester
=========


.. image:: https://img.shields.io/pypi/v/LEDtester.svg
        :target: https://pypi.python.org/pypi/LEDtester

.. image:: https://img.shields.io/travis/crotty-d/LEDtester.svg
        :target: https://travis-ci.org/crotty-d/LEDtester

.. image:: https://readthedocs.org/projects/LEDtester/badge/?version=latest
        :target: https://LEDtester.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




LED tester assignment


* Free software: MIT license
* Documentation: https://LEDtester.readthedocs.io.


Functionality
-------------

This python package simulates a square grid of LED lights, which we control by sending commands to turn on or off certain rectangular regions. Its main purpose is to count the numbr of lights that are on after all instructions have been carried out.

The L × L lights are modelled as a 2 dimensional grid with L rows of lights and L lights in each row and the LED's at each corner are (0, 0), (0, L − 1), (L − 1, L − 1) and (L − 1, 0). The lights are either on or off.

The LEDtester module in the package sends instructions to turn on, turn off, or switch various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

For example:
* "turn on 0,0 through 999,999" would turn on (or leave on) every light.
* "switch 0,0 through 999,0" would toggle the first line of 1000 lights, turning
off the ones that were on, and turning on the ones that were off.
* "turn off 499,499 through 500,500" would turn off (or leave off) the middle
four lights.

After applying the series of instructions, the number of lights that are on is calculated and displayed in the console.

Usage
-----
* Installation: $> pip install git+https://github.com/crotty-d/led-tester
 * Ideally create  a dedicated virtual environment based on the requirements.txt file, and pip install into this

* Run: $> solve_led --input <local path or URI for instructions file>
 * Example: solve_led --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt


Package template credit
-----------------------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
