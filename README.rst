##########################################
CherryPy JSON-RPC-Server Tool (DEPRECATED)
##########################################

**DEPRECATED!**

Use *python-jsonrpc* instead:
    
- https://pypi.python.org/pypi/python-jsonrpc
- https://github.com/gerold-penz/python-jsonrpc


**python-jsonrpc** Example:

.. code:: python

    #!/usr/bin/env python
    # coding: utf-8

    import cherrypy
    from pyjsonrpc.cp import CherryPyJsonRpc, rpcmethod


    class Root(CherryPyJsonRpc):

        @rpcmethod
        def add(self, a, b):
            """Test method"""
            return a + b

        index = CherryPyJsonRpc.request_handler


    print "Starting HTTP server ..."
    print "URL: http://localhost:8080"
    cherrypy.quickstart(Root())


---------

| 
| 

*cherrypy-jsonrpc* stellt CherryPy eine Klasse zum Handling von 
JSON-RPC v2.0 zur Verfügung.

Leitet man eine Klasse von dieser Klasse ab, werden alle mit

::

    <FunctionName>.exposed = True

gekennzeichneten Methoden dieser Klasse zu JSON-RPC-Methoden.

An der Umsetzung des JSON-RPC-Servers zur Verwendung als CherryPy-Tool wird
derzeit gearbeitet.

Informationen:

- `JSON-RPC Specification`_
- `Historical JSON-RPC Specifications`_
- `JSON-Schema`_ (klingt interessant - sollte man einbauen)


.. _`JSON-RPC Specification`: http://jsonrpc.org/spec.html
.. _`Historical JSON-RPC Specifications`: http://jsonrpc.org/historical/
.. _`JSON-Schema`: http://json-schema.org/


Beispiel:

.. code:: python

    #!/usr/bin/env python
    # coding: utf-8

    import cherrypy
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

