from threading import Thread
from influxdb import InfluxDBClient

host='localhost' 
port=8086
dbname = 'shower'
user = 'root'
password = 'root'
 
class database_post(Thread):
 
    def __init__(self, tag, value):
        ''' Constructor. '''
        Thread.__init__(self)
        self.tag = tag
        self.value = value
 
    def run(self):

        client = InfluxDBClient(host, port, user, password, dbname)
        json_body = [
            {
                "measurement": "shower",
                "tags": {
                    "axis": self.tag
                },
                "fields": {
                    "value": self.value
                }
            }
        ]
        client.write_points(json_body)

