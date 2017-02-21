var influx = require('influx')

var client = influx({
	  host: 'localhost',
	  port: 8086,
	  protocol: 'http',
	  database: 'shower'
	})

exports.get = function() {
  	return client;
}
