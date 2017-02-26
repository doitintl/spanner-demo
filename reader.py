import time
import sys
import select
import os
from datetime import datetime, timedelta


# Imports the Google Cloud Client Library.
from google.cloud import spanner

def run_reader():
    # Instantiate a client.
    spanner_client = spanner.Client()

    # Your Cloud Spanner instance ID.
    instance_id = 'meetup'

    # Get a Cloud Spanner instance by ID.
    instance = spanner_client.instance(instance_id)

    # Your Cloud Spanner database ID.
    database_id = 'performance-log'

    # Get a Cloud Spanner database by ID.
    database = instance.database(database_id)
    while True:
        start_time = datetime.now()
        query = 'select count(*),AVG(utilization) from cpu where TIMESTAMP_TRUNC(ts,MINUTE) = TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(),MINUTE)'
        results = database.execute_sql(query)
        end_time = datetime.now()
        for row in results:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('AVG CPU Util.: ' + str(row[1]))
            print('latency: %s' % ((end_time - start_time).microseconds / 1000.0))
            print('Rows (1 minute): %s' % (row[0]))

if __name__ == '__main__':
    run_reader()
