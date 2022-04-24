import json
import sqlite3

def get_value_from_db(sql):
    with sqlite3.connect('dcim.db') as connect:
        connect.row_factory = sqlite3.Row
        result = connect.execute(sql).fetchall()

    return result


def search_by_status(status):
    response = get_value_from_db(sql=f'''
    SELECT rack.id as rack_id, rack.name as rack_name, customer.name as customer_name, room.name as room_name
    FROM rack
    LEFT JOIN customer ON rack.customer_id = customer.id
    LEFT JOIN room ON rack.room_id = room.id
    WHERE state = '{status}'
    ''')
    status_data = []
    for i in response:
        status_data.append(dict(i))

    return status_data


def search_by_customers():
    pass


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

    return data_size


print(search_by_status('occupied'))
print(search_by_size())