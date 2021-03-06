#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def create_plot():
    df = _read_data()
    _make_plot_file(df)


def _read_data():
    """Read the measurements from speedtest.log and returns a pandas dataframe"""
    df = pd.io.parsers.read_csv(
        '../results/speedtest.log',
        names='date time ping download upload'.split(),
        header=None,
        sep=r'\s+',
        parse_dates={'timestamp': [0, 1]},
    )
    print("Download Max [Mbit/s]:", round(df['download'].max()/1e+6, 2))
    print("Upload Max [Mbit/s]:", round(df['upload'].max()/1e+6, 2))
    print("Download Mean [Mbit/s]:", round(df['download'].mean()/1e+6, 2))
    print("Upload Mean [Mbit/s]:", round(df['upload'].mean()/1e+6, 2))
    print("Download Median [Mbit/s]:", round(df['download'].median()/1e+6, 2))
    print("Upload Median [Mbit/s]:", round(df['upload'].median()/1e+6, 2))
    return df


def _make_plot_file(input):
    """Creates a plot of the download and upload bandwidth"""
    rcParams['xtick.labelsize'] = 'xx-small'
    #  plt.plot(input['timestamp'], input[column].to_numpy())
    plt.title('Bandwidth')
    ax = input.plot(x="timestamp", y="download", legend=False)
    ax2 = ax.twinx()
    input.plot(x="timestamp", y="upload", ax=ax2, legend=False, color="r")
    ax.yaxis.set_view_interval(0, 100000000)
    ax2.yaxis.set_view_interval(0, 100000000)
    ax.figure.legend()
    plt.ylabel('bits/s')
    plt.xlabel('Timestamp')

    plt.grid()

    current_figure = plt.gcf()
    current_figure.subplots_adjust(bottom=.25)
    current_figure.savefig('../results/{}.png'.format('bandwidth'))
