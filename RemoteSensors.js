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
