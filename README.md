[![Python](https://img.shields.io/pypi/pyversions/textra.svg)](https://badge.fury.io/py/textra)
[![PyPI](https://badge.fury.io/py/textra.svg)](https://badge.fury.io/py/textra)

# @TexTra
Machine translation for Everyone

# Install

```bash
pip install textra
```

# Usage

```bash
$ trans --help
usage: trans [-h] [--name NAME] [--key KEY] [--secret SECRET] [-s SOURCE] [-t TARGET] text

positional arguments:
  text

options:
  -h, --help            show this help message and exit
  --name NAME           login id
  --key KEY
  --secret SECRET
  -s SOURCE, --source SOURCE
  -t TARGET, --target TARGET
```

# Examples

```bash
$ trans 'I am God. You are Dog.'
私は神だお前は犬だ
```

```bash
$ trans -s ja -t en 吾輩は猫である
I am the cat
```

You can get the key and secret from here.

![image](https://user-images.githubusercontent.com/12811398/186966682-5a563423-fbe2-4f3f-aa09-4a274ac0e778.png)
