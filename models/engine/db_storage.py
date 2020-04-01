#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""

from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine: creates engine based on arguments passed
        __session: session to be created
    """

    __engine = None
    __session = None
    __filtered = {}
    __all = {}

    def __init__(self):
        """Instantiation of DBStorage class"""

        i = 0
        args_dict = {}

        while i < len(sys.argv):
            param = sys.argv[i]
            split_param = param.split("=")
            args_dict[split_param[0]] = split_param[1]

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(args_dict['HBNB_MYSQL_USER'], args_dict['HBNB_MYSQL_PWD'], args_dict[HBNB_MYSQL_HOST], args_dict['HBNB_MYSQL_DB'], pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)

        if args_dict[HBNB_ENV] == 'test':
            Base.metadata.drop_all(self.__engine)

        else:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

    def all(self, cls=None):
        """

        Return:
            returns a dictionary of __object
        """
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        if cls is None:

            for cls in classes:
                all_recs = self.__session.query(cls).all()
                for i in all_recs:
                    key = i.__name__ + getattr(i,i.id)
                    value = i # or is it i.__dict__
                    self.__all.update({key:value})

            return self.__all

        else:

            fil_recs =  self.__session.query(cls).all()

            for value in fil_recs:
                key = value.__name__ + getattr(value,value.id)
                #or is it val = value.__dict__
                self.__filtered.update({key:value})

            return self.__filtered

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        self.__session.add(obj)


    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()
 
    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__enginge, expire_on_commit=False)
            Session = scoped_session(sessiobn_factory)
            self.__session = Session
        except:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside
        """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

        except:
            pass

    def close(self):
        self.__session.remove()
