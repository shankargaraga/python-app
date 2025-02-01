'''
load emps.csv file into memory and read all the data from the file and remove email column
and remaining data write it in another file
use loggging
'''

import csv

with open("emps.csv", "r") as file_reader:
    csv_data = csv.DictReader(file_reader)  # csv_data depends on file_reader being open
    with open("newemps.csv", "w", newline="") as file_writer:  # Added newline=""
        columns = ['fname', 'lname']
        csv_write = csv.DictWriter(file_writer, fieldnames=columns, delimiter=',')
        csv_write.writeheader()

        for row in csv_data:
            del row['email']
            csv_write.writerow(row)  # Move this inside the loop

print("processing done")
