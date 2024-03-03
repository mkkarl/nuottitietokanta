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
    
def new_sheet(collection_id, name, composer, writer, arranger, creator, artist):
    try:
        sql = text("""INSERT INTO sheet (collection_id, name, composer, writer, arranger, creator, artist)
                   VALUES (:collection_id, :name, :composer, :writer, :arranger, :creator, :artist)""")
        db.session.execute(sql, {"collection_id":collection_id, "name":name, "composer":composer, "writer":writer, "arranger":arranger, "creator":creator, "artist":artist})
        db.session.commit()
    except:
        return False
    return True

def get_all_sheets():
    try:
        sql = text("SELECT S.id, S.name, S.composer, S.writer, S.arranger, S.creator, S.artist, C.id AS coll_id, C.name AS coll_name " \
                   "FROM sheet S, sheet_collection C " \
                   "WHERE S.collection_id = C.id")
        result = db.session.execute(sql)
        coll_sheets = result.fetchall()
        return coll_sheets
    except:
        return False
    
def add_collection_owner(user_id, collection_id):
    try:
        sql = text("""INSERT INTO collection_owner (collection_id, user_id) 
                    VALUES (:collection_id, :user_id)""")
        db.session.execute(sql, {"collection_id":collection_id, "user_id":user_id})
        db.session.commit()
    except:
        return False
    return True

def get_collection_owners(collection_id):
    try:
        sql = text("""SELECT CO.user_id AS user_id, U.username AS name
                   FROM collection_owner CO, users U
                   WHERE CO.collection_id=:collection_id AND U.id=CO.user_id""")
        result = db.session.execute(sql, {"collection_id":collection_id})
        owners = result.fetchall()
        return owners
    except:
        return False

def is_collection_owner(collection_id, user_id):
    try:
        sql = text("""SELECT user_id, collection_id
                   FROM collection_owner
                   WHERE collection_id=:collection_id AND user_id=:user_id""")
        result = db.session.execute(sql, {"collection_id":collection_id, "user_id":user_id})
        rows = len(result.fetchall())
        if rows > 0:
            return True
        else:
            return False
    except:
        return False