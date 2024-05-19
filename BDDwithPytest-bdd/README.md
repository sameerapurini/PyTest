
# BDD Cucumber automation tests Python Based selenium project for api and Web testing
This is an automation project for testing using using `pytest` and `pytest-bdd`


### Prerequisites
The following tool are needed run the tests:
  - Chrome Web Browser and compatible ChromeDriver
  - Python 3
  - pipenv
  - pytest
    
## Installation Steps:

In order to get the tests to run locally, you need to install the following software.
    1. pipenv install
    2. pip install chromedriver-py
    3. pip install termcolor 

###### NOTE: All commands shall be executed from Automation Project root directory: `../[PROJECT_DIR]/tests/`

#### MacOS

- Install [Homebrew](https://brew.sh/) with `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Install [Pyenv](https://formulae.brew.sh/formula/pyenv) with `brew install pyenv`, this is a python version manager.
- Add the following to `~/.bash_profile`

```
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    export PATH="$PYENV_ROOT/shims:$PATH"
    export PATH="$PYENV_ROOT/completions/pyenv.bash:$PATH"
```
Install the following,

  1. Install python 3.8.13 with `pyenv install 3.8.13`
  2. Set python version 3.8.13 to be used globally with `pyenv global 3.8.13`
  3. Install all project dependencies with `pip install -r requirements.txt --use-pep517`
  4. Check the python version used with `which python`

### Test Execution
- [Fork](https://github.com/ashikkumar23/gherkin-bdd-api-test-framework/fork) the repository `bdd-gherkin-api-test-automation-framework`
- Clone the repository via HTTPS `git clone https://github.com/<your_github_username>/bdd-gherkin-api-test-automation-framework.git` or via SSH `git clone git@github.com:<your_github_username>/bdd-gherkin-api-test-automation-framework.git`
- Open [Pycharm](https://www.jetbrains.com/pycharm/) (or any IDE) > File > Open > Open the project where the repository is located (i.e., `../bdd-gherkin-test-automation-framework/tests`)
- Run the command: **pytest** in `Terminal`

## Pycharm Edit Configuration:

- Go to `Edit Configurations...`
- Add `New Configuration` (`+` sign) > `Python tests` > `pytest`
- Provide `Target Script path` and `Working directory` (i.e., `../bdd-gherkin-test-automation-framework/tests`)
- Select the required `Python interpreter`
- And, `Additional Arguments`: `-v --gherkin-terminal-reporter --reruns 1 --reruns-delay 1 --tags="automated" --color="yes"`
