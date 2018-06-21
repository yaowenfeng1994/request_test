#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web


class IPHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        remote_ip = self.request.remote_ip
        print(remote_ip)
        self.write(remote_ip)
