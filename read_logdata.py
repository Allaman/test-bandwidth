#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def main():
    create_plot()


def create_plot():
    df = read_data()
    #  make_plot_file(df, 'download')
    #  make_plot_file(df, 'upload')
    make_plot_file(df)


def read_data():
    df = pd.io.parsers.read_csv(
        'speedtest.log',
        names='date time ping download upload'.split(),
        header=None,
        sep=r'\s+',
        parse_dates={'timestamp': [0, 1]},
    )
    print("Download Max [bit/s]:", round(df['download'].max()))
    print("Upload Max [bit/s]:", round(df['upload'].max()))
    print("Download Mean [bit/s]:", round(df['download'].mean()))
    print("Upload Mean [bit/s]:", round(df['upload'].mean()))
    print("Download Median [bit/s]:", round(df['download'].median()))
    print("Upload Median [bit/s]:", round(df['upload'].median()))
    return df


def make_plot_file(input):
    rcParams['xtick.labelsize'] = 'xx-small'
    #  plt.plot(input['timestamp'], input[column].to_numpy())
    plt.title('Bandwidth')
    ax = input.plot(x="timestamp", y="download", legend=False)
    ax2 = ax.twinx()
    input.plot(x="timestamp", y="upload", ax=ax2, legend=False, color="r")
    ax.yaxis.set_view_interval(0, 100000000)
    ax2.yaxis.set_view_interval(0, 100000000)
    ax.figure.legend()
    plt.ylabel('MBps')
    plt.xlabel('Timestamp')

    plt.grid()

    current_figure = plt.gcf()
    current_figure.subplots_adjust(bottom=.25)
    current_figure.savefig('{}.png'.format('bandwidth'))


if __name__ == '__main__':
    main()
