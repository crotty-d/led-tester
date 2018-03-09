#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `LEDtester` package."""

import sys
sys.path.append('.')


import numpy as np

from click.testing import CliRunner

from LEDtester import LEDsimulator
from LEDtester import cli
from LEDtester import utils

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    # FIXME Cannot figure out to pass option argument to invoked function (nothing in docs)
#     result = runner.invoke(cli.main, ['--input ../data/test_data.txt'])
#     assert result.exit_code == 0
#     print(result.output)
#     assert 'test_data.txt' and 'seconds' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.output
 
def test_parse_valid_file():
    file = './data/test_data.txt'
    L, instructions = utils.parse_file(file)
    assert L == 10
    assert instructions == ['turn on 0,0 through 9,9', 'turn off 0,0 through 9,9', 'switch 0,0 through 9,9', 'turn off 0,0 through 9,9', 'turn on 2,2 through 7,7']

def test_parse_invalid_filepath():
    file = './data/doesnotexist.txt'
    L, instructions = utils.parse_file(file)
    assert L == 0
    assert instructions[0] == 'error'
    
    grid = LEDsimulator.LEDgrid(10)
    grid.lights[4,4] = 1
        
    for instruction in instructions:
        grid.apply(instruction)
        
    print(grid.lights)
        
    assert grid.count() == 1
    

def test_LEDsim_construct():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    print(grid.lights)
    
    assert isinstance(grid.lights, np.ndarray)
    assert grid.lights.shape == (L, L)
    assert grid.lights.sum() == 0
    
    
def test_LEDsim_count():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    print(grid.lights)
    assert grid.count() == 0
    
    grid.lights[2:5, 1:3] = 1
    print(grid.lights)
    assert grid.count() == 6
    

def test_LEDsim_instruct_on():
    L = 20
    grid = LEDsimulator.LEDgrid(L)
    instruction = 'turn on 0,0 through 9,9'
    grid.apply(instruction)
    
    print(grid.lights)
    
    # Check on/off pattern correct
    on_coords = ((0,0), (5,5), (0,9), (9,0))
    off_coords = ((10,10), (15,15), (0,10), (10,0))
    
    for coord in on_coords:
        assert grid.lights[coord[1], coord[0]] == 1, coord
    for coord in off_coords:
        assert grid.lights[coord[1], coord[0]] == 0, coord
        
    # Check count
    assert grid.count() == 100
    
    
def test_LEDsim_instruct_off():
    L = 20
    grid = LEDsimulator.LEDgrid(L)
    grid.lights[0:20, 0:20] = 1
    instruction = 'turn off 0,0 through 9,9'
    grid.apply(instruction)
    
    print(grid.lights)
    
    # Check on/off pattern correct
    on_coords = ((10,10), (15,15), (0,10), (10,0))
    off_coords = ((0,0), (5,5), (0,9), (9,0))
    
    for coord in on_coords:
        assert grid.lights[coord[1], coord[0]] == 1, coord
    for coord in off_coords:
        assert grid.lights[coord[1], coord[0]] == 0, coord
        
    # Check count
    assert grid.count() == 300
    
    
def test_LEDsim_instruct_switch():
    L = 20
    grid = LEDsimulator.LEDgrid(L)
    grid.lights[0:10, 0:10] = 1
    instruction = 'switch 2,2 through 10,10'
    grid.apply(instruction)
    
    print(grid.lights)
    
    # Check on/off pattern correct
    on_coords = ((0,0), (0,9), (9,0), (10,10))
    off_coords = ((2,2), (2,9), (9,2), (12,12))
    
    for coord in on_coords:
        assert grid.lights[coord[1], coord[0]] == 1, coord
    for coord in off_coords:
        assert grid.lights[coord[1], coord[0]] == 0, coord
        
    # Check count
    assert grid.count() == 20 + 16 + 9 + 8
    
    
def test_LEDsim_instruct_bounds():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    instruction = 'turn on -3,-8 through 15,5'
    grid.apply(instruction)
    
    print(grid.lights)
    
    # Check on/off pattern correct
    on_coords = ((0,0), (5,5), (0,5), (9,0))
    off_coords = ((9,9), (9,6), (0,9), (9,6))
    
    for coord in on_coords:
        assert grid.lights[coord[1], coord[0]] == 1
    for coord in off_coords:
        assert grid.lights[coord[1], coord[0]] == 0
                
    # Check count
    assert grid.count() == 60
    
    
def test_LEDsim_instruct_invertedcoords():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    instruction = 'turn on 8,8 through 1,1'
    grid.apply(instruction)
    
    print(grid.lights)
    
    # Check on/off pattern correct
    on_coords = ((1,1), (5,5), (1,5), (8,1))
    off_coords = ((9,9), (9,0), (0,9), (0,0))
    
    for coord in on_coords:
        assert grid.lights[coord[1], coord[0]] == 1
    for coord in off_coords:
        assert grid.lights[coord[1], coord[0]] == 0
                
    # Check count
    assert grid.count() == 64
    
    
def test_LEDsim_instruct_invalid():
    L = 20
    grid = LEDsimulator.LEDgrid(L)
    # Turn on initial group of lights and count
    grid.lights[0:10, 0:10] = 1
    count_init = grid.count()
    # Apply invalid instructions
    instructions = ['activate 5,5 through 15,15', 'turn off 5,s through 15,15', 'turn on 5,5 to 15,15']
    for instruct in instructions:
        grid.apply(instruct)
    
    print(grid.lights)
    
    # Check on/off pattern correct
    on_coords = ((0,0), (5,5), (0,9), (9,0))
    off_coords = ((10,10), (15,15), (0,10), (10,0))
    
    for coord in on_coords:
        assert grid.lights[coord[1], coord[0]] == 1
    for coord in off_coords:
        assert grid.lights[coord[1], coord[0]] == 0
        
    # Check count has not changed from initial value, i.e. invalid instruction has been ignored
    assert grid.count() == count_init

    
if __name__ == '__main__':
    sys.exit()
