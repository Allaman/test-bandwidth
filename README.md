A simple set of python scripts too measure and visualize your internet connection.

[Little background](https://knowledge.rootknecht.net/testing-internet-connection)

## Dependencies

- Docker :)

## Build

docker build . -t vis

## Collect Data

Run `docker run ${PWD}/results:/results vis test`

## Visual Data

Run `docker run ${PWD}/results:/results vis plot`

## Examples

![Data](https://repo.rootknecht.net/open/vis-bandwidth/raw/master/results/speedtest.log)

![Plot](./results/bandwidth.png)

## Todo

- advanced plotting!
- non docker doc
- formated output of calculated values
- external configuration
- Graph for Ping
