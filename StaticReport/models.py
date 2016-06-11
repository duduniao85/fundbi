# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
##############################连接ORACLE数据库###############################
##############################取数据表数据###################################
from sqlalchemy.orm import *
# from fundbi.db import Session, metadata
from django.conf import settings
from django.core import signals
from django.dispatch import dispatcher
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
#
# def create_engine():
#     url = URL(drivername=settings.DATABASE_ENGINE,
#               database=settings.DATABASE_NAME,
#               username=settings.DATABASE_USER,
#               password=settings.DATABASE_PASSWORD,
#               host=settings.DATABASE_HOST,
#               port=settings.DATABASE_PORT or None,
#               query = getattr(settings, 'DATABASE_OPTIONS', {})
#               )
#     options = getattr(settings, 'SQLALCHEMY_OPTIONS', {})
#     engine = sqlalchemy.create_engine(url, **options)
#     return engine

Base = declarative_base()

# 定义表结构
class GameCompany(Base):
    __tablename__ = 'game_company'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    country = Column(String(50))


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('game_company.id'), index=True)
    category = Column(String(10))
    name = Column(String(200), nullable=False)
    release_date = Column(Date)

    # 和Django不同，外键需要显式定义，具体好坏见仁见智
    # 此处的relation可以为lazy加载外键内容时提供一些可配置的选项
    company = relationship('GameCompany', backref=backref('games'))


# 此处定义要使用的数据库
db_engine=create_engine('oracle+cx_oracle://king:1@127.0.0.1:1521/XE', echo=True)
# 调用create_all来创建表结构，已经存在的表将被忽略
Base.metadata.create_all(db_engine)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, Column, ForeignKey
metadata = MetaData()

# we can reflect it ourselves from a database, using options
# such as 'only' to limit what tables we look at...
metadata.reflect(db_engine, only=['weeklyquote'])



# we can then produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# calling prepare() just sets up mapped classes and relationships.
Base.prepare()

# mapped classes are ready
weeklyquote = Base.classes.weeklyquote
# user和address就是表名，通过这样的语句就可以把他们分别映射到User和Address类
