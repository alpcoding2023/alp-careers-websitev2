from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://0szyl1rs15zyeoxaqbwu:pscale_pw_NesTiVWe2N9wBxmLxiZtDORyJsl4oGNklr1JfE5ED49@aws.connect.psdb.cloud/alpcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(dict(row))

  print(result_dicts)
