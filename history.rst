###################
CherryPy - JSON-RPC
###################

by Gerold Penz 2011


=============
Version 0.3.1
=============

2013-05-01

- Übersiedelung nach Github

- Setup erstellt und alles für den Upload zu PyPi vorbereitet

- Erster Upload zu PyPi

- Responses in ein eigenes Modul ausgelagert

- *tools.py*-Modul für *jsonrpcmethod*-Tool erstellt


=============
Version 0.2.4
=============

2011-09-26

- `raise` aus Testserver entfernt

- Versucht, den Ordner *cpjsonrpc* durch ein Modul zu ersetzen. Damit wird aber
  ein Einbinden des Quellcodes für Subversion erschwert. Deshalb bleibt es beim
  Ordner.


=============
Version 0.2.3
=============

2011-09-08

- Fehlerrückgabe verbessert

- Fehler werden jetzt besser geloggt.


=============
Version 0.2.2
=============

07.09.2011

- `print`-Anweisungen wurden durch `cherrypy.log` ersetzt.

- Änderungen in den Docstrings


=============
Version 0.2.1
=============

2011-09-07

- Batch-Requests sind jetzt möglich

- Rückgabe der Responses (Successful- und Error-Objekte)

- Das Ding funktioniert ab jetzt


=============
Version 0.1.3
=============

2011-09-07

- Request-Klassen für die Fehlerrückgabe


=============
Version 0.1.2
=============

06.09.2011

- Die Parameter werden jetzt schon vernünftig geparst


=============
Version 0.1.1
=============

2011-09-06

- Erstimport

- Grundstruktur erstellt

- Error-Klassen 

- JSON-RPC-Methoden der JsonRpcMethods-Klasse bestimmen

- Grundstruktur erstellt

- Testserver erstellt

- Tests mit json_in und json_out Tools von CherryPy
