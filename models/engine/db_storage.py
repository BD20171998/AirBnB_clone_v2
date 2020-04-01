#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""

from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """This class saves data to a MySQL database"""

    __engine = None
    __session = None
    __filtered = {}
    __all = {}

    def __init__(self):
        """Instantiation of DBStorage class"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        else:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

    def all(self, cls=None):
        """
        This returns all or one specific class object based on user's input as a 
        dictionary
        """
        print(type(cls))
        if cls:
            pass
        else:
            classes = [State]
            spec_recs = {}
            for cls in classes:
                for rows in self.__session.query(cls).all():
                    key = "{}.{}".format(rows.__class__.__name__, rows.id)
                    spec_recs[key] = rows
        return all_recs

    def new(self, obj):
        """Adds given object to DB session"""
        self.__session.add(obj)


    def save(self):
        """saves the current session to the MySQL database"""
        self.__session.commit()

    def reload(self):
        """reload the database
        """
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__enginge, expire_on_commit=False)
            Session = scoped_session(sessiobn_factory)
            self.__session = Session
        except:
            pass

    def delete(self, obj=None):
        """Delete obj if it’s inside"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def close(self):
        """Removes session when needed"""
        self.__session.remove()
