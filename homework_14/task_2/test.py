from homework_14.task_2.csv_manager import CSVManager

class Test_CSV_file:
    def test_add_rows(self):
        csv_manager = CSVManager('test_csv.csv')
        new_data = {'first_name': 'Yulia', 'last_name': 'Hlushko', 'age': 19, 'gender': 'Female', 'salary': 3000}
        csv_manager.add_row(new_data)
        assert csv_manager.check_row_exists(new_data)


    def test_remove_row(self):
        csv_manager = CSVManager('test_csv.csv')
        new_data1 = {'first_name': 'Alona', 'last_name': 'Avtunich', 'age': 29, 'gender': 'Female', 'salary': 1000}
        csv_manager.add_row(new_data1)
        csv_manager.remove_row()
        assert csv_manager.check_row_exists(new_data1)