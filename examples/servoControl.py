import simplejson, serial, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = sock.makefile("rb")
sock.connect(("192.168.0.250", 8000))
sock.send("GET /?continuous=1&delay=0 HTTP/1.0\r\n\r\n")

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)

oldpitch = oldroll = 0;
lastpitch = lastroll = 0;
pitchc = rollc = 0

while True:
    try:
        string = file.readline();
        result = simplejson.loads(string)
    except ValueError:
        continue;

    pitch = abs(int(result['pitch']) - 90)
    roll = abs(int(result['roll']) - 90)

    if oldpitch == 0:
        oldpitch = pitch
    if oldroll == 0:
        oldroll = roll

    if pitch > 170:
        pitch = 170
    if pitch < 10:
        pitch = 10

    if pitch == lastpitch:
        pitchc += 1
    else:
        pitchc = 0

    setpitch = pitch
    if abs(pitch - lastpitch) > 15 or pitchc < 3:
        setpitch = oldpitch

    if setpitch != oldpitch:
        pitchc = 0
        oldpitch = setpitch
        ser.write("%dx" % setpitch)

    lastpitch = pitch

    if roll > 170:
        roll = 170
    if roll < 10:
        roll = 10

    if roll == lastroll:
        rollc += 1
    else:
        rollc = 0

    setroll = roll
    if abs(roll - lastroll) > 15 or rollc < 3:
        setroll = oldroll

    if setroll != oldroll:
        rollc = 0
        oldroll = setroll
        ser.write("%dy" % setroll)

    lastroll = roll

ser.close()
