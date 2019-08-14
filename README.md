# smartbear-hands-on-ui-testing-python
This repository contains the example test project
for the **Hands-On Web UI Testing with Python** webinar
delivered by *SmartBear* in collaboration with *Automation Panda*
on August 14, 2019.
The webinar slides are saved in this repository as `webinar-slides.pdf`.

## Setup
This project requires Python 3.

To set up the Python environment and install dependencies, run:

    > pip install pipenv
    > pipenv install

## Running Tests
You will need a CrossBrowserTesting license to run the tests in this project.
You can obtain a trial license from https://crossbrowsertesting.com/.
Add your username and authentication key to `cbt_config.json`.

To run tests, run the following command from the project's root directory:

    > pipenv run python -m pytest

The terminal will print the pytest banner.
Be patient - tests may take a few seconds to complete.
You can also check results on the CrossBrowserTesting website.

## Additional Resources

* [CrossBrowserTesting](https://crossbrowsertesting.com/) website
* [Automation Panda](https://www.automationpanda.com/) blog
* [Hands-On Web UI Testing](https://github.com/AndyLPK247/pyohio-2019-web-ui-testing) PyOhio 2019 tutorial
* [Test Automation University](https://testautomationu.applitools.com/) courses
  * [Web Element Locator Strategies](https://testautomationu.applitools.com/web-element-locator-strategies/)
  * [Behavior Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)
