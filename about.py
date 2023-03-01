"""
This file provides standard information to
help with debugging.

This file named: about.py
This module is named: about
    print(get_header(_file_))
To learn more, search:
    builtin attributes python
"""

#imports
import datetime
import os
import platform
import sys

data_folder = ""
divider = "==============================================="
def get_source_directory_path():
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir

def get_data_directory_path():
    datapath = os.sep.join([os.getcwd(), data_folder])
    return datapath

def get_data_file_path(fn):
    dir = get_data_directory_path()
    fullPath = os.sep.join([dir, fn])
    return fullPath

def get_header(fn):
    """This function prints out helful information about a file"""
    return f"""

{divider}
{divider}

Welcome!

It's {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}

This file is running on: {os.name} {platform.system()} {platform.release()}

This Python version is: {platform.python_version()}

The Python interpreter is at:
{sys.executable}

The active enviroment should be either conda or pip (one should be None):
    Active conda env is: {os.environ.get('CONDA_DEFAULT_ENV') }
    Active pip env is:   {os.environ.get('PIP_DEFAULT_ENV')}

The path to the active virtual enviroment is:
{sys.prefix}

The Current Working Directory (CWD) where this command was launched is:

{os.getcwd()}

The absolute path to the data directory is:
{get_source_directory_path()}

{fn}

{divider}
{divider}
"""
print(get_header(__file__))

print_to_file = True

if print_to_file:
    fn = "about.text"
with open (fn, "w") as f:
    f.write(get_header(__file__))

