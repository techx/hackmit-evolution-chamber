from database import get_db


class Stats:

    @staticmethod
    def increment():
        cursor = get_db().cursor()
        cursor.execute('UPDATE stats SET num_decisions = %d WHERE 1 == 1' % (Stats.num() + 1))
        get_db().commit()

    @staticmethod
    def reset():
        cursor = get_db().cursor()
        cursor.execute('UPDATE stats SET num_decisions = 0 WHERE 1 == 1')
        get_db().commit()

    @staticmethod
    def num():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT num_decisions FROM stats;')
        return cursor.fetchone()[0]
