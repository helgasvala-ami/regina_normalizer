# abn pkg
#!/usr/bin/env python3

from __future__ import annotations
import sys
from typing import List, Optional

from regina_normalizer import tokenizer
from regina_normalizer import abbr_functions as af
from regina_normalizer import number_functions as nf

DEFAULT_TOKENIZER = tokenizer.Tokenizer()

def input_string(text_string: str, domain: str) -> str:
    tok = DEFAULT_TOKENIZER
    sentences = tok.detect_sentences(text_string)
    normalized = []
    for sent in sentences:
        abbr_sent = af.replace_abbreviations(sent, domain)
        normalized.append(nf.handle_sentence(abbr_sent, domain))
    final_string = ' '.join(normalized)
    #print(final_string)
    return final_string

def input_file(input_file: str, output_file: str, domain: str) -> None:
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    tok = DEFAULT_TOKENIZER
    sentences = tok.detect_sentences(' '.join(lines))
    normalized = []
    for sent in sentences:
        abbr_sent = af.replace_abbreviations(sent, domain)
        normalized.append(nf.handle_sentence(abbr_sent, domain))
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in normalized:
            f.write(f"{item}\n")


def main(argv: Optional[List[str]] = None) -> None:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) == 2:
        print(input_string(args[0], args[1]))
    elif len(args) == 3:
        input_file(args[0], args[1], args[2])
        print("Done writing output file!")
    else:
        print(
            "\nERROR MESSAGE\n\n"
            "For command line, use: python3 -m regina_normalizer <string-to-be-normalized> <domain>\n"
            "For a text file, use: python3 -m regina_normalizer <input-file> <output-file> <domain>\n"
            "{domain} can be 'sport' or 'other'\n"
        )


if __name__ == '__main__':
    main()