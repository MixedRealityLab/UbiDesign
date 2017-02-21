var express = require('express');
var router = express.Router();
var influxClient = require('./../database/influx.js');


/* GET home page. */
router.get('/', function(req, res, next) {
  res.send("hello");
});

router.post('/range', function(req, res, next) {
        var sensor_id = req.body.sensor_id;
        var start = req.body.start;
        var end = req.body.end;

        var query = "select value from shower where axis='"+sensor_id+"' AND time >=  '"+ start +"' AND time <= '" + end + "'";

        console.log("query:: ", query);
        influxClient.get().query(query, function (err, results) { 
            if (err) {
              console.log("[Error]:: /data/range", sensor_id, start, end, err);
              res.send(err);
            }
            
            res.json(results);
        });        
      });

module.exports = router;
