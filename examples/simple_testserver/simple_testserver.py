#!/usr/bin/env python
# coding: utf-8

import os
import sys
import cherrypy

THISDIR = os.path.dirname(os.path.abspath(__file__))
# Add app dir to path for testing cpjsonrpcserver
APPDDIR = os.path.abspath(os.path.join(THISDIR, os.path.pardir, os.path.pardir))
sys.path.insert(0, APPDDIR)

import cpjsonrpcserver


class JsonRpcMethods(cpjsonrpcserver.JsonRpcMethods):
    
    def hello(self, name):
        return u"Hello " + name
    hello.exposed = True
    
    
    def multi(self, num):
        return num * 2
    multi.exposed = True


def main():
    cherrypy.quickstart(JsonRpcMethods(debug = True))


if __name__ == "__main__":
    main()
