import sqlite3
from flask import g, Flask
from constants import Constants
import json

DATABASE = 'db/sqlite.db'

app = Flask(Constants.APP_NAME)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def serialize_result_to_individual(res,idname="id"):
    return {idname: res[0], "parameters":json.loads(res[1]), "elo": res[2]}

class Database:

    @staticmethod
    def incr_comparisons():
        cursor = get_db().cursor()
        cursor.execute('UPDATE stats SET num_comparisons = %d WHERE 1 == 1' % (Database.num_comparisons() + 1))
        get_db().commit()

    @staticmethod
    def reset_comparisons():
        cursor = get_db().cursor()
        cursor.execute('UPDATE stats SET num_comparisons = 0 WHERE 1 == 1')
        get_db().commit()

    @staticmethod
    def num_comparisons():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT num_comparisons FROM stats;')
        return cursor.fetchone()[0]

    @staticmethod
    def current_generation_is_empty():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM current')
        return not cursor.fetchone()

    @staticmethod
    def add_individual_to_current_generation(parameters):
        string = json.dumps(parameters)
        cursor = get_db().cursor()
        cursor.execute('INSERT INTO current (parameters, elo) VALUES (?, 1000.0)', (string,))
        get_db().commit()

    @staticmethod
    def get_individual_for_id(idd):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT id, parameters, elo FROM current WHERE id = ?', (idd,))
        return serialize_result_to_individual(cursor.fetchone())

    @staticmethod
    def update_elo_for_id(idd, elo):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE current SET elo = ? WHERE id = ?', (elo, idd))
        db.commit()

    @staticmethod
    def get_all_individuals_sorted():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT id, parameters, elo FROM current ORDER BY elo DESC')
        return [serialize_result_to_individual(res) for res in cursor.fetchall()]

    @staticmethod
    def get_random_individuals(num):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT id, parameters, elo FROM current ORDER BY RANDOM() LIMIT ?', (num,))
        return [serialize_result_to_individual(res) for res in cursor.fetchall()]

    @staticmethod
    def delete_individuals(individuals):
        cursor = get_db().cursor()
        id_list = ", ".join(map(lambda x: str(x["id"]), individuals))
        cursor.execute('DELETE FROM current WHERE id IN (%s)' % id_list)
        get_db().commit()

    @staticmethod
    def get_historical_individuals():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT gen, parameters, elo FROM historical ORDER BY gen')
        return [serialize_result_to_individual(res,"gen") for res in cursor.fetchall()]

    @staticmethod
    def add_historical_individual(individual):
        string = json.dumps(individual['parameters'])
        elo = individual['elo']
        cursor = get_db().cursor()
        cursor.execute('INSERT INTO historical (parameters, elo) VALUES (?, ?)', (string,elo))
        get_db().commit()
