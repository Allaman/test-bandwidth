#!/usr/bin/env python

import speedtest
import logging
import time

LOG_FILE = '/results/speedtest.log'
INTERVALL = 60


def start_testing():
    """Infinite loop executing speedtest every $INTERVAL"""
    _setup_logging()
    while True:
        ping = download = upload = None
        ping, download, upload = _get_results()
        logging.info("%5.1f %5.1f %5.1f", ping, download, upload)
        print("Waiting for next measurement...")
        time.sleep(INTERVALL)


def _setup_logging():
    """logger to output results to a file"""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M",
    )


def _get_results():
    """Run speedtest with speedtest.py"""
    s = speedtest.Speedtest()
    print("Testing download..")
    s.download()
    print("Testing upload..")
    s.upload()
    return s.results.ping, s.results.download, s.results.upload
