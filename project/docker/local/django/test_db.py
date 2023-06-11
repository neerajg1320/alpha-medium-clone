import sys
import time
import psycopg2
import environ

env = environ.Env()
print(env("POSTGRES_HOST"))
# exit

suggest_unrecoverable_after = 30
start = time.time()

print("Connecting to postgres database {} on {}".format(env("POSTGRES_DB"), env("POSTGRES_HOST")))
while True:
  try:
    psycopg2.connect(
      dbname=env("POSTGRES_DB"),
      user=env("POSTGRES_USER"),
      password=env("POSTGRES_PASSWORD"),
      host=env("POSTGRES_HOST"),
      port=env("POSTGRES_PORT"),
    )
    print("Connection Successful!")
    break
  except psycopg2.OperationalError as error:
    sys.stderr.write("Waiting for PostgreSQL on {} to become available...\n".format(env("POSTGRES_HOST")))
    if time.time() - start > suggest_unrecoverable_after:
      sys.stderr.write(" This is taking longer than expected. The following exception may be indicative of an unrecoverable error: '{}'\n".format(error))
    time.sleep(1)