import csv

class CSVManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def add_row(self, data_dict):
        with open(self.csv_file, 'a', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=data_dict.keys())
            csv_writer.writerow(data_dict)
        print("Row added successfully.")


    def remove_row(self):
        rows = []
        with open(self.csv_file, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            rows = [row for row in csv_reader]

        if rows:
            rows.pop()

        with open(self.csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(rows)
        print("Last row removed successfully.")


    def check_row_exists(self, data_dict):
        with open(self.csv_file, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                if all(row[key] == value for key, value in data_dict.items()):
                    return True
            return True



