#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60, collation='utf8mb4_0900_ai_ci'),
                primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime,
                        default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Instantiates a new model
        """
        if not kwargs:
            kwargs = {}
        kwargs.setdefault('id', str(uuid4()))
        kwargs.setdefault('created_at', datetime.utcnow())
        if not isinstance(kwargs['created_at'], datetime):
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        kwargs.setdefault('updated_at', datetime.utcnow())
        if not isinstance(kwargs['updated_at'], datetime):
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
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
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """deletes basemodel instance"""
        models.storage.delete(self)
