from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False)


class Forecast(db.Model):
    __tablename__ = 'forecast'
    __table_args__ = {'extend_existing': True}
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    forecast_datetime = db.Column(db.String(50), nullable=False)
    forecast = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(100))


class City(db.Model):
    __tablename__ = 'city'
    __table_args__ = {'extend_existing': True}
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
