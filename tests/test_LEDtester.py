#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `LEDtester` package."""

import os
import sys
sys.path.append('.')

import pytest

from click.testing import CliRunner

from LEDtester import LEDtester #TODO: Maybe avoid naming module and package same name, LEDtester?
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
 
def test_file_parse():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile) # FIXME
    assert N is not None
    
if __name__ == '__main__':
    print(os.getcwd())
