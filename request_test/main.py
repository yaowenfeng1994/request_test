#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import asyncio

import tornado.httpserver as http_server
import tornado.platform.asyncio as tornado_asyncio
import tornado.options as options

from tornado.web import Application

from handler.ip_test import IPHandler

options.define("port", default="8080", help="run on the given port", type=int)
options.define("debug", default=False, help="enable the debug mode", type=bool)


class ServiceApplication(Application):
    def __init__(self, **settings):
        super(ServiceApplication, self).__init__(
            handlers=[
                (r"/ip_test", IPHandler),
            ],
            **settings)


if __name__ == '__main__':
    options.parse_command_line()
    tornado_asyncio.AsyncIOMainLoop().install()
    app = ServiceApplication(debug=options.options.debug)
    server = http_server.HTTPServer(app, xheaders=True)
    server.listen(options.options.port)
    logging.info("Debug-Mode {switch}".format(switch="On" if options.options.debug else "Off"))
    logging.info("Server (pid::{pid}) started on {port}".format(pid=os.getpid(), port=options.options.port))
    asyncio.get_event_loop().run_forever()
