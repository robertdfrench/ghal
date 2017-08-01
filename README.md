[![Build Status](https://travis-ci.org/robertdfrench/ghal.svg?branch=master)](https://travis-ci.org/robertdfrench/ghal)
# Ghal
Githost Abstraction Layer

## Installation

```bash
pip install ghal
```

## Usage

```python
import ghal

githost = ghal.connect("robertdfrench@github.com", "API_KEY_HERE")
spack = githost.get_project("LLNL/spack")

print("## Spack bugs")
for issue in spack.get_issues(label="bug"):
    print("* %s" % issue.title)
```
