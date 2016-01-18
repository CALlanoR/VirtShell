""" Filename: provisioning_agent
    Description: Agent to provisioning containers and virtual machines in a host
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

__version__ = '0.1'

import os
import sys
import imp
import time
import json
import signal
import psutil
import os.path
import logging
import datetime
import tornado.web
import tornado.ioloop
import multiprocessing
import tornado.websocket
import tornado.httpserver
from database import Database
from exceptions import PluginException
from logging.handlers import SysLogHandler

################################################################################
# Global Variables
################################################################################
main_logger = None
database = None
listener_handler = None

################################################################################
# Signals
################################################################################
def signal_handler(signal, frame):
    pid = os.getpid()
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        main_logger.info("agent-service with pid [%d] terminated.", child.pid)
        child.kill()
    main_logger.info("agent with pid [%d] terminated.", pid)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

################################################################################
# AgentService Class
################################################################################
class ListenerHandler(object):
    def __init__(self):
        self.listeners = {}
        self.plugins = {}
        self.plugin_folder = "./plugins"
        self.special_method = "__init__.py"
        self.get_plugins()
        self.register_plugin_actions()

    def register_plugin_actions(self):
        for plugin_name in self.plugins:            
            plugin_class = self.load_plugin(plugin_name)
            # Asignar aqui el logger para no pasarlo mas
            plugin_methods = plugin_class.catalogue()
            for plugin_method_name in plugin_methods:
                plugin_method = getattr(plugin_class, plugin_method_name)
                plugin_key = plugin_name + '-' + plugin_method_name
                self.register(plugin_key, (plugin_class, plugin_method))
        print(self.listeners)

    def register(self, listener, action):            
        self.listeners[action] = listener

    def dispatch(self, request):
        message = json.loads(request)
        action = message['drive'] + '-' + message['action']
        plugin, method = self.listeners[action]
        return method(request)                  
            
    def get_plugins(self):
        main_logger.info("finding plugins")
        possible_plugins = os.listdir(self.plugin_folder)
        possible_plugins.remove(self.special_method)
        for module in possible_plugins:
            if not module.endswith(".pyc") and not os.path.isdir(module):
                module = os.path.splitext(module)[0]
                info = imp.find_module(module, [self.plugin_folder])
                self.plugins[module] = info
                main_logger.info("plugin %s.py found" % module)

    def load_plugin(self, name):
        return imp.load_module(name, *(self.plugins[name]))

################################################################################
# RequestHandler Class
################################################################################
class RequestHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        main_logger.info("new connection")
        main_logger.info("Connection stablished")
        RequestHandler.clients.append(self)

    def on_message(self, json_message):
        print(json_message)
        main_logger.info("message received %s" % json_message)
        response = listener_handler.dispatch(json_message)
        self.write_message(response)

    def on_close(self):
        main_logger.info("connection closed")
        RequestHandler.clients.remove(self)

    @classmethod
    def write_to_clients(cls):
        for client in cls.clients:
            client.write_message("Hi there!")

application = tornado.web.Application([(r'/', RequestHandler)])

################################################################################
# Logging plumbing
################################################################################
def init_logger(LoggerName):
    # Create logger
    logger = logging.getLogger(LoggerName)
    logger.setLevel(logging.INFO)
    # Create handler
    handler = SysLogHandler(address='/dev/log')
    handler.setLevel(logging.INFO)
    # Create formatter
    formatter = logging.Formatter('%(asctime)s %(name)s '
                                  '%(levelname)s %(message)s')
    # Add formatter and handler
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # Return logger
    return logger

if __name__ == "__main__":
    main_logger = init_logger('virtshell-agent')
    database = Database(main_logger)
    listener_handler = ListenerHandler()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    main_logger.info("started...")
    #tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=15), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()

# sudo python3 agent.py