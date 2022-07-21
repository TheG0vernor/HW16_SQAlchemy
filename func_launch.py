import json

from database import *

db.drop_all()
db.create_all()


# запустите файл для создания/заполнения базы


def user_data():
    with open('DATA/data_users.json', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        db.session.add(
            User(id=i['id'], first_name=i['first_name'], last_name=i['last_name'], age=i['age'],
                 email=i['email'], role=i['role'], phone=i['phone']))
        # или User(**i)
    db.session.commit()


def offer_data():
    with open('DATA/data_offers.json', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        db.session.add(
            Offer(id=i['id'], order_id=i['order_id'], executor_id=i['executor_id']))
        # или User(**i)
    db.session.commit()


def order_data():
    with open('DATA/data_orders.json', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        db.session.add(
            Order(id=i['id'], name=i['name'], description=i['description'], start_date=i['start_date'],
                  end_date=i['end_date'], address=i['address'], price=i['price'], customer_id=i['customer_id'],
                  executor_id=i['executor_id']))
        # или User(**i)
    db.session.commit()


user_data()
order_data()
offer_data()
