try:
    from waitress import serve
except ImportError:
    serve = None

from run import app

if serve is not None:
    serve(app, host='127.0.0.1', port=5000, threads=8)
else:
    app.run(host='127.0.0.1', port=5000, threaded=True)