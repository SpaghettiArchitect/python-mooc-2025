import math


def main() -> None:
    stations = get_station_data("stations1.csv")
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    print()
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)


def get_station_data(filename: str) -> dict:
    all_stations = {}

    with open(filename) as stations_file:
        for station in stations_file:
            station_data = station.strip().split(";")

            if station_data[0] == "Longitude":
                continue

            longitude = float(station_data[0])
            latitude = float(station_data[1])
            name = station_data[3]

            all_stations[name] = (longitude, latitude)

    return all_stations


def distance(stations: dict, station1: str, station2: str) -> float:
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict) -> tuple[str, str, float]:
    result = ("", "", 0)
    for station1 in stations:
        for station2 in stations:
            if station1 == station2:
                continue
            current_distance = distance(stations, station1, station2)
            if current_distance > result[2]:
                result = (station1, station2, current_distance)

    return result


# main()
