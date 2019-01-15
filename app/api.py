from app import app
from models import Ad
from models import Customer
from models import Town
from models import Phone
from flask import jsonify
from flask import request
from app import db
import json

#api's for ad
@app.route('/api/ad', methods=['GET'])
def api_ad_get():
    ads = Ad.query.all()
    ads_json = [{"id": ad.id, "customer": ad.customer, "phone": ad.phone, "price": ad.price, "locality": ad.locality}
                  for ad in ads]
    return jsonify(ads_json)

@app.route('/api/ad/<id>', methods=['GET'])
def api_ad_get_id(id):
    ads = Ad.query.filter_by(id=id)
    if not ads:
        abort(404)
    ad = ads[0]
    ad_json = {"id": ad.id, "customer": ad.customer, "phone": ad.phone, "price": ad.price, "locality": ad.locality}
    return jsonify(ad_json)

@app.route('/api/customer', methods=['POST'])
def api_customer_insert():
    new_customer = request.get_json()
    customer = Customer(id=new_customer['id'], name=new_customer['name'])
    db.session.add(customer)
    db.session.commit()
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)

@app.route('/api/ad', methods=['POST'])
def api_ad_insert():
    new_ad = request.get_json()
    ad = Ad(id=new_ad['id'], customer=new_ad['customer'], phone=new_ad['phone'], price=new_ad['price'], locality=new_ad['locality'])
    db.session.add(ad)
    db.session.commit()
    ad_json = {"id": ad.id, "customer": ad.customer, "phone": ad.phone, "price": ad.price, "locality": ad.locality}
    return jsonify(ad_json)

@app.route('/api/ad/<id>', methods=['DELETE'])
def api_ad_delete(id):
    ads = Ad.query.filter_by(id=id)
    if not ads:
        abort(404)
    ad = ads[0]
    db.session.delete(ad)
    db.session.commit()
    return jsonify()

@app.route('/api/ad/<id>', methods=['PUT'])
def api_ad_update(id):
    updated_ad = request.get_json()
    ads_to_update = Ad.query.filter_by(id=id)
    data = json.loads(request.get_data())
    ad_to_update = ads_to_update[0]
    ad_to_update = db.session.query(Ad).filter_by(id = id).first()
    ad_to_update.customer = data['customer']
    ad_to_update.phone = data['phone']
    ad_to_update.price = data['price']
    ad_to_update.locality = data['locality']
    db.session.commit()
    return jsonify(ad_to_update.to_dict())

#api's for customer
@app.route('/api/customer', methods=['GET'])
def api_customer_get():
    customers = Customer.query.all()
    customers_json = [{"id": customer.id, "name": customer.name}
                  for customer in customers]
    return jsonify(customers_json)

@app.route('/api/customer/<id>', methods=['GET'])
def api_customer_get_id(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)


@app.route('/api/customer/<id>', methods=['DELETE'])
def api_customer_delete(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    db.session.delete(customer)
    db.session.commit()
    return jsonify()

@app.route('/api/customer/<id>', methods=['PUT'])
def api_customer_update(id):
    updated_customer = request.get_json()
    customers_to_update = Customer.query.filter_by(id=id)
    data = json.loads(request.get_data())
    customer_to_update = customers_to_update[0]
    customer_to_update = db.session.query(Customer).filter_by(id = id).first()
    customer_to_update.name = data['name']
    db.session.commit()
    return jsonify(customer_to_update.to_dict())

#api's for phone
@app.route('/api/phone', methods=['GET'])
def api_phone_get():
    phones = Phone.query.all()
    phones_json = [{"id": phone.id, "name": phone.name}
                  for phone in phones]
    return jsonify(phones_json)

@app.route('/api/phone/<id>', methods=['GET'])
def api_phone_get_id(id):
    phones = Phone.query.filter_by(id=id)
    if not phones:
        abort(404)
    phone = phones[0]
    phone_json = {"id": phone.id, "name": phone.name}
    return jsonify(phone_json)

@app.route('/api/phone', methods=['POST'])
def api_phone_insert():
    new_phone = request.get_json()
    phone = Phone(id=new_phone['id'], name=new_phone['name'])
    db.session.add(phone)
    db.session.commit()
    phone_json = {"id": phone.id, "name": phone.name}
    return jsonify(phone_json)

@app.route('/api/phone/<id>', methods=['DELETE'])
def api_phone_delete(id):
    phones = Phone.query.filter_by(id=id)
    if not phones:
        abort(404)
    phone = phones[0]
    db.session.delete(phone)
    db.session.commit()
    return jsonify()

@app.route('/api/phone/<id>', methods=['PUT'])
def api_phone_update(id):
    updated_phone = request.get_json()
    phones_to_update = Phone.query.filter_by(id=id)
    data = json.loads(request.get_data())
    phone_to_update = phones_to_update[0]
    phone_to_update = db.session.query(Phone).filter_by(id = id).first()
    phone_to_update.name = data['name']
    db.session.commit()
    return jsonify(phone_to_update.to_dict())

#api's for town
@app.route('/api/town', methods=['GET'])
def api_town_get():
    towns = Town.query.all()
    towns_json = [{"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
                  for town in towns]
    return jsonify(towns_json)

@app.route('/api/town/<id>', methods=['GET'])
def api_town_get_id(id):
    towns = Town.query.filter_by(id=id)
    if not towns:
        abort(404)
    town = towns[0]
    town_json = {"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
    return jsonify(town_json)

@app.route('/api/town', methods=['POST'])
def api_town_insert():
    new_town = request.get_json()
    town = Town(id=new_town['id'], region=new_town['region'], area=new_town['area'], locality=new_town['locality'])
    db.session.add(town)
    db.session.commit()
    town_json = {"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
    return jsonify(town_json)

@app.route('/api/town/<id>', methods=['DELETE'])
def api_town_delete(id):
    towns = Town.query.filter_by(id=id)
    if not towns:
        abort(404)
    town = towns[0]
    db.session.delete(town)
    db.session.commit()
    return jsonify()

@app.route('/api/town/<id>', methods=['PUT'])
def api_town_update(id):
    updated_town = request.get_json()
    towns_to_update = Town.query.filter_by(id=id)
    data = json.loads(request.get_data())
    town_to_update = towns_to_update[0]
    town_to_update = db.session.query(Town).filter_by(id = id).first()
    town_to_update.region = data['region']
    town_to_update.area = data['area']
    town_to_update.locality = data['locality']
    db.session.commit()
    return jsonify(town_to_update.to_dict())
