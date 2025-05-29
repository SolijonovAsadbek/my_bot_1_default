from typing import Literal

from sqlalchemy import (create_engine,
                        text,
                        Column,
                        Text, String, Integer, INT, CheckConstraint,
                        )
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from tabulate import tabulate

# from sqlalchemy.ext.declarative import declarative_base
# sqlite, postgres, mysql
db_url = 'database.db'
# dbl_url = "postgresql + psycopg2: // user:password@host:port/db_name"
engine = create_engine(f'sqlite:///file:{db_url}?mode=rwc&uri=true', echo=True)
Base = declarative_base()


# conn = engine.connect()
# query = ("CREATE TABLE IF NOT EXISTS people("
#          "id integer primary key autoincrement,"
#          "name text,age integer)")
# conn.execute(text(query))
# conn.execute(text("INSERT INTO people (name, age) VALUES ('Alex', 25);"))
# conn.commit()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    age = Column(Integer, CheckConstraint('age > 0'), default=1)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.name!r}, {self.age})'

    @property
    def is_adult(self):
        return self.age >= 18

    @property
    def greating(self):
        return f"Hello, {self.name}"

    @classmethod
    def display(cls, session):
        people = session.query(cls).all()
        people = [(p, p.is_adult, p.greating) for p in people]
        header = ['Obyekt', 'is_adult', 'greating']
        print(tabulate(people, header, tablefmt='simple_grid'))
        return people

    def save(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def save_all(cls, session, instances):
        session.add_all(instances)
        session.commit()

    @classmethod
    def delete(cls, session, id_):
        obj = session.query(cls).filter(id_ == cls.id).first()
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False

    @classmethod
    def get_by_id(cls, session, id_):
        return session.query(cls).filter(id_ == cls.id).first()

    # update
    @classmethod
    def update(cls, session, id_, **kwargs):
        # obj = session.query(cls).filter(id_ == cls.id).first()
        obj = cls.get_by_id(session, id_)
        if obj:
            for key, value in kwargs.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
                else:
                    raise KeyError(f'`{cls.__name__}` class da  `{key}` attribut mavjud emas!')
            session.commit()
            return True
        return False


Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)
session = Session(bind=engine)
# print(People.display(session))
# p1 = People(name='Billie', age=40)
# p2 = People(name='Billie', age=40)
# print(People.delete(session, id_=7))
# session.add(People(name='Tillabek', age=12))
# session.commit()
# obj = session.query(People).filter(1 == People.id).first()
# session.delete(obj)
# session.commit()

# print(People.update(session, id_=6, name='George', age=34))
# session.add_all([
#     People(name='Akbar', age=20),
#     People(name='Behruz', age=16),
#     People(name='Diyor', age=19)])
# session.commit()
