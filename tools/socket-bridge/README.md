# socket-bridge

## Getting started

1. Clone (this part of the) repository on device with 433 Mhz transmitter (e.g., Raspberry Pi)
2. Run `make` to build dependencies: transmit and rc-switch
3. Run `python3 socket-bridge.py` to start the server on default port 8080
4. Send PUT to `hostname:port/socket/{1-16}/{on|off}` to switch a channel between 1 and 16 on or off

## References

This work is inspired by and based on

- [sui77/rc-switch](https://github.com/sui77/rc-switch)
- [atsage/rc-switch](https://github.com/atsage/rc-switch)
- [ninjablocks/433Utils](https://github.com/ninjablocks/433Utils)

Further interesting and related projects

- [jccprj/RemoteSwitch-arduino-library](https://github.com/jccprj/RemoteSwitch-arduino-library)
- [mschlenstedt/LoxBerry-Plugin-RCSwitch](https://github.com/mschlenstedt/LoxBerry-Plugin-RCSwitch)
- [sui77/SimpleRcScanner](https://github.com/sui77/SimpleRcScanner)
