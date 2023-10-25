#!/usr/bin/env python3
# %%

from transformers import (AutoTokenizer, PreTrainedTokenizerBase)
import transformers
from tokenizers import AddedToken
from typing import List

transformers_version = transformers.__version__
print("\n\n########################")
print("Transformers version: ", transformers_version)

def load_tokenizer(model_path:str, use_fast_tokenizer:bool)->PreTrainedTokenizerBase:
    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
                model_path,
                use_fast_tokenizer=use_fast_tokenizer,
                local_files_only=False,
                trust_remote_code=True,
            )
    
    return tokenizer


def test_tokenizer(model_path:str, use_fast_tokenizer:bool, tokens_to_add:List[str] = [], normalized_added_tokens:bool = False):
    print("\n#######")
    print(f"Testing tokenizer for model, {model_path}. use_fast_tokenizer = {use_fast_tokenizer}.")
    if not(tokens_to_add is None or len(tokens_to_add) == 0):
        print(f"Will add the following tokens to it: {tokens_to_add}, and normalized_added_tokens = {normalized_added_tokens}")

    tokenizer: PreTrainedTokenizerBase = load_tokenizer(model_path, use_fast_tokenizer=use_fast_tokenizer)

    for new_token in tokens_to_add:
        if normalized_added_tokens:
            tokenizer.add_tokens(AddedToken(new_token, normalized=True))    
        else:
            tokenizer.add_tokens(AddedToken(new_token, normalized=False))
        #tokenizer.add_tokens(new_token)
        # This also fails:
        

    tokenizer_test_string = "This is a test string.\nThis is another line.\nAnd finally the third line."
    tokens = tokenizer(tokenizer_test_string)
    str_tokens = tokenizer.tokenize(tokenizer_test_string)
    print(f"Tokenizing the following string: \"\"\"{tokenizer_test_string}\"\"\"")
    print("The tokenized (str) version of the string is: ", str_tokens)
    print("The tokenized (ints) version of the string is: ", tokens['input_ids'])

# This custom tokenizer was just the flan-t5-small tokenizer with a \n added to it like this: `tokenizer.add_tokens(AddedToken('\n', normalized=False))`

print("Here are all of the tests with the SLOW tokenizer:")
test_tokenizer("./custom_tokenizer", use_fast_tokenizer=False)
test_tokenizer("google/flan-t5-small", use_fast_tokenizer=False)
test_tokenizer("google/flan-t5-small", use_fast_tokenizer=False, tokens_to_add=['\n'], normalized_added_tokens=True)
test_tokenizer("google/flan-t5-small", use_fast_tokenizer=False, tokens_to_add=['\n'], normalized_added_tokens=False)

print("Here are all of the tests with the FAST tokenizer:")
test_tokenizer("./custom_tokenizer", use_fast_tokenizer=True)
test_tokenizer("google/flan-t5-small", use_fast_tokenizer=True)
test_tokenizer("google/flan-t5-small", use_fast_tokenizer=True, tokens_to_add=['\n'], normalized_added_tokens=True)
test_tokenizer("google/flan-t5-small", use_fast_tokenizer=True, tokens_to_add=['\n'], normalized_added_tokens=False)

print("\n\n\n")