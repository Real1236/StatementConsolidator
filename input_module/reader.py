import os
import csv
from filter import Filter

class Reader(Filter):
    def process(self, data):
        # Get the directory where the script is located
        directory = os.path.dirname(os.path.realpath(__file__))

        # Get a list of all files in the directory
        all_files = os.listdir(directory)

        # Filter the list to only include .csv files
        csv_files = [file for file in all_files if file.endswith('.csv')]

        # Create a dictionary to store the file contents
        file_contents = {}

        # For each .csv file, read the file
        for csv_file in csv_files:
            with open(os.path.join(directory, csv_file), 'r') as file:
                reader = csv.reader(file)
                file_contents[csv_file] = list(reader)

        return file_contents
