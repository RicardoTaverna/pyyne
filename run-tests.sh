#!/bin/sh

echo "Running docstyle code check."
python -m pydocstyle main.py

echo ""

echo "Runnig code quality tests"
python -m pycodestyle --config=.pycodestyle  main.py
python -m pycodestyle --config=.pycodestyle  pyynechallengebank
python -m mypy main.py

echo ""

echo "Running python unittest."
python -m unittest -v ./tests/adapter_test.py