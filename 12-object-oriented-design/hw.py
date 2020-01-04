"""
calculates amount of time to deliver container from factory according give list
"""

class Transport:
    def __init__(self, location):
        self.location = location
        self.oper_time = 0

    def travel(self, trav_time):
        self.oper_time += trav_time


class Truck(Transport):
    def __init__(self, location, dest_list):
        self.destinations = dest_list
        super().__init__(location)

    def deliver(self, destination):
        self.location = destination
        self.oper_time += points_distances[destination]

    def way_back(self, back_from):
        self.location = 'factory'
        self.oper_time += points_distances[back_from]


class Ship(Transport):
    def __init__(self, location, dest_list):
        self.destinations = dest_list
        super().__init__(location)

    def deliver(self, destination):
        self.location = destination
        self.oper_time += points_distances[destination]

    def way_back(self, back_from):
        self.location = 'port'
        self.oper_time += points_distances[back_from]


points_distances = {
    'A': 4,
    'port': 1,
    'B': 5
}


def est_count(this, remain_list, transport_arr):    
    trucks = []

    for i in transport_arr:
        if isinstance(i, Truck):
            trucks.append(i.location)

    for c in set(remain_list):
        est_time = remain_list.count(c) \
                    * points_distances[c] \
                    * (len(trucks) - 1)
        if est_time > points_distances[this]:
            return True

    return False


class Deliver:
    def __init__(self, transport):
        self.transport = transport

    def calculate_time(self, deliv_string):
        to_deliver = [c for c in deliv_string]
        for t in self.transport:
            t.oper_time = 0
            if isinstance(t, Truck):
                t.location = 'factory'
            elif isinstance(t, Ship):
                t.location = 'port'
        port_stack = []
        elaps_time = 0

        while to_deliver:
            for t in self.transport:
                if isinstance(t, Truck):
                    if t.location == 'factory':
                        if t.oper_time <= elaps_time:
                            curr = to_deliver.pop(0)
                            if curr == 'A':
                                t.deliver('port')
                                port_stack.append((curr, t.oper_time))
                            else:
                                t.deliver(curr)
                            if not to_deliver:
                                break
                    if t.location != 'factory' \
                        and len(to_deliver) > 0 \
                        and est_count(t.location, to_deliver, self.transport):
                        t.way_back(t.location)
            elaps_time += 1

        while port_stack:
            for s in self.transport:
                if isinstance(s, Ship):
                    if s.location == 'port':
                        port_deliv = port_stack.pop(0)
                        if s.oper_time < port_deliv[1]:
                            s.oper_time = port_deliv[1]
                        s.deliver(port_deliv[0])
                    elif len(port_stack) > 0:
                        s.way_back(s.location)

        return max([t.oper_time for t in self.transport])

truck1 = Truck('factory', ['port', 'B'])
truck2 = Truck('factory', ['port', 'B'])
boat = Ship('port', ['A'])
deliv_pattern = Deliver([truck1, truck2, boat])


assert deliv_pattern.calculate_time('A') == 5
assert deliv_pattern.calculate_time('AB') == 5
assert deliv_pattern.calculate_time('BB') == 5
assert deliv_pattern.calculate_time('ABB') == 7
deliv_pattern.calculate_time('AABABBAB')
deliv_pattern.calculate_time('ABBBABAAABBB')
