import android, time, BaseHTTPServer, urlparse

print "\nStarting sensors...\n"
droid = android.Android()
droid.startSensing()
time.sleep(2)

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    # Disable logging DNS lookups
    def address_string(self):
        return str(self.client_address[0])

    def do_GET(self):

        url = urlparse.urlparse(self.path)
        params = urlparse.parse_qs(url.query)

        delay = 1
        if 'delay' in params:
            delay = float(params['delay'][0])

        self.send_response(200)
        self.send_header("Content-type", "application/x-javascript; charset=utf-8")
        self.end_headers()

        try:
            while True:
                sensors = droid.readSensors()
                data = sensors['result']

                if 'jsonp' in params:
                    self.wfile.write("%s(" % (params['jsonp'][0]))

                output = []
                for type in data:
                    output.append("\"%s\": \"%s\"" % (type, data[type]))

                self.wfile.write("{%s}" % (','.join(output)))

                if 'jsonp' in params:
                    self.wfile.write(');')

                self.wfile.write("\n")
                self.wfile.flush()

                if 'continuous' not in params:
                    break

                time.sleep(delay)

        except socket.error, e:
            print "Client disconnected.\n"


PORT = 8000
httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.co.uk', 80))
sData = s.getsockname()

print "Serving at '%s:%s'" % (sData[0], PORT)
httpd.serve_forever()
