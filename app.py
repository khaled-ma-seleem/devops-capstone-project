# To run the app use one of these:
# FLASK_APP=service FLASK_ENV=development flask run
# python app.py

from service import app
import os

# Set environment variables
os.environ['FLASK_APP'] = 'service'
os.environ['FLASK_ENV'] = 'development'  # Change to 'production' for production environment

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
