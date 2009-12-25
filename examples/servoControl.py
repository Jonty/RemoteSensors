import simplejson, serial, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = sock.makefile("rb")
sock.connect(("192.168.0.250", 8000))
sock.send("GET /?continuous=1&delay=0 HTTP/1.0\r\n\r\n")

ser = serial.Serial('/dev/ttyUSB1', 19200, timeout=1)

while True:
    try:
        string = file.readline();
        result = simplejson.loads(string)
    except ValueError:
        continue;

    pitch = abs(int(result['pitch']) - 90)
    roll = abs(int(result['roll']) - 90)

    if pitch > 170:
        pitch = 170
    if pitch < 10:
        pitch = 10

    if roll > 170:
        roll = 170
    if roll < 10:
        roll = 10

    serstring = "%dx%dy" % (pitch, roll)
    print serstring
    ser.write(serstring)

ser.close()
