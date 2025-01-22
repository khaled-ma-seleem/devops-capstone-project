# To run the app use one of these:
# FLASK_APP=service FLASK_ENV=development FLASK_RUN_PORT=$PORT flask run
# python app.py
# honcho start

from service import app
import os

FLASK_ENV = os.getenv('FLASK_ENV', 'development')
FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", "5000")

debug = {'development': True, 'production': False}
mode = debug[FLASK_ENV]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=FLASK_RUN_PORT, debug=mode)
