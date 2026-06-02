<!-- omit in toc -->
# Regina Normalizer

![Version](https://img.shields.io/badge/Version-T9-darkviolet)
![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)
![CI Status](https://img.shields.io/badge/CI-[unavailable]-red)
![Docker](https://img.shields.io/badge/Docker-[unavailable]-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

Regina is a tool for normalization of Icelandic text in preparation for conversion to speech. Normalization involves converting numbers,
dates, ordinals, etc. into fully spelled-out alphabetic words.

## Overview

This repository was created at Reykjavík University and is
part of the [Icelandic Language Technology Programme](https://github.com/icelandic-lt/icelandic-lt).

- **Category:** [TTS](https://github.com/icelandic-lt/icelandic-lt/blob/main/doc/tts.md)
- **Domain:** Server
- **Languages:** Python 3.10+ (requires Rust for IceBERT-PoS build on some platforms)
- **Audience**: Developers, Researchers
- **License**: MIT
- **Origins:** [regina_normalizer](https://github.com/cadia-lvl/regina_normalizer)

## Status
![Installable](https://img.shields.io/badge/Installable-green)

The package installs with `pip install .` and includes all required dependencies for full normalization.

## System Requirements
- Python 3.10+

## Quickstart

Install the package:

`pip install .`

Import the normalizer:

`python -c "from regina_normalizer import normalizer; print(normalizer.input_string('Leikurinn fór 2-2 fyrir KR.', 'sport'))"`

## Troubleshooting

- Installation requires Python 3.10+ and may require Rust to be available on your system for building the IceBERT-PoS dependency.
- On Apple Silicon (M1/M2/arm64), ensure you have a compatible Rust toolchain installed (`rustup` or Homebrew).
- If installation fails due to Rust/build issues, verify your build tools are up to date or use a pre-built wheel environment.

## Installation

```bash
pip install .
```

## Usage

```python
from regina_normalizer import normalizer

print(normalizer.input_string("Leikurinn fór 2-2 fyrir KR.", "sport"))
```

```python
normalizer.input_file("input.txt", "output.txt", "other")
```

Valid domains:
- `other`
- `sport`




