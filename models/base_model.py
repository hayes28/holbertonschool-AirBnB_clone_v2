#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models
from os import getenv

STORE_TYPE = getenv("HBNB_TYPE_STORAGE")
if STORE_TYPE == "db":
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            kwargs = {}
        kwargs.setdefault('id', str(uuid4()))
        kwargs.setdefault('created_at', datetime.utcnow())
        if not isinstance(kwargs['create_at'], datetime):
            kwargs['create_at'] = datetime.strptime(
                kwargs['create_at'], '%Y-%m-%dT%H:%M:%S.%f')

        kwargs.setdefault('updated_at', datetime.utcnow())
        if not isinstance(kwargs['update_at'], datetime):
            kwargs['update_at'] = datetime.strptime(
                kwargs['update_at'], '%Y-%m-%dT%H:%M:%S.%f')

        if STORE_TYPE != "db":
            kwargs.pop('__class__', None)
        for attr, val in kwargs.items():
            setattr(self, attr, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = dict(self.__dict__)
        new_dict.pop('_sa_instance_state', None)
        for k, v in new_dict.items():
            if isinstance(v, datetime):
                new_dict[k] = v.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def delete(self):
        """
        delete the current instance from the storage
        (models.storage) by calling the method delete
        """
        models.storage.delete(self)
