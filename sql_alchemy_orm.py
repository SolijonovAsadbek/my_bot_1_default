from sqlalchemy import (create_engine,
                        text,
                        Column,
                        Text, String, Integer, INT,
                        )
from sqlalchemy.orm import declarative_base, sessionmaker

# from sqlalchemy.ext.declarative import declarative_base
# sqlite, postgres, mysql
db_url = 'database.db'

engine = create_engine(f'sqlite:///{db_url}', echo=True)
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
    name = Column(String(50), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.name!r}, {self.age})'


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
print(session.query(People).all())
# p1 = People(name='John', age=30)
# session.add(p1)
# session.commit()
