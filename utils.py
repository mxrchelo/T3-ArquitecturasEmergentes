from db import get_db


def insert_location(company_api_key,company_id, name, country, city, meta):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute( """INSERT INTO locations(company_id, name, country, city, meta) 
                    VALUES (?, ?, ?, ?)""",(company_id, name, country, city, meta)
                    )
        db.commit()
        return True
    else:
        return None


def update_location(company_api_key, id, name, country, city, meta):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute(
           """UPDATE locations SET name = ?, country = ?, city = ?, meta =? WHERE id = ?""",
           (name, country, city, meta, id)
        )
        db.commit()
        return True
    else:
        return None


def delete_location(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute( """DELETE FROM locations WHERE id = ?""",(id))
        db.commit()
        return True
    else:
        return None


def get_location_by_id(company_api_key,id):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute( """SELECT * FROM locations WHERE id = ?""",(id))
        return cursor.fetchone()
    else:
        return None


def get_locations(company_api_key):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}';"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        query = "SELECT * FROM locations"
        cursor.execute(query)
        return cursor.fetchall()
    else:
        return None

#kdvlkñjdgjslkgjhkldfjhgjklghdfkjhdfkjlhgksjhkjsfhkljsgk


def insert_sensor(company_api_key, location_id, name, category, meta, api_key):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute(
            """INSERT INTO sensors(location_id, name, category, meta, api_key)
                VALUES (?, ?, ?, ?)""",(location_id, name, category, meta, api_key)
        )
        db.commit()
        return True
    else:
        return None


def update_sensor(company_api_key, id, location_id, name, category, meta):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute(
           "UPDATE locations SET location_id = ?, name = ?, category = ?, meta =? WHERE id = ?",
           ( location_id, name, category, meta, id))
        db.commit()
        return True
    else:
        return None


def delete_sensor(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute("""DELETE FROM sensor WHERE id = ?""",(id)
        )
        db.commit()
        return True
    else:
        return None
        

def get_sensor_by_id(company_api_key,id):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute( """SELECT * FROM sensors WHERE id = ?""", (id))
        return cursor.fetchone()
    else:
        return None


def get_sensors(company_api_key):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{company_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        query = "SELECT * FROM sensors"
        cursor.execute(query)
        return cursor.fetchall()
    else:
        return None


#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

def insert_sensor_data(sensor_api_key, name, data, date):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{sensor_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute(
            """INSERT INTO sensor_data(name, meta, date)
                VALUES (?, ?, ?, ?)""",(name, data, date)
        )
        db.commit()
        return True
    else:
        return None


def update_sensor_data(sensor_api_key, id, name, data, date):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{sensor_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute(
           "UPDATE locations SET name = ?, data = ?, date = ? WHERE id = ?",
           (name, data, date, id))
        db.commit()
        return True
    else:
        return None


def delete_sensor_data(sensor_api_key, id):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{sensor_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute("""DELETE FROM sensor_data WHERE id = ?""",(id)
        )
        db.commit()
        return True
    else:
        return None
        

def get_sensor_data_by_id(sensor_api_key,id):
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{sensor_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        cursor.execute( """SELECT * FROM sensor_data WHERE id = ?""", (id))
        return cursor.fetchone()
    else:
        return None


def get_list_sensor_data(sensor_api_key, list):
    result = []
    db = get_db()
    cursor = db.cursor()
    auth = f""" SELECT * FROM companies WHERE api_key = '{sensor_api_key}'"""
    cursor.execute(auth)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        for id in list:
            query = cursor.execute( """SELECT * FROM sensor_data WHERE id = ?""", (id))
            cursor.execute(query)
            result.append(cursor.fetchall())
        return result
    else:
        return None
