import os
from src import create_app

# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/config.py
# app = create_app('flask_test.cfg')

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
