RemoteSensors
=============

RemoteSensors is a small python daemon that runs under the Android Scripting Environment.
It's purpose is to explore the options that become available for device integration when the sensors 
available on Android devices are exported for use in external applications.

The daemon can run in several modes and is fairly simple, I suggest reading the code is the best
documentation for this - it's very small.

It ships with one example app, a javascript bookmarklet to be used on Google Maps pages that 
interactively scrolls the map by tilting the Android device.


Demo
----

1. Download remoteSensors.pl and place it in the Android Scripting Environments scripts directory on the SD card of the Android device. Connect the device to the same wifi network as the computer running google maps.

2. Start remoteSensors.pl from within the Android Scripting Environment, after a few seconds it will give you an IP address and port.

3. Save the following line as a bookmarklet in your browser:
    
    javascript:var%20e=document.createElement('script');e.setAttribute('language','javascript');e.setAttribute('src','http://www.jonty.co.uk/bits/GoogleMapSensors.js');document.body.appendChild(e);void(0);

4. Browse to a google map, hit the bookmarklet, and when prompted enter the IP:PORT given to you by remoteSensors.pl

5. Tilt your device and scroll about!
