#include "./rc-switch/RCSwitch.h"
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {

    int pin = 0; // WiringPi pin mapping: https://projects.drogon.net/raspberry-pi/wiringpi/pins/
    int protocol = 13; // standard value for Mumbi RC-10/RCS-20GS

    char *eptr;
    long long code = strtoll(argv[1], &eptr, 10); // read transmission code from program parameters

    if (argc >= 3) protocol = atoi(argv[2]); // set protocol if parameter is given

    if (wiringPiSetup () == -1) return 1; // setup WiringPi library

    RCSwitch rCSwitch = RCSwitch(); // setup RCSwitch library

    if (protocol != 0) rCSwitch.setProtocol(protocol); // set protocol to standard (0 does not exist and defaults to library default)

    rCSwitch.enableTransmit(pin); // enable transmit mode on designated pin
    rCSwitch.send(code, 33); //  send code in 33 bit transmission

    return 0;
}
