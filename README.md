# pdftotext

[![PyPI](https://img.shields.io/pypi/v/pdftotext.svg)](https://pypi.python.org/pypi/pdftotext)
[![Downloads](https://pepy.tech/badge/pdftotext)](https://pepy.tech/project/pdftotext)

Simple PDF text extraction

```python
import pdftotext

# Load your PDF
with open("lorem_ipsum.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
with open("secure.pdf", "rb") as f:
    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

# Read some individual pages
print(pdf[0])
print(pdf[1])

# Read all the text into one string
print("\n\n".join(pdf))
```


## OS Dependencies

These instructions assume you're on a recent OS. Package names may differ for an
older OS.

### Debian, Ubuntu, and friends

```
sudo apt install build-essential libpoppler-cpp-dev python3-dev
```

### Fedora, Red Hat, and friends

```
sudo yum install gcc-c++ poppler-cpp-devel python3-devel
```

### macOS

```
brew install poppler python
```


## Install

```
pip install pdftotext
```
