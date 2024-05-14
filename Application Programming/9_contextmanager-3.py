"""
3. Give a Try - Run a System Command  using Popen utility of subprocess module

- Define a function "run_process", which accepts a system command, runs the command at the backgroun, and retruns the results.
-Hint: Use "Popen" utility in "subprocess" module to run a system command.
-Hint: Use "with" along with "Popen" 
"""

import sys
import os
import subprocess
import inspect


# Complete the function below.


def run_process(cmd_args):
    with subprocess.Popen(
        cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ) as process:
        stdout, stderr = process.communicate()
        return stdout
