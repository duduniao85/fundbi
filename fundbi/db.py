#-*- coding: utf-8 -*-
# from django.conf import settings
# from django.core import signals
# from django.dispatch import dispatcher
# import sqlalchemy
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.engine.url import URL
#
# __all__ = ['Session', 'metadata']
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
#
# def end_request(signal, sender):
#     Session.remove()
#
# dispatcher.connect(receiver=end_request,signal=signals.request_finished)
# metadata = sqlalchemy.MetaData()
# Session = scoped_session(sessionmaker(autoflush=True,transactional=True,bind=create_engine()))
