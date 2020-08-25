# Ace-connect

> This is a temporary repository, it should be deprecated as upstream. This repository is for the backend of a friends website

## Environment requirements

Please setup `python >= 3.7`, `pip` and the listing below. Other versions "might" work but aren't tested.

### Virtual environments

Setting up the virtual environment for python. We have chosen to use `venv` instead of other virtual environment tools for reasons stated [from the official documentations](https://docs.python.org/3/library/venv.html)  

```bash
python3 -m venv .

# Replace all instances of <venv> with /path/to/directory
# POSIX compliant
source <venv>/bin/activate
# DOS compliant
<venv>\Scripts\activate.bat
```

## Execution

```bash
python3 translator.py
```

This would make the translator app take the natural language text file, `nl.txt ` and turn it into a OWL/XML format of `text.owl`.