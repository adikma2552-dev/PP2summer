import psycopg2
from config import DB_CONFIG


def get_connection():
    """Create and return connection to PostgreSQL database."""
    return psycopg2.connect(**DB_CONFIG)
