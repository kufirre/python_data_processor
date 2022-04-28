import csv

# List to hold the column we want to report
reported_column = []

# List to hold the column we are monitoring for changes
monitored_column = []

# List to hold the values of the desired column where changes are observed
reported_values = []

# Open the csv file to fetch the contents of the column we want to report
with open('Sensor_Data_1.csv', 'r') as csv_file:
    dict_reader = csv.DictReader(csv_file)

    # Get fieldnames from DictReader object and store in list
    headers = dict_reader.fieldnames

    # Create a list comprehension to contain the values of the column we want to report where  changes occur
    reported_column = [value[headers[0]] for value in dict_reader]

# Open the csv file again; this time to fetch the contents of the column we want to monitor
with open('Sensor_Data_1.csv', 'r') as csv_file:
    dict_reader2 = csv.DictReader(csv_file)

    # Get fieldnames from DictReader object and store in list
    headers = dict_reader2.fieldnames

    # Create a list comprehension to contain the values of the column we want to check where  changes occur
    monitored_column = [(values[headers[3]]) for values in dict_reader2]


with open('report.csv', 'w', newline='') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(['Event', 'Event Start Time', 'Event End Time'])
    for i, value in enumerate(monitored_column):

        # Create CSV file (report.csv) containing event - monitored_column[i+2], event start reported_column[i], event end - reported_column[i+2]
        # This would ignore the last 2 lines
        if i < len(monitored_column) - 2:

            # This is done to skip empty lines
            if value != '':

                # The next value is 2 lines ahead of the current value
                next_value = monitored_column[i+2]

                # If there is a difference between the next value and the previous value
                if float(next_value) - float(value) != 0:
                    # print(reported_column[i+2])           # uncomment this line to print the values individually
                    reported_values.append(reported_column[i+2])
                    writer.writerow([monitored_column[i+2], reported_column[i], reported_column[i+2]])

# list of values required
print("This list of values where changes occurred: {}".format(reported_values))
