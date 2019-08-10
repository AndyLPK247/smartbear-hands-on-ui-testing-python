"""
This module contains shared fixtures.
"""

import json
import pytest
import requests
import selenium.webdriver


# ----------------------------------------------------------------------
# Fixture: Read the CrossBrowserTesting config file
# ----------------------------------------------------------------------

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


# ----------------------------------------------------------------------
# Fixture: Create the WebDriver instance
# ----------------------------------------------------------------------

@pytest.fixture
def browser(cbt_config, request):

  # Concatenate the URL
  username = cbt_config['authentication']['username'].replace('@', '%40')
  key = cbt_config['authentication']['key']
  url = f"http://{username}:{key}@hub.crossbrowsertesting.com:80/wd/hub"

  # Request a remote browser from CrossBrowserTesting
  caps = cbt_config['webdriver']
  caps['name'] += ' | ' + request.node.name
  b = selenium.webdriver.Remote(desired_capabilities=caps, command_executor=url)

  # Make its calls wait up to 30 seconds for elements to appear
  b.implicitly_wait(30)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()


# ----------------------------------------------------------------------
# Hook + Fixture: Upload extra info to CrossBrowserTesting
# ----------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

  # Expose the test result to the request
  outcome = yield
  setattr(item, 'test_result', outcome.get_result())


@pytest.fixture
def cbt_uploader(cbt_config, browser, request):
  URL = 'https://crossbrowsertesting.com/api/v3'

  # Get config data
  username = cbt_config['authentication']['username']
  key = cbt_config['authentication']['key']

  # Create the uploader
  uploader = requests.Session()
  uploader.auth = (username, key)

  # Start recording the video
  response = uploader.post(f'{URL}/selenium/{browser.session_id}/videos')
  video_hash = response.json()['hash']
  
  # Let the test run
  yield

  # Stop recording the video
  uploader.delete(f'{URL}/selenium/{browser.session_id}/videos/{video_hash}')
  
  # Determine the score
  score = 'fail' if request.node.test_result.failed else 'pass'

  # Post the test result
  uploader.put(
    f'{URL}/selenium/{browser.session_id}',
    data={'action': 'set_score', 'score': score})
