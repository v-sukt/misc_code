
For starting the application from bin's executables we need to first update the PYTHONPATH variable
to load the contents of gathonweb folder based modules

export PYTHONPATH=$PYTHONPATH:.
$ python bin/app.py

though this won't be required for 
$ nosetests

For sessions details use:

    >>> import pickle
    >>> import base64
    >>> base64.b64decode(open("sessions/XXXXX").read())
    "(dp1\nS'count'\np2\nI1\nsS'ip'\np3\nV127.0.0.1\np4\nsS'session_id'\np5\nS'XXXX'\np6\ns."
    >>>
    >>> x = base64.b64decode(open("sessions/XXXXX").read())
    >>>
    >>> pickle.loads(x)
    {'count': 1, 'ip': u'127.0.0.1', 'session_id': 'XXXXX'}

