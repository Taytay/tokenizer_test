#!/bin/bash

set -e

echo "Installing transformers 4.33.3"
pip install -q -r ./requirements-transformers-4.33.3.txt
./tokenizer_test.py

echo ""

echo "Installing transformers 4.34.1"
pip install -q -r ./requirements-transformers-4.34.1.txt
./tokenizer_test.py