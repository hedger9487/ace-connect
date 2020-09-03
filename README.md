# Ace-connect

> This is a temporary repository, it should be deprecated as upstream. This repository is for the backend of a friends website

# Git clone 

```bash
git clone --recurse-submodule <url> <name>
```

## Environment requirements

Please setup `python >= 3.7`, `pip` and the listing below. Other versions might work but aren't tested.

### Virtual environments

Setting up the virtual environment for python. We have chosen to use `venv` instead of other virtual environment tools for reasons stated [from the official documentations](https://docs.python.org/3/library/venv.html)  

```bash
# Replace all instances of <venv> with /path/to/directory
python3 -m venv <venv>

# POSIX compliant
source <venv>/bin/activate

# DOS compliant
<venv>\Scripts\activate.bat
```

### SWI-Prolog

The libraries of the `ape.exe` file may require the libraries of [SWI-Prolog](https://www.swi-prolog.org/) go and download it. Or if you're on Linux, you could search on your package manager. 

### Python packages

```bash
pip install pyswip
```
### APE - ACE Parsing Engine

You would probably need to recompile the `ape.exe` file. Go to [their Github Page](https://github.com/Attempto/APE) clone it or you could use the submodule provided in this repository and run 

```bash
# POSIX compliant
cd APE
make install
mv ape.exe ..
cd ..
```

## Execution

```bash
python3 translator.py
```

This would make the translator app input the natural language text file, `nl.txt ` and turn it into a OWL/XML format of output `text.owl`.

## Known issues

1. On RHEL-based OS, the `swi-prolog` binaries might be in a different place and with different commands. Would recommend you to recompile the source binaries.