"""
Multiply developer skill assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file and other files within this repository are used for a developer skill
assessment by Multiply (multiply.cloud).

If you have been asked to attempt this assessment, you are free to modify 
any of the files or even create new files if necessary in order to get the 
outcome required in this task.
"""
import csv
import datetime

from batchers import create_batches

num_days = 7

# for small db
datafile = "db.csv"
DAILY_BATCHES = 3
MAX_BATCH_SIZE = 2

# for large db
# datafile = "db_large.csv"
# DAILY_BATCHES = 30
# MAX_BATCH_SIZE = 8

curr_datetime = datetime.datetime.now()

with open("batch_list.csv", 'w') as new_file:

    csv_writer = csv.writer(new_file)

    # Create batches for the next num_days days
    for i in range(num_days):
        # Notify day in range
        print("\n===================")
        print("Batches for Day: {}".format(i + 1))

        # Add your create_batches args here
        daily_batch = create_batches(i + 1, DAILY_BATCHES, MAX_BATCH_SIZE, datafile)
        print("Batches for day {}:".format(i + 1) + str(daily_batch))

        csv_writer.writerow(daily_batch)

curr_datetime += datetime.timedelta(days=1)
