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
    keys = [
      'id', 'title', 'location', 'salary', 'currency', 'responsibilities',
      'requirements'
    ]
    result_dicts = []
    result_dicts = [dict(zip(keys, row)) for row in result]
    return result_dicts


def load_job_from_db(id):
  with engine.connect() as conn:
    stmt = text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id)
    result = conn.execute(stmt)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      keys = [
        'id', 'title', 'location', 'salary', 'currency', 'responsibilities',
        'requirements'
      ]
      result_dicts = []
      result_dicts = [dict(zip(keys, row)) for row in rows]
      return result_dicts


def add_applcn_to_db(id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    conn.execute(query,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])
