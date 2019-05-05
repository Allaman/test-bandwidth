A simple set of python scripts too measure and visualize your internet connection.

[Little background](https://knowledge.rootknecht.net/testing-internet-connection)

## Dependencies

- Docker :)

When using without Docker see `setup.py` for Python dependencies.

## Build

`git clone https://repo.rootknecht.net/open/vis-bandwidth.git`
`cd vis-bandwidth`
`docker build . -t vis`

## Collect Data

`docker run -v $PWD/:/app vis test`

`cd vis-bandwidth && python main.py --cmd test`

## Visual Data

`docker run -v $PWD/:/app vis plot`

`cd vis-bandwidth && python main.py --cmd plot`

## Examples

![Data](https://repo.rootknecht.net/open/vis-bandwidth/raw/master/results/speedtest.log)

![Plot](./results/bandwidth.png)

## Todo

- advanced plotting!
- formated output of calculated values
- external configuration
- Graph for Ping
