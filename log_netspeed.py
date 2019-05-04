#!/usr/bin/env python

import speedtest
import logging
import time

LOG_FILE = 'speedtest.log'
INTERVALL = 60


def main():
    setup_logging()
    while True:
        ping = download = upload = None
        ping, download, upload = get_results()
        logging.info("%5.1f %5.1f %5.1f", ping, download, upload)
        time.sleep(INTERVALL)


def setup_logging():
    """logger to output results to a file"""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M",
    )


def get_results():
    """Run speedtest with speedtest.py"""
    s = speedtest.Speedtest()
    s.download()
    s.upload()
    return s.results.ping, s.results.download, s.results.upload


if __name__ == '__main__':
    main()
