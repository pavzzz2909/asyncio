from support.config import bd_user, bd_password, bd_database

import asyncpg

import aiohttp
import asyncio
from asyncio import run
import more_itertools
from pprint import pprint

import hashlib
from datetime import datetime

# для работы с Flask
from flask import Flask, jsonify, request
from flask.views import MethodView

# для работы с БД
import sqlalchemy
from sqlalchemy import (create_engine, Column, exc,
                        MetaData, Table, Boolean, DateTime,
                        Index, Text, Integer, String, desc, between,
                        DateTime, BIGINT, TIMESTAMP, PrimaryKeyConstraint,
                        UniqueConstraint, ForeignKeyConstraint, ForeignKey, Numeric)
from sqlalchemy.orm import Session, sessionmaker, relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() # класс от которого наследуются класс таблиц



class AsyncBaseService(object):
    engine = create_async_engine(f'postgresql+asyncpg://{bd_user}:{bd_password}@127.0.0.1:5432/{bd_database}', echo=True)
    session = sessionmaker(bind=engine)
    session = Session(bind=engine)

async_connection = AsyncBaseService.engine.connect()

#############################################################################

class BaseService(object):
    engine = sqlalchemy.create_engine(f'postgresql://{bd_user}:{bd_password}@localhost:5432/{bd_database}')
    session = sessionmaker(bind=engine)
    session = Session(bind=engine)

connection = BaseService.engine.connect()
