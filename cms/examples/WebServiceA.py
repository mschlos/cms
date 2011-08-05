#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programming contest management system
# Copyright © 2010-2011 Giovanni Mascellani <mascellani@poisson.phc.unipi.it>
# Copyright © 2010-2011 Stefano Maggiolo <s.maggiolo@gmail.com>
# Copyright © 2010-2011 Matteo Boscariol <boscarim@hotmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Simple web service example.

"""

import os

import tornado.web

from cms.async.AsyncLibrary import logger
from cms.async.WebAsyncLibrary import WebService
from cms.async import ServiceCoord


class WebServiceA(WebService):
    """Simple web service example.

    """

    def __init__(self, shard):
        logger.initialize(ServiceCoord("WebServiceA", shard))
        logger.debug("WebServiceA.__init__")
        WebService.__init__(self,
            9999,
            [(r"/", MainHandler)],
            {
                "login_url": "/",
                "template_path": "./",
                "cookie_secret": "DsEwRxZER06etXcqgfowEJuM6rZjwk1JvknlbngmNck=",
                "static_path": os.path.join(os.path.dirname(__file__),
                                            "..", "cms", "async", "static"),
                "debug": "True",
            },
            shard=shard)
        self.ServiceB = self.connect_to(ServiceCoord("ServiceB", 1))


class MainHandler(tornado.web.RequestHandler):
    """Home page handler.

    """
    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print sys.argv[0], "shard"
    else:
        WebServiceA(int(sys.argv[1])).run()
