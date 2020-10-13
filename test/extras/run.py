#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2020 Snowflake Computing Inc. All right reserved.
#

# This script run every Python file in this directory other than this one in a subprocess
# and checks their exit codes

import pathlib
import subprocess
import sys

import psutil


def print_debug_info() -> None:
    p = psutil.Process()  # Get current process
    print("Full path: {}".format(sys.path))
    print("Current process information\nPID: {}\nName: {}".format(p.pid, p.name()))
    print("Cmdline: {}".format(' '.join(p.cmdline())))


def run_tests() -> None:
    file_ignore_list = ['run.py', '__init__.py']
    for test_file in pathlib.Path(__file__).parent.glob('*.py'):
        if test_file.name not in file_ignore_list:
            print("Running {}".format(test_file))
            sub_process = subprocess.run(['python', str(test_file)])
            sub_process.check_returncode()


def main(_print_debug_info: bool = False):
    if _print_debug_info:
        print_debug_info()
    run_tests()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(prog="run_extra_tests")
    parser.add_argument("--debug", action='store_true')
    options = parser.parse_args()
    main(options.debug)
