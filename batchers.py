import math
from typing import List
from csv import DictReader

from Product import Product


def create_batches(
        day_num,
        num_batches,
        max_batch_size,
        datafile,
) -> List[str]:
    """
    Create a required number of scraping batches. Presumed this will be run once daily

    :param day_num: The specific day number
    :param datafile: The name of the data file passed from main
    :param num_batches: Total number of batches to create. Assumed to be a daily value
    :param max_batch_size: Maximum size of each batch. actual size <= max_batch_size

    Add more params as you may require:
    :raises ValueError: if the defined num_batches <= 0 or max_batch_size < 1
    """

    # Read file data
    file_handler = open(datafile, 'r')
    csv_reader = DictReader(file_handler)

    prods = []
    for line in csv_reader:
        new_prod = Product(line['Product'], float(line['Frequency']))
        prods.append(new_prod)

    file_handler.close()

    if num_batches <= 0:
        raise ValueError(
            "Cannot have 0 or negative number of batches. Current number: {}".format(
                num_batches
            )
        )
    if max_batch_size < 1:
        raise ValueError(
            "Cannot have 0 or negative maximum batch size. Current number: {}".format(
                max_batch_size
            )
        )

    # You will need to fake moving time forward. You are free to decide
    # How small/big each time step will be
    hour = 0
    minute = 0
    interval = ((24 / num_batches) * 60)

    # List to hold all the batches per day
    batches = []

    for i in range(num_batches):
        # Call the create_batch function
        time = str("{}".format(hour) + ":" + "{}".format(int(minute)))

        print("Batch number {}".format(i + 1), "of {}".format(num_batches), "at {}".format(time))
        batch = create_batch(day_num, num_batches, max_batch_size, prods)

        # Add created batch to existing batches
        batches.append(batch)

        minute += interval
        if minute >= 60:
            # Increase hours
            hour += 1
            minute = minute - 60

        # curr_datetime += time_step
        # create_batch_kwarg["current_datetime"] = curr_datetime

    return batches


def create_batch(
        day_num,
        number_of_batches,  # Total number of batches
        max_batch_size,  # Max number of products per batch
        products,  # List of products
) -> str:
    # Your code here ...

    for b in range(number_of_batches):
        batch_counter = 0

        # Fot the string of products in the batch
        batch = ""

        # Check if max is reached
        for prod in products:
            if batch_counter < max_batch_size:
                # Get current product frequency
                prod_frequency = prod.product_frequency

                # Check frequency
                if prod_frequency >= 1.0:
                    batch += prod.product_name + ","

                    # Increase the batch counter
                    batch_counter += 1

                    # Decrement product frequency
                    prod.product_frequency = prod_frequency - 1
                else:
                    # Check original frequency
                    if prod.product_frequency < 1:
                        if prod.product_frequency > 0:

                            # Invert decimal
                            new_freq = (math.floor(1 / prod.product_frequency))

                            if (day_num % new_freq) == 0:
                                batch += prod.product_name + ","

                                # Set product frequency to zero
                                prod.product_frequency = 0

                                # Increase the batch counter
                                batch_counter += 1

        new_batch = batch[:-1]
        print('[' + new_batch + ']')

        return new_batch
