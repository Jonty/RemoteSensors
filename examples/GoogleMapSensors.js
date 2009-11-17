function RemoteSensors (params) {

    this.fetch = function () {
        while (script = document.getElementById('JSONP')) {
            script.parentNode.removeChild(script);
            for (var prop in script) {
                delete script[prop];
            }
        }

        var node = document.createElement('script');
        node.setAttribute('language','javascript');
        node.setAttribute('id','JSONP');
        node.setAttribute('src', 'http://' + this.host + '/?jsonp=' + this.callback + '&rand=' + Math.random());
        document.body.appendChild(node);
    };

    this.getHost = function () {
        host = prompt("Please enter the host:port of the sensor server", "");
        if (host) {
            this.host = host;
        } else {
            this.getHost();
        }
    };

    // Initial
    this.callback = params.callback;
    if (params.host) {
        this.host = params.host;
    } else {
        this.getHost();
    }

    this.fetch();
}

var rs = new RemoteSensors({callback: 'gotData'});
function gotData(data) {

    var url = gApplication.getPageUrl();
    var zoom = url.match('z=([0-9]+)');

    var map = gApplication.getMap().getCenter();
    gApplication.getMap().panTo(new GLatLng(map.lat() + (data['pitch'] / (zoom[1] * zoom[1] * 100)), map.lng() - (data['roll'] / (zoom[1] * zoom[1] * 100))));

    rs.fetch();
}
