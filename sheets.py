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

def get_collections():
    try:
        sql = text("SELECT id, name, type FROM sheet_collection")
        result = db.session.execute(sql)
        collections = result.fetchall()
        return collections
    except:
        return False
    
def get_collection(id):
    try:
        sql = text("SELECT id, name, type FROM sheet_collection WHERE id=:id")
        result = db.session.execute(sql, {"id":id})
        collection = result.fetchone()
        return collection
    except:
        return False

def get_sheets(collection_id):
    try:
        sql = text("SELECT id, name, composer, writer, arranger, creator, artist FROM sheet " \
                   "WHERE collection_id=:collection_id")
        result = db.session.execute(sql, {"collection_id":collection_id})
        coll_sheets = result.fetchall()
        return coll_sheets
    except:
        return False