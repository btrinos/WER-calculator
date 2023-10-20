# WER-calculator
Word Error Rate (WER) Calculator

# Word Error Rate (WER) Calculator

This project provides a Python-based tool for computing the Word Error Rate (WER) between two texts. WER is a common metric used to measure the performance of speech recognition, machine translation, and other systems that produce sequences of words. It represents the ratio of the number of insertions, deletions, and substitutions to the number of words in the reference.

## Overview

The main function, `wer(reference, hypothesis)`, calculates the WER between the `reference` and `hypothesis` texts. The computation is based on dynamic programming, and the algorithm used is similar to the one used for calculating the Levenshtein distance (or edit distance) between two sequences.

## Installation

1. Clone the repository:

```
git clone https://github.com/btrinos/wer-calculator.git
```

2. Change to the project directory:

```
cd wer-calculator
```

3. No external libraries are required, so you're good to go!

## Usage

The script currently reads two text files: `d1.txt` as the reference text and `d2.txt` as the hypothesis text. Ensure these files are present in the specified location or modify the paths accordingly.

Run the script:

```
python wer_calculator.py
```

The script will output the Word Error Rate (WER) between the texts in the two files, formatted as a percentage.

## Example

Given the following reference and hypothesis:

**Reference:** "This is a test"
**Hypothesis:** "This is test"

The script will output:

```
Word Error Rate (WER): 25.00%
```

This is because one word ("a") is missing from the hypothesis, making the WER 1/4 = 25%.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Any contributions, whether it's refining the algorithm, improving documentation, or adding features, are highly appreciated!

## License

This project is licensed under the MIT License. See `LICENSE` for more information.

---
