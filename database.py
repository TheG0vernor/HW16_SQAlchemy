from functions import *
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'  # таблица пользователей
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(100))
    last_name = db.Column(db.Text(100))
    age = db.Column(db.Integer)
    email = db.Column(db.Text(50))
    role = db.Column(db.Text(10))
    phone = db.Column(db.Text(12))

    def das_dict(self):  # чтобы при необходимости получить данные таблицы в словаре
        return {"id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
                "email": self.email,
                "role": self.role,
                "phone": self.phone}


class Order(db.Model):
    __tablename__ = 'order'  # таблица ордеров
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(50))
    description = db.Column(db.Text(200))
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.Text(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        f'{User.__tablename__}.id'))  # tablename - чтобы игнорировать название таблицы
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    def das_dict(self):
        return {'id': self.id,
                'name': self.name,
                'description': self.description,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'address': self.address,
                'price': self.price,
                'customer_id': self.customer_id,
                'executor_id': self.executor_id}


class Offer(db.Model):
    __tablename__ = 'offer'  # таблица офферов
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(f'{Order.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))
    order = relationship('Order')
    user = relationship('User')

    def das_dict(self):
        return {'id': self.id,
                'order_id': self.order_id,
                'executor_id': self.executor_id}


@app.route('/users/', methods=['GET', 'POST'])
def user_output():
    if request.method == 'GET':
        return func_iterable(User.query.all())  # выгрузим user'ов из таблицы
    elif request.method == 'POST':  # должен поступить список со словарём, иначе завернуть словарь в список
        if type(request.json) == list:
            add_data_user(request.json)
        elif type(request.json) == dict:
            add_data_user([request.json])


@app.route('/users/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def user_output_pk(pk):
    if request.method == 'GET':
        if db.session.query(User).filter(User.id == pk).first():  # фильтр по значению
            return jsonify(db.session.query(User).filter(User.id == pk).first().das_dict())
        else:
            return '<h3>Нет такого user`a</h3>'
    elif request.method == 'PUT':  # обновление user'а
        upd_data_user(request.json, pk)
    elif request.method == 'DELETE':  # удаление user'а
        delete_data_user(pk)


@app.route('/orders/', methods=['GET', 'POST'])
def order_output():
    if request.method == 'GET':
        return func_iterable(Order.query.all())
    elif request.method == 'POST':
        if type(request.json) == list:
            add_data_order(request.json)
        elif type(request.json) == dict:
            add_data_order([request.json])


@app.route('/orders/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def order_output_pk(pk):
    if request.method == 'GET':
        if db.session.query(Order).filter(Order.id == pk).first():  # фильтр по значению
            return jsonify(db.session.query(Order).filter(Order.id == pk).first().das_dict())
        else:
            return '<h3>Нет такого ордера</h3>'
    elif request.method == 'PUT':  # обновление order'а
        upd_data_order(request.json, pk)
    elif request.method == 'DELETE':  # удаление order'а
        delete_data_order(pk)


@app.route('/offers/', methods=['GET', 'POST'])
def offer_output():
    if request.method == 'GET':
        return func_iterable(Offer.query.all())
    elif request.method == 'POST':
        if type(request.json) == list:
            add_data_offer(request.json)
        elif type(request.json) == dict:
            add_data_offer([request.json])


@app.route('/offers/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def offer_output_pk(pk):
    if request.method == 'GET':
        if db.session.query(Offer).filter(Offer.id == pk).first():  # фильтр по значению
            return jsonify(db.session.query(Offer).filter(Offer.id == pk).first().das_dict())
        else:
            return '<h3>Нет такого оффера</h3>'
    elif request.method == 'PUT':  # обновление offer'а
        upd_data_offer(request.json, pk)
    elif request.method == 'DELETE':  # удаление offer'а
        delete_data_offer(pk)


if __name__ == '__main__':
    app.run()
