from abc import ABC, abstractclassmethod

class Aircraft(ABC):
    def __init__(self, number_of_passengers, name):
        self._number_of_passengers = number_of_passengers
        self._name = name

    def get_number_of_passengers(self):
        return self._number_of_passengers

    def get_name(self):
        return self._name

    @abstractclassmethod
    def calculate_amount_of_fuel(self, km):
        pass

    @abstractclassmethod
    def manifest(self):
        pass


class IntercontinentalAircraft(Aircraft):
    def __init__(self, number_of_passengers, name, cargo_hold):
        super().__init__(number_of_passengers, name)
        self.__cargo_hold = cargo_hold

    def calculate_amount_of_fuel(self, km):
        self.fluel = int((0.25 * km * self._number_of_passengers) + (2 * km * self.__cargo_hold))
        return self.fluel
    @property
    def manifest(self):
        return "Intercontinental flight %s: passenger count %s, cargo load %s" %(Aircraft._name, Aircraft._number_of_passengers, self.__cargo_hold)


class ShortHaulAircraft(Aircraft):
    serial_number = -1
    def __init__(self, number_of_passengers , name):
        super().__init__(number_of_passengers, name)


    def get_serial_number(self):
        ShortHaulAircraft.serial_number +=1
        return ShortHaulAircraft.serial_number

    def calculate_amount_of_fuel(self, km):
        self.fluel = int(0.1 * km * self._number_of_passengers)
        return self.fluel

    @property
    def manifest(self):
        return "Short haul flight serial number %s, name %s: passenger count %s" \
               %(self.serial_number, self._name, self._number_of_passengers)

class ControlTower(IntercontinentalAircraft, ShortHaulAircraft):
    aircrafts = []

    def __init__(self):
        pass

    def add_aircraft(self, aircraft):
        self.aircraft = aircraft
        ControlTower.aircrafts.append(aircraft)

    def get_manifests(self):
        self.manifest_list = []
        for aircraft in ControlTower.aircrafts:
            manifest = super().manifest(aircraft)
            self.manifest_list.append(manifest)
            return self.manifest_list


if __name__ == '__main__':
    intercontinental_flight = IntercontinentalAircraft(500, "Boeing-747", 100)
    short_haul_flight = ShortHaulAircraft(110, "Airbus-A220")
    short_haul_flight2 = ShortHaulAircraft(85, "Airbus-A220")

    assert short_haul_flight.get_serial_number() == 0
    assert short_haul_flight2.get_serial_number() == 1

    assert short_haul_flight.get_number_of_passengers() == 110
    assert short_haul_flight.get_name() == "Airbus-A220"

    assert intercontinental_flight.get_number_of_passengers() == 500
    assert intercontinental_flight.get_name() == "Boeing-747"

    assert intercontinental_flight.calculate_amount_of_fuel(10000) == 3250000.
    assert short_haul_flight.calculate_amount_of_fuel(250) == 2750.

    assert intercontinental_flight.manifest == "Intercontinental flight Boeing-747: passenger count 500, cargo load 100"
    assert short_haul_flight2.manifest == "Short haul flight serial number 1, name Airbus-A220: passenger count 85"

    tower = ControlTower()
    tower.add_aircraft(intercontinental_flight)
    tower.add_aircraft(short_haul_flight)
    tower.add_aircraft(short_haul_flight2)

    air_traffic_report = tower.get_manifests()
    for aircraft in air_traffic_report:
        print(aircraft)

    # prints:
    # Intercontinental flight Boeing-747: passenger count 500, cargo load 100
    # Short haul flight serial number 0, name Airbus-A220: passenger count 110
    # Short haul flight serial number 1, name Airbus-A220: passenger count 85
