#!/usr/bin/env python3
# %%

from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer, PreTrainedTokenizerBase)
import transformers

transformers_version = transformers.__version__
print("Transformers version: ", transformers_version)

def test_tokenizer(model_path:str):
    print("")
    print("Testing tokenizer for model: ", model_path)
    print("Loading tokenizer from model path: ", model_path)
    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
                model_path,
                use_fast=True,
                local_files_only=False,
                trust_remote_code=True,
            )

    tokenizer_test_string = "This is a test string.\nThis is another line.\nAnd finally the third line."
    tokens = tokenizer(tokenizer_test_string)
    str_tokens = tokenizer.tokenize(tokenizer_test_string)
    print(f"Tokenizing the following string: \"\"\"{tokenizer_test_string}\"\"\"")
    print("The tokenized (str) version of the string is: ", str_tokens)
    print("The tokenized (ints) version of the string is: ", tokens['input_ids'])

test_tokenizer("./custom_tokenizer")
test_tokenizer("google/flan-t5-small")