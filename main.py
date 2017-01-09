import json

from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler
from tornado.web import Application

from components import db_handler


active_clients = []


def send_data_to_clients(message):
    print "active cleints {}".format(len(active_clients))
    for client in active_clients:
        try:
            client.write_message(message)
        except Exception as err:
            print "websocket err: {}".format(err.message)
            active_clients.remove(client)


class SocketOutputHandler(WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print "websocket opened"
        if self not in active_clients:
            active_clients.append(self)

    def on_message(self, message):
        self.write_message(json.loads(message))
        print message

    def on_close(self):
        print "websocket closed!"
        if self in active_clients:
            active_clients.remove(self)



class EmployeeInputHandler(Application):
    def post(self, *args, **kwargs):
        data = self.request.body
        send_data_to_clients(data)
        message = json.loads(data)
        db_handler.save_employee_data(data)

