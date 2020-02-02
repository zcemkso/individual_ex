"""
Provide Python code to create either a SQLite database or a MySQL database and insert sample data.
Your solution may make use of any appropriate Python package e.g. sqlite3, mysql-connector, sqlalchemy.
The structure of the database must be as follows:

Database name: rain

Table names: user, forecast, city

Columns for user table: user_id (INTEGER PRIMARY KEY), username (TEXT NOT NULL), email (TEXT NOT NULL)

Columns for city table: city_id (INTEGER PRIMARY KEY), city (TEXT NOT NULL)

Columns for forecast table: forecast_id (INTEGER PRIMARY KEY), city_id (INTEGER, Foreign Key), user_id (INTEGER, Foreign Key), forecast_datetime (TEXT NOT NULL), forecast (text not null), comment (TEXT)

Note: SQLite does not have a datetime data type, use TEXT and enter dates as YYYY-MM-DD HH:MM:SS

Insert the following records into each table:
    [user: user_id, username, email]
        1, weatherman, jo@bloggs.com
        2, itrains, itrains@alot.co.uk
        3, sunny, sunny_grl@sunshine.co.uk
    [city: city_id, city]
        1, London
        2, Manchester
        3, Birmingham
        4, Edinburgh
        5, Belfast
        6, Cardiff
    [forecast: forecast_id, city_id, user_id, forecast_datetime, forecast, comment]
        1, 2, 2, 2020-01-27 09:00:00, 'Moderate rain', 'It is really likely to rain today, sorry folks'
        2, 6, 1, 2020-01-27 09:00:00, 'Heavy rain', 'Don't leave home without full waterproofs today!'
        3, 1, 3, 2020-01-27 09:00:00, 'No rain', 'No umbrella required.'

"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///IndEx1.db')

Base = declarative_base()

# Define the classes and tables
class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Forecast(Base):
    __tablename__ = 'forecast'
    forecast_id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('city.city_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    forecast_datetime = Column(String(50), nullable=False)
    forecast = Column(String(50), nullable=False)
    comment = Column(String(100))

class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    User(user_id=1, username='weatherman', email='jo@bloggs.com'),
    User(user_id=2, username='itrains', email='itrains@alot.co.uk'),
    User(user_id=3, username='sunny', email='sunny_grl@sunshine.co.uk'),

    City(city_id=1, city='London'),
    City(city_id=2, city='Manchester'),
    City(city_id=3, city='Birmingham'),
    City(city_id=4, city='Edinburgh'),
    City(city_id=5, city='Belfast'),
    City(city_id=6, city='Cardiff'),

    Forecast(forecast_id=1, city_id=2, user_id=2, forecast_datetime='2020-01-27 09:00:00', forecast='Moderate rain', comment='It is really likely to rain today, sorry folks'),
    Forecast(forecast_id=2, city_id=6, user_id=1, forecast_datetime='2020-01-27 09:00:00', forecast='Heavy rain', comment="Don't leave home without full waterproofs today!"),
    Forecast(forecast_id=3, city_id=1, user_id=3, forecast_datetime='2020-01-27 09:00:00', forecast='No rain', comment='No umbrella required.')
])

session.commit()

session.close()