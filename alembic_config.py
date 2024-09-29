import configparser
import os

# Create the ConfigParser object
config = configparser.ConfigParser()

# Read the .ini file
config.read('alembic.ini')

# Access a specific section and value
DB_URL = config['alembic']['sqlalchemy.url']

# Optionally, set it in os.environ if needed
# os.environ['DATABASE_URL'] = database_url
