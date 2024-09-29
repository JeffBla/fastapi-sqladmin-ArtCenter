from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from alembic_config import DB_URL

engine = create_engine(DB_URL, isolation_level='AUTOCOMMIT')

Session = sessionmaker(bind=engine)
Base = declarative_base()
