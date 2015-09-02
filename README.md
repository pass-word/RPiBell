# RPiBell

Ring a bell connected to Raspberry Pi's GPIO pin.

## Installation

```shell
git clone https://bitbucket.org/pass-word/rpibell.git
```

## Usage

```python
from rpibell import RPiBell
bell = RPiBell(18)              # Your GPIO pin

# Ring a single time
bell.ring_once()

# Set ring time
bell.ring_time = 0.025

# Set ring interval
bell.ring_interval = 0.03

# Make a burst
bell.ring_times(20)             # Ring for 20 times

# Ring for a certain time
bell.ring(30)                   # Ring for 30 seconds
```

## Requirements

 * RPi.GPIO
 * You may need root privilege to use this library

## Notes

Currently all functions will return after ring has finished.

## Author

 * [James Swineson](https://swineson.me)