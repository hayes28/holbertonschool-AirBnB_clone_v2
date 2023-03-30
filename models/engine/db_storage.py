#!/usr/bin/python3
""" This module defines a class to manage sql storage for hbnb clone """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """
    This class manages storage of hbnb models in SQL database
    """
    __engine = None
    __session = None
    __all_classes = {"state": State, "city": City, "amenity": Amenity,
                     "place": Place, "review": Review, "user": User}

    def __init__(self):
        """init engine"""
        data = [0, 0, 0, 0]
        data[0] = os.getenv("HBNB_MYSQL_USER")
        data[1] = os.getenv('HBNB_MYSQL_PWD')
        data[2] = os.getenv('HBNB_MYSQL_HOST') or 'localhost'
        data[3] = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            "mysql+mysqldb://{0}:{1}@{2}/{3}"
            .format(data[0], data[1], data[2], data[3]),
            pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the database"""
        if cls is None:

            temp = []
            for c in self.__all_classes.values():
                temp.extend(self.__session.query(c).all())
        else:
            if type(cls) is str:
                cls = self.__all_classes.get(cls.lower())
                if cls is None:
                    return {}
            temp = self.__session.query(cls).all()
        new_dict = {}
        for obj in temp:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_temp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_temp)
        self.__session = Session()

    def close(self):
        """ close session """
        self.__session.close()
