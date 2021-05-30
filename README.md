# CSCI926-Project

## Prerequisites

- python
- virtualenv
- git
- selenium webdriver
- node


## Setup 
If you seting up for the first time, then pull the  notebook submodule first. 
```
git submodule update --init --recursive
```

The jupyter devleoper  has provide a well documented guideline .Please follow this for inital setup. Note : virtualenv  recommended
https://jupyter-notebook.readthedocs.io/en/stable/contributing.html

```
cd notebook
pip install -e .
pip install -e '.[test]'
pip install pynguin
```

## Pynguin Test Case
For generating the automated test case, use pynguin application. See the setup for the installation.

```
pynguin --algorithm WHOLE_SUITE --project_path notebook/notebook  --output_path test_gen_whole --module_name _tz

pynguin --algorithm RANDOM --project_path notebook/notebook  --output_path test_gen_ran --module_name _tz
```

## Run Test Case
To run the test cases, go to the test folder and run pytest.

```
cd tests
pytest
```

## PyTest and Seleinum Guide

- https://docs.pytest.org/en/6.2.x/contents.html
- https://selenium-python.readthedocs.io/

Note : conftest.py source code is used for initalization and derived from the notebook repo.

## Contributing Guide

- Please keep the generated test files separate
- New test case should be added in tests folder 