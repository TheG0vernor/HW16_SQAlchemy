from flask import jsonify
from database import *


def func_iterable(input_):  # функция перебора значений
    list_ = []
    for i in input_:
        list_.append(i.das_dict())  # к переменной перебора применяем метод класса
    return jsonify(list_)


def add_data_user(user):
    for i in user:
        # db.session.add(User(id=i['id'],  ## другой вариант
        #                     first_name=i['first_name'],
        #                     last_name=i['last_name'],
        #                     age=i['age'],
        #                     email=i['email'],
        #                     role=i['role'],
        #                     phone=i['phone']))
        db.session.add(User(**i))  # сам назначит себе те ключи, которые придут. Позволит добавлять пользователя без id.
    db.session.commit()


def upd_data_user(user, pk):
    put_user = User.query.get(pk)
    put_user.id = user['id']
    put_user.first_name = user['first_name']
    put_user.last_name = user['last_name']
    put_user.age = user['age']
    put_user.email = user['email']
    put_user.role = user['role']
    put_user.phone = user['phone']
    db.session.add(put_user)
    db.session.commit()

def delete_data_user(pk):
    del_user = User.query.get(pk)
    db.session.delete(del_user)
    db.session.commit()


def add_data_order(order):
    for i in order:
        db.session.add(Order(**i))
    db.session.commit()


def upd_data_order(order, pk):
    put_order = Order.query.get(pk)
    put_order.id = order['id']
    put_order.name = order['name']
    put_order.description = order['description']
    put_order.start_date = order['start_date']
    put_order.end_date = order['end_date']
    put_order.address = order['address']
    put_order.price = order['price']
    db.session.add(put_order)
    db.session.commit()


def delete_data_order(pk):
    del_order = Order.query.get(pk)
    db.session.delete(del_order)
    db.session.commit()


def add_data_offer(offer):
    for i in offer:
        db.session.add(Offer(**i))
    db.session.commit()


def upd_data_offer(offer, pk):
    put_offer = Offer.query.get(pk)
    put_offer.id = offer['id']
    put_offer.order_id = offer['order_id']
    put_offer.executor_id = offer['executor_id']
    db.session.add(put_offer)
    db.session.commit()


def delete_data_offer(pk):
    del_offer = Offer.query.get(pk)
    db.session.delete(del_offer)
    db.session.commit()
