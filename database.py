from sqlalchemy import create_engine, text

import os

my_secret = os.environ['DB_CON']
db_con = my_secret[1:-1]
engine = create_engine(db_con,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    keys = ['id', 'title', 'location', 'salary', 'currency', 'description']
    result_dicts = []
    result_dicts = [dict(zip(keys, row)) for row in result]
    return result_dicts
