# home-dashboard
This is a small flask applikation to manage

- 433mhz devices
- Next garbage pickup
- Weather
- Temperatures
- Spotify

in a Dashboard overview.


# Installation

    python3 -m venv venv
	pip install requirements -r requirements.txt

#Debian:

    sudo apt-get install libtool libusb-1.0-0-dev librtlsdr-dev rtl-sdr build-essential autoconf cmake pkg-config
    git clone https://github.com/merbanan/rtl_433.git
    cd rtl_433/
    mkdir build
    cd build
    cmake ..
    make
    make install
