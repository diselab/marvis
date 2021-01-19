
# Defines the RPI variable which is needed by rc-switch/RCSwitch.h
CXXFLAGS=-DRPI

all: transmit

transmit: ./rc-switch/RCSwitch.o transmit.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $+ -o $@ -lwiringPi -lwiringPiDev -lcrypt	

clean:
	$(RM) ../rc-switch/*.o *.o transmit RFSniffer

