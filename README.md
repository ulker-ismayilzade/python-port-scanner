# python-port-scanner
A custom multi-threaded port scanner built with Python to identify open TCP ports and active services.
# Simple Python Port Scanner
A multi-threaded port scanner developed in Python to identify open ports and services on a target host.

## Features
- Scans common TCP ports.
- Provides service name detection based on port numbers.
- Fast execution using Python's `socket` library.

## How it works
The script attempts to establish a connection to a range of ports. If a connection is successful, the port is flagged as open.
