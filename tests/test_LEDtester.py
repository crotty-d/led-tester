#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `LEDtester` package."""

import sys
sys.path.append('.')

import pytest
import numpy as np

from click.testing import CliRunner

from LEDtester import LEDsimulator
from LEDtester import cli
from LEDtester import utils

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'LEDtester.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Input URI (file or URL).' in help_result.output
 
def test_parse_file():
    file = "./data/test_data.txt"
    L, instructions = utils.parse_file(file)
    assert L == 10
    assert instructions == ['turn on 0,0 through 9,9', 'turn off 0,0 through 9,9', 'switch 0,0 through 9,9', 'turn off 0,0 through 9,9', 'turn on 2,2 through 7,7']
  
def test_LEDsim_construct():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    print(grid.lights.T)
    
    assert isinstance(grid.lights, np.ndarray)
    assert grid.lights.shape == (L, L)
    assert grid.lights.sum() == 0
    
def test_LEDsim_count():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    print(grid.lights.T)
    assert grid.count() == 0
    
    grid.lights[2:5, 1:3] = 1
    print(grid.lights.T)
    assert grid.count() == 6 

def test_LEDsim_instruct_on():
    L = 20
    grid = LEDsimulator.LEDgrid(L)
    instruction = 'turn on 0,0 through 9,9'
    grid.apply(instruction)
    
    print(grid.lights.T)
    
    # Check on/off pattern correct
    on_coords = ((0,0), (5,5), (0,9), (9,0))
    off_coords = ((10,10), (15,15), (0,10), (10,0))
    
    for coord in on_coords:
        assert grid.lights[coord[0], coord[1]] == 1, coord
    for coord in off_coords:
        assert grid.lights[coord[0], coord[1]] == 0, coord
        
    # Check count
    assert grid.count() == 100
    
def test_LEDsim_instruct_switch(): #FIXME 
    L = 20
    grid = LEDsimulator.LEDgrid(L)
    grid.lights[0:10, 0:10] = 1
    instruction = 'switch 2,2 through 10,10'
    grid.apply(instruction)
    
    print(grid.lights.T)
    
    # Check on/off pattern correct
    on_coords = ((0,0), (0,9), (9,0), (10,10))
    off_coords = ((2,2), (2,9), (9,2), (12,12))
    
    for coord in on_coords:
        assert grid.lights[coord[0], coord[1]] == 1, coord
    for coord in off_coords:
        assert grid.lights[coord[0], coord[1]] == 0, coord
        
    # Check count
    assert grid.count() == 20 + 16 + 9 + 8
    
def test_LEDsim_instruct_bounds():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    instruction = 'turn on 0,0 through 15,5'
    grid.apply(instruction)
    
    print(grid.lights.T)
    
    # Check on/off pattern correct
    on_coords = ((0,0), (5,5), (0,5), (9,0))
    off_coords = ((9,9), (9,6), (0,9), (9,6))
    
    for coord in on_coords:
        assert grid.lights[coord[0], coord[1]] == 1
    for coord in off_coords:
        assert grid.lights[coord[0], coord[1]] == 0
                
    # Check count
    assert grid.count() == 60
    
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
        assert grid.lights[coord[0], coord[1]] == 1
    for coord in off_coords:
        assert grid.lights[coord[0], coord[1]] == 0
        
    # Check count has not changed from initial value, i.e. invalid instruction has been ignored
    assert grid.count() == count_init

    
if __name__ == '__main__':
    sys.exit()
