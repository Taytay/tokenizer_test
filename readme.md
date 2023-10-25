# Tokenizer bug in Transformers 4.34.0?

## Getting started:
1. Create your conda or pipenv environment so you are starting with a blank slate.
2. Run `compare_tokenizers.sh`

## What it does
This will install transformers 4.33.3, and run the script `compare_tokenizers.py` which will show how a string is tokenized with a default tokenizer and a customized version. The customized version is just the google/flan-t5-small with a new character added to the vocab: '\n'
Then it will install transformers 4.34.0 and run the script again.

Conclusion: In 4.34.0, it looks like only the customized tokenizer (where we added a '\n' character) has issues.