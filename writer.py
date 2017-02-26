import uuid
import random
import sys
import select
import os
import datetime

# Imports the Google Cloud Client Library.
from google.cloud import spanner


def run_writer():
    
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
        data = 'a' * 2000
        values = []
        row_id = (uuid.uuid4().int & (1<<63)-1)
        for i in range(500):
            row_id += 1
            utilization = random.randint(0,100)
            ts = datetime.datetime.now()
            values.append((row_id, data, ts, utilization))
        with database.batch() as batch:
            batch.insert(
                table='cpu',
                columns=('id', 'data', 'ts', 'utilization'),
                values=values)


if __name__ == '__main__':
    run_writer()
