class Car_Owner:
    _instance = None
    _owner_data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._owner_data = {}
        return cls._instance

    def set_data(self, key, value):
        self._owner_data[key] = value

    def get_data(self, key):
        return self._owner_data.get(key)


# Usage
owner_data_1 = Car_Owner()
owner_data_1.set_data("owner_name", "Yulia Hlushko")
print(owner_data_1.get_data("owner_name"))

owner_data_2 = Car_Owner()
owner_data_2.set_data("owner_name", "Olena Kravchenko")
print(owner_data_2.get_data("owner_name"))

print(owner_data_1 is owner_data_2)