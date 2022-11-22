"""
Multiply developer skill assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file and other files within this repository are used for a developer skill
assessment by Multiply (multiply.cloud).

If you have been asked to attempt this assessment, you are free to modify 
any of the files or even create new files if necessary in order to get the 
outcome required in this task.
"""
import datetime
import os
import random

from batchers import create_batches

num_days = 7

# for small db
# datafile = "db.csv"
# DAILY_BATCHES = 3  # A batch every 4 hours
# MAX_BATCH_SIZE = 2

# for large db
datafile = "db_large.csv"
DAILY_BATCHES = 30
MAX_BATCH_SIZE = 8

curr_datetime = datetime.datetime.now()

# Create batches for the next num_days days
for i in range(num_days):

    # Notify day in range
    print("\n===================")
    print("Batches for Day: {}".format(i + 1))

    # Add your create_batches args here
    daily_batch = create_batches(i+1, DAILY_BATCHES, MAX_BATCH_SIZE, datafile, curr_datetime)
    print("Batches for day {}:".format(1 + 1) + str(daily_batch))

# TODO: Save info about your batch to a file
# with open("new" + datafile, 'w') as batches:
#     fieldnames = ['Product', 'Frequency']
#
#     csv_writer = csv.writer(batches, fieldnames=fieldnames)
#
#     csv_writer.writeheader()

curr_datetime += datetime.timedelta(days=1)
