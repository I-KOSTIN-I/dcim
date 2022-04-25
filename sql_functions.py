import json
import sqlite3

from flask import jsonify


def get_value_from_db(sql):
    with sqlite3.connect('dcim.db') as connect:
        connect.row_factory = sqlite3.Row
        result = connect.execute(sql).fetchall()

    return result


def search_by_status():
    response = get_value_from_db(sql=f'''
    SELECT rack.id as rack_id, rack.name as rack_name, customer.name as customer_name, room.name as room_name
    FROM rack
    LEFT JOIN customer ON rack.customer_id = customer.id
    LEFT JOIN room ON rack.room_id = room.id
    WHERE state = 'occupied'
    ''')
    status_data = []
    for i in response:
        status_data.append(dict(i))

    return json.dumps(status_data, ensure_ascii=False)


def search_by_customers():
    response = get_value_from_db(sql=f'''
    SELECT room.id as room_id, room.name as room_name, json_group_array(customer.id) as customer_id
    FROM rack
    LEFT JOIN customer ON rack.customer_id = customer.id
    LEFT JOIN room ON rack.room_id = room.id
    GROUP BY room.id
    ''')
    customers_data = []
    for i in response:
        customers_data.append(dict(i))

    return json.dumps(customers_data, ensure_ascii=False)


def search_by_size():
    response = get_value_from_db(sql=f'''
    SELECT room.id as room_id, rack.id as rack_id, max(rack.size) as rack_max_size
    FROM rack
    LEFT JOIN customer ON rack.customer_id = customer.id
    LEFT JOIN room ON rack.room_id = room.id
    GROUP BY room.id  
    ''')
    data_size = []
    for i in response:
        data_size.append(dict(i))

    return json.dumps(data_size, ensure_ascii=False)


print(search_by_status())
print(search_by_size())
print(search_by_customers())