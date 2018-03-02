#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `LEDtester` package."""

#ximport os
import sys
sys.path.append('.')

import pytest

from click.testing import CliRunner

from LEDtester import LEDsimulator
from LEDtester import cli
from LEDtester import utils


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'LEDtester.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
 
def test_file_parse(): # TODO possibly add @fixture and input to test_LEDtester? Independence?
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None
    # TODO assert instructions content
    
# TODO def test_LEDsimulator():

    
if __name__ == '__main__':
    sys.exit()
    #xprint(os.getcwd())
