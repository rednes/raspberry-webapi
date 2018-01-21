# raspberry-webapi

Raspberry Pi 3 Model BでLチカするWebAPIを構築します。

## Requirements

- python3
- wiringpi

## CIRCUIT_DIAGRAM

![回路図](https://raw.githubusercontent.com/rednes/raspberry-webapi/img/raspberrypi.png)


## Usage

### Start Server

```
$ python3 index.py
```

### Call API

```
$ curl http://localhost:8080/api/1
$ curl http://localhost:8080/api/2
$ curl http://localhost:8080/api/3
```
