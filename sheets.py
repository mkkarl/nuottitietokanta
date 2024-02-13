from flask import session
from sqlalchemy import text
from db import db

def new_collection(collection_name, collection_type):
    try:
        sql = text("INSERT INTO sheet_collection (name, type) VALUES (:name, :type)")
        db.session.execute(sql, {"name":collection_name, "type":collection_type})
        db.session.commit()
    except:
        return False
    return True