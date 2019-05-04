#!/usr/bin/env python
import argparse
from log_netspeed import start_testing
from read_logdata import create_plot


def main():
    args = _parse_args()
    if args.cmd ==  'test':
        start_testing()
    if args.cmd == 'plot':
        create_plot()


def _parse_args():
    """Parse commandline arguments
    Returns:
        args
    """
    parser = argparse.ArgumentParser(description='Measure and visualize internet bandwidth')
    parser.add_argument("--cmd", help="'test' or 'plot'", dest="cmd")
    return parser.parse_args()


if __name__ == '__main__':
    main()
