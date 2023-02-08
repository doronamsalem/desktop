def is_airport_empty(all_took_off, all_landed):
    landed_airplanes = set(all_landed)        # set of the airport in current day
    for airplane in landed_airplanes:
        if all_landed.count(airplane) == all_took_off.count(airplane) + 1:
            return airplane
    return True


def is_airport_empty1(traffic):
    airport_today = set(traffic)
    for airport in airport_today:
        if traffic.count(airport) % 2 != 0:
            return airport
    return True


landed = [1111, 2222, 3333, 1111, 6666]
take_off = [1111, 2222, 1111, 6666]
traffic_today = [1111, 2222, 3333, 1111, 6666, 1111, 2222, 1111, 6666, 3333]

print(is_airport_empty(take_off, landed))
print(is_airport_empty1(traffic_today))
