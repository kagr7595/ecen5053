

#Using [7] as a basis for Websockets
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import redis
import json
from shared_classes import *


#create a connection to the localhost Redis server instance, by default it runs on port 6379
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('new python connection')

    def on_message(self, message):
        print ('message received %s' % message)
        lval = redis_db.get('current')
        v1 = lval.decode()
        v = json.loads(v1)
        l = P_dict(**v)
        

        msg = json.loads(message)
        if msg['type'] == "current_temp_f":
            val = "%0.1f" % l.show_current_temp_f()[0]
            datetime = l.show_current_temp_f()[1]
            send_msg = dict( type='current_temp_f',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))
        elif msg['type'] == "current_hum":
            val = "%0.1f" % l.show_current_hum()[0]
            datetime = l.show_current_hum()[1]
            send_msg = dict( type='current_hum',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))
        elif msg['type'] == "lowest_temp_f":
            val = "%0.1f" % l.show_lowest_temp_f()[0]
            datetime = l.show_lowest_temp_f()[1]
            send_msg = dict( type='lowest_temp_f',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))
        elif msg['type'] == "lowest_hum":
            val = "%0.1f" % l.show_lowest_hum()[0]
            datetime = l.show_lowest_hum()[1]
            send_msg = dict( type='lowest_hum',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))
        elif msg['type'] == "highest_temp_f":
            val = "%0.1f" % l.show_highest_temp_f()[0]
            datetime = l.show_highest_temp_f()[1]
            send_msg = dict( type='highest_temp_f',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))
        elif msg['type'] == "highest_hum":
            val = "%0.1f" % l.show_highest_hum()[0]
            datetime = l.show_highest_hum()[1]
            send_msg = dict( type='highest_hum',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))
        elif msg['type'] == "average_temp_f":
            val = "%0.1f" % l.show_average_temp_f()[0]
            datetime = l.show_average_temp_f()[1]
            send_msg = dict( type='average_temp_f',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))
        elif msg['type'] == "average_hum":
            val = "%0.1f" % l.show_average_hum()[0]
            datetime = l.show_average_hum()[1]
            send_msg = dict( type='average_hum',
                             data=val,
                             time=datetime )
            self.write_message(json.dumps(send_msg))


    def on_close(self):
        print ('connection closed')

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
    ])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s ***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
