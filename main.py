import os
from src import create_app

# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/config.py

config_name = os.getenv('APP_SETTINGS', 'development') # config_name = "development"
app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
