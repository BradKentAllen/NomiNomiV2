# NomiNomi



home IP:  192.168.1.220

Pass:  goose13





```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
	ssid="Raven_Nest"
	psk="goose133"
	key_mgmt=WPA-PSK
}

network={
	ssid="AllenNet1"
	psk="fiGure8knot87881?"
}
```



## Operations Notes

* Boat needs to point generally North on power up
* Wiggle boat during and after power up to engage compass
* Boat needs to be pointed into a sail-able wind angle when START is pressed.  It will intially sail this course until a distance from home.



## Hardware Technical Notes

```
# Aug 2022 list
LCD					0x23
ADC (wind/volt)		0x48
DS1307 RTC			0x68
BNo055 (compass)	0x69
Ultimate GPS

# ### OLD

LCD				0x23
ADC (wind/volt)	0x49	
servo board		0x40
9-axis accel	0x69 (or 0x68)
```

#### Compass

https://peppe8o.com/magnetometer-with-raspberry-pi-computers-gy-271-hmc5883l-wiring-and-code/

for yacht:  https://www.roboticboat.uk/Microcontrollers/RaspberryPi3/CMPS14/CMPS14.html

## Software Technical Notes

- GPS
    - GPS returns NMEA in format DDMM.MMMM but the circuit python library parses this to **decimal degrees**.
    - Haversine:  https://pypi.org/project/haversine/
    - angle:  https://towardsdatascience.com/calculating-the-bearing-between-two-geospatial-coordinates-66203f57e4b4
    - Ultimate GPS:  https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-parsing
- 
