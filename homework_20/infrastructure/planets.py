class Planet:
    def __init__(self,
                 name,
                 rotation_period,
                 orbital_period,
                 diameter,
                 climate,
                 gravity,
                 terrain,
                 surface_water,
                 population,
                 residents,
                 films,
                 created,
                 edited,
                 url):
        self.name = name
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population
        self.films = films
        self.residents = residents
        self.created = created
        self.created = created
        self.edited = edited
        self.url = url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
