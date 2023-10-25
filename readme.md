# Tokenizer bug in Transformers 4.34.0?

## Getting started:
1. Create your conda or pipenv environment so you are starting with a blank slate.
2. Run `compare_tokenizers.sh`

## What it does
This will install transformers 4.33.3, and run the script `compare_tokenizers.py` which will show how a string is tokenized with a default tokenizer and a customized version. The customized version is just the google/flan-t5-small with a new character added to the vocab: '\n'
Then it will install transformers 4.34.1 and run the script again.

Conclusion: In 4.34.1, it looks like only the customized tokenizer (where we added a '\n' character in the tokenizer that was saved to disk) has issues when loaded from disk.
Otherwise, the behavior of the tokenizers (fast and slow) is the same in both versions.

## Output

Here's what I see when I run it:
```
❯ ./compare_tokenizers.sh
Installing transformers 4.33.3
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.


########################
Transformers version:  4.33.3
Here are all of the tests with the SLOW tokenizer:

#######
Testing tokenizer for model, ./custom_tokenizer. use_fast_tokenizer = False.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '\n', '▁This', '▁is', '▁another', '▁line', '.', '\n', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 32100, 100, 19, 430, 689, 5, 32100, 275, 2031, 8, 1025, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = False.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '▁This', '▁is', '▁another', '▁line', '.', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 100, 19, 430, 689, 5, 275, 2031, 8, 1025, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = False.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = True
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', ' ', '▁is', ' ', '▁', 'a', ' ', '▁test', ' ', '▁string', '.', ' ', '▁This', ' ', '▁is', ' ', '▁another', ' ', '▁line', '.', ' ', '▁And', ' ', '▁finally', ' ', '▁the', ' ', '▁third', ' ', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 32100, 19, 32100, 3, 9, 32100, 794, 32100, 6108, 5, 32100, 100, 32100, 19, 32100, 430, 32100, 689, 5, 32100, 275, 32100, 2031, 32100, 8, 32100, 1025, 32100, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = False.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = False
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '\n', '▁This', '▁is', '▁another', '▁line', '.', '\n', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 32100, 100, 19, 430, 689, 5, 32100, 275, 2031, 8, 1025, 689, 5, 1]
Here are all of the tests with the FAST tokenizer:

#######
Testing tokenizer for model, ./custom_tokenizer. use_fast_tokenizer = True.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '\n', '▁This', '▁is', '▁another', '▁line', '.', '\n', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 32100, 100, 19, 430, 689, 5, 32100, 275, 2031, 8, 1025, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = True.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '▁This', '▁is', '▁another', '▁line', '.', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 100, 19, 430, 689, 5, 275, 2031, 8, 1025, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = True.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = True
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', ' ', '▁is', ' ', '▁', 'a', ' ', '▁test', ' ', '▁string', '.', ' ', '▁This', ' ', '▁is', ' ', '▁another', ' ', '▁line', '.', ' ', '▁And', ' ', '▁finally', ' ', '▁the', ' ', '▁third', ' ', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 32100, 19, 32100, 3, 9, 32100, 794, 32100, 6108, 5, 32100, 100, 32100, 19, 32100, 430, 32100, 689, 5, 32100, 275, 32100, 2031, 32100, 8, 32100, 1025, 32100, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = True.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = False
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '\n', '▁This', '▁is', '▁another', '▁line', '.', '\n', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 32100, 100, 19, 430, 689, 5, 32100, 275, 2031, 8, 1025, 689, 5, 1]





Installing transformers 4.34.1
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.


########################
Transformers version:  4.34.1
Here are all of the tests with the SLOW tokenizer:

#######
Testing tokenizer for model, ./custom_tokenizer. use_fast_tokenizer = False.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', ' ', '▁is', ' ', '▁', 'a', ' ', '▁test', ' ', '▁string', '.', '\n', '▁This', ' ', '▁is', ' ', '▁another', ' ', '▁line', '.', '\n', '▁And', ' ', '▁finally', ' ', '▁the', ' ', '▁third', ' ', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 32100, 19, 32100, 3, 9, 32100, 794, 32100, 6108, 5, 32100, 100, 32100, 19, 32100, 430, 32100, 689, 5, 32100, 275, 32100, 2031, 32100, 8, 32100, 1025, 32100, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = False.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '▁This', '▁is', '▁another', '▁line', '.', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 100, 19, 430, 689, 5, 275, 2031, 8, 1025, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = False.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = True
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', ' ', '▁is', ' ', '▁', 'a', ' ', '▁test', ' ', '▁string', '.', ' ', '▁This', ' ', '▁is', ' ', '▁another', ' ', '▁line', '.', ' ', '▁And', ' ', '▁finally', ' ', '▁the', ' ', '▁third', ' ', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 32100, 19, 32100, 3, 9, 32100, 794, 32100, 6108, 5, 32100, 100, 32100, 19, 32100, 430, 32100, 689, 5, 32100, 275, 32100, 2031, 32100, 8, 32100, 1025, 32100, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = False.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = False
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '\n', '▁This', '▁is', '▁another', '▁line', '.', '\n', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 32100, 100, 19, 430, 689, 5, 32100, 275, 2031, 8, 1025, 689, 5, 1]
Here are all of the tests with the FAST tokenizer:

#######
Testing tokenizer for model, ./custom_tokenizer. use_fast_tokenizer = True.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', ' ', '▁is', ' ', '▁', 'a', ' ', '▁test', ' ', '▁string', '.', '\n', '▁This', ' ', '▁is', ' ', '▁another', ' ', '▁line', '.', '\n', '▁And', ' ', '▁finally', ' ', '▁the', ' ', '▁third', ' ', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 32100, 19, 32100, 3, 9, 32100, 794, 32100, 6108, 5, 32100, 100, 32100, 19, 32100, 430, 32100, 689, 5, 32100, 275, 32100, 2031, 32100, 8, 32100, 1025, 32100, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = True.
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '▁This', '▁is', '▁another', '▁line', '.', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 100, 19, 430, 689, 5, 275, 2031, 8, 1025, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = True.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = True
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', ' ', '▁is', ' ', '▁', 'a', ' ', '▁test', ' ', '▁string', '.', ' ', '▁This', ' ', '▁is', ' ', '▁another', ' ', '▁line', '.', ' ', '▁And', ' ', '▁finally', ' ', '▁the', ' ', '▁third', ' ', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 32100, 19, 32100, 3, 9, 32100, 794, 32100, 6108, 5, 32100, 100, 32100, 19, 32100, 430, 32100, 689, 5, 32100, 275, 32100, 2031, 32100, 8, 32100, 1025, 32100, 689, 5, 1]

#######
Testing tokenizer for model, google/flan-t5-small. use_fast_tokenizer = True.
Will add the following tokens to it: ['\n'], and normalized_added_tokens = False
Tokenizing the following string: """This is a test string.
This is another line.
And finally the third line."""
The tokenized (str) version of the string is:  ['▁This', '▁is', '▁', 'a', '▁test', '▁string', '.', '\n', '▁This', '▁is', '▁another', '▁line', '.', '\n', '▁And', '▁finally', '▁the', '▁third', '▁line', '.']
The tokenized (ints) version of the string is:  [100, 19, 3, 9, 794, 6108, 5, 32100, 100, 19, 430, 689, 5, 32100, 275, 2031, 8, 1025, 689, 5, 1]

```