import psycopg2
from config import get_db_info

def main():
    """ read the database configuration file"""
    filename = 'database.ini'
    section = 'postgresql'
    db_info = get_db_info(filename, section)
    """set conn = none so that the connection is closed if it fails"""
    conn = None
    """ connect to the PostgreSQL database server"""
    try:
        with psycopg2.connect(**db_info) as conn:
            print("Successfully connected to the database!")
            """ create a cursor"""
            with conn.cursor() as cur:
                # write your queries here...maybe
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Failed to connect to the database: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    main()