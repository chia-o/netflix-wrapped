""" instead of hardcoding the database connection details, this provides flexibility if I use more than 1 database"""
# don't forget to add database.ini to .gitignore
from configparser import ConfigParser

def get_db_info(filename, section):
    """ create a parser instance"""
    parser = ConfigParser()
    parser.read(filename)

    """ return the databse metadata as a dictionary in tuples"""
    db_info = {}
    if parser.has_section(section):
        pairs = parser.items(section)
        for item in pairs:
            db_info[item[0]] = item[1]
    else:
        raise Exception(f"Section{section} could not be found in the file.")
    return db_info