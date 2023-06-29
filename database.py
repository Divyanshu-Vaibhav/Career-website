
from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://zralbx0ptj8mnr1d3r8j:pscale_pw_PQ9n3SHHkeO6FIGwkulMUsTit6Dgin8fbqqascoYvq2@aws.connect.psdb.cloud/steamcareers?charset=utf8mb4",connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
           
        }
    })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    keys = ['id', 'title', 'location', 'salary', 'currency', 'description']
    result_dicts = []
    result_dicts = [dict(zip(keys, row)) for row in result]
    return result_dicts