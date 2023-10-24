"""
This module contains the entry point for your application.
It imports the Flask app object from the application package and runs the application.
"""

from application.app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
