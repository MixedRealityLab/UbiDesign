from threading import Thread
from influxdb import InfluxDBClient

host='localhost' 
port=8086
dbname = 'shower'
user = 'root'
password = 'root'
 
class database_post(Thread):
 
    def __init__(self, tag, value, measurement):
        ''' Constructor. '''
        Thread.__init__(self)
        self.tag = tag
        self.value = value
        self.measurement = measurement
 
    def run(self):

        try: 
            floatValue = float(self.value)
            client = InfluxDBClient(host, port, user, password, dbname)
            json_body = [
                {
                    "measurement": self.measurement,
                    "tags": {
                        "axis": self.tag
                    },
                    "fields": {
                        "value": floatValue
                    }
                }
            ]
            client.write_points(json_body)
        except Exception as error:
            print(repr(error))

