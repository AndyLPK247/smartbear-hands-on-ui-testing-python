"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
Warning: the SEARCH_INPUT locator had to be updated because the page changed!
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
  
  # Locators

  SEARCH_INPUT = (By.ID, 'search_form_input')

  @classmethod
  def PHRASE_RESULTS(cls, phrase):
    xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
    return (By.XPATH, xpath)

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def result_count_for_phrase(self, phrase):
    results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
    return len(results)
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    return search_input.get_attribute('value')

  def title(self):
    return self.browser.title
