import json
import csv

class Convert_json_to_csv:
    def __init__(self, json_file, csv_file):
        self.json_file = json_file
        self.csv_file = csv_file

    def convert(self):
        with open(self.json_file, 'r') as jsonfile:
            data = json.load(jsonfile)

        with open(self.csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(data)

        print(f'You can find generated csv in {self.csv_file}')

# Usage
converter = Convert_json_to_csv('example.json', 'new_example.csv')
converter.convert()