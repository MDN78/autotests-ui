# UI Course Automation Tests

This project implements automated tests for
the [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login). The
tests are written using **Python**, **Pytest**, **Allure** and **Playwright**. The test application’s source code is
available
on [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Stack

<p  align="left">
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="playwright" src="https://github.com/MDN78/MDN78/blob/main/assets/playwright_2.png"></code>  
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
</p>

## Project Overview

The goal of this project is to automate the testing of the UI Course application. The automated tests verify various
functionalities of the application to ensure its stability and correctness. The project structure follows best practices
for organizing test code with clear, maintainable scripts and based on patterns: `Page Object`, `Page Component` ,
`Page Factory`.
Project use new library for tracking and visualizing UI test coverage — directly on your actual application, not static
snapshots.

[Install library](https://pypi.org/project/ui-coverage-tool/)   
[Official docs](https://github.com/Nikita-Filonov/ui-coverage-tool)

#### Project features:
* Pydantic
* Playwright trace viewer
* Logging
* CI / CD process
* Pytest-xdist - distributing tests across multiple CPUs to speed up test execution

Supported browsers:

| Chrome | Firefox | Webkit |
|--------|---------|--------|

Change parameter in `.env` to activate all browsers:
```dotenv
BROWSERS=["chromium","firefox","webkit"]

```


## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/MDN78/autotests-ui
cd autotests-ui
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Additional Playwright Setup (if needed)

If you're running Playwright for the first time, you might need to install the required browsers:

```bash
playwright install
```

### Running the Tests with Allure Report Generation

Tests blocks:

 - [x] Authentication
    * authorization
    * registration
- [x] Courses
    * Create course
    * edit course
- [x] Dashboard

To run the tests and generate an Allure report, use the following command:

```bash
pytest -m "regression"
```

This will execute all tests in the project and display the results in the terminal.

### Viewing the Allure Report

After the tests have been executed, you can generate and view the Allure report with:

```bash
allure serve
```

This command will open the Allure report in your default web browser.
