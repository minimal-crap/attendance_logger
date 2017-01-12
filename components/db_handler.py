import uuid
import datetime

from sqlalchemy import create_engine
from conf.settings import db_settings as dbs
from components.models import Employee

database_url = "{0}://{1}:{2}@{3}:{4}/{5}".format(dbs['vendor'],
                                                  dbs['user'],
                                                  dbs['password'],
                                                  dbs['host'],
                                                  dbs['port'],
                                                  dbs['db'])

engine = create_engine(database_url)


def create_employee_table():
    try:
        if not engine.dialect.has_table(engine,
                                        Employee.__tablename__):
            employee_obj = Employee()
            employee_obj.metadata.create_all(engine)

    except Exception as err:
        print err.message


def save_employee_data(data):
    try:
        conn = engine.connect()
        current_time = str(datetime.datetime.now())
        checkin_id = str(uuid.uuid4())
        sql_string = "insert into {0} values({1}, {2}, {3}, {4}, {5})".format(checkin_id,
                                                                              data['name'],
                                                                              data['designation'],
                                                                              data['department'],
                                                                              current_time)
    except Exception as err:
        print err.message

