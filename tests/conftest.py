"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def cbt_config(scope='session'):

  # Read the config file
  with open('cbt_config.json') as config_file:
    config = json.load(config_file)
  
  # Verify authentication config
  assert 'authentication' in config
  assert 'username' in config['authentication']
  assert 'key' in config['authentication']

  # Verify webdriver config
  assert 'webdriver' in config
  assert 'name' in config['webdriver']
  assert 'browserName' in config['webdriver']
  assert 'platform' in config['webdriver']

  # Return the config data
  return config


@pytest.fixture
def browser(cbt_config):

  # Concatenate the URL
  username = cbt_config['authentication']['username']
  key = cbt_config['authentication']['key']
  url = f"http://{username}:{key}@hub.crossbrowsertesting.com:80/wd/hub"

  # Request a remote browser from CrossBrowserTesting
  caps = cbt_config['webdriver']
  b = selenium.webdriver.Remote(desired_capabilities=caps, command_executor=url)

  # Make its calls wait up to 30 seconds for elements to appear
  b.implicitly_wait(30)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
