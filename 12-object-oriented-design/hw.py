"""
calculates amount of time required
to deliver list of containers over graph of destination points
according to given transport, destinations and distances
"""


class Transport:
    """abstract transport class"""
    def __init__(self, location, distances):
        self.distances = distances
        self.location = location
        self.oper_time = 0

    def travel(self, trav_time):
        self.oper_time += trav_time

    def deliver(self, destination):
        self.location = destination
        self.oper_time += self.distances[destination]

    def way_back(self, back_from):
        self.location = self.init_location
        self.oper_time += self.distances[back_from]


class Truck(Transport):
    """creates truck instances with given
    initial location and available delivery points"""
    def __init__(self, location, dest_list):
        self.init_location = 'factory'
        super().__init__(location, dest_list)


class Ship(Transport):
    """creates ship instances with given
    initial location and available delivery points"""
    def __init__(self, location, dest_list):
        self.init_location = 'port'
        super().__init__(location, dest_list)


class Deliver:
    """create instance of current situation, which includes transport,
    sources of containers, destinations and distances"""
    def __init__(self, given_transport, deliv_string, distances):
        self.transport = given_transport
        self.deliv_string = deliv_string
        self.distances = distances

    def est_count(self, current, remain_list, transport_arr):
        trucks = []

        for i in transport_arr:
            if isinstance(i, Truck):
                trucks.append(i.location)

        for c in set(remain_list):
            if c not in self.distances:
                raise LookupError('wrong destination given')
            est_time = remain_list.count(c) \
                * self.distances[c] \
                * (len(trucks) - 1)
            if est_time > self.distances[current]:
                return True
        return False

    def calculate_time(self):
        to_deliver = [c for c in self.deliv_string]
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
                            if curr not in self.distances:
                                raise LookupError('wrong destination given')
                            if curr == 'A':
                                t.deliver('port')
                                port_stack.append((curr, t.oper_time))
                            else:
                                t.deliver(curr)
                            if not to_deliver:
                                break
                    if t.location != 'factory' \
                        and len(to_deliver) > 0 \
                            and self.est_count(
                                t.location, to_deliver, self.transport
                            ):
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

        print(
            f'list "{self.deliv_string}" will be delivered in \n\
            {max([t.oper_time for t in self.transport])} hours'
        )
        return max([t.oper_time for t in self.transport])


class Calculator:
    """allows to create transport situations and invoke calculation"""
    def __init__(self, distances, num_trucks=0, num_ships=0):
        if num_trucks == 0 and num_ships == 0:
            raise ValueError("transport list is empty")
        self.distances = distances
        self.transport_creator({'trucks': num_trucks, 'ships': num_ships})

    def transport_creator(self, transport):
        full_transport = []
        for tp in transport:
            if tp == 'trucks':
                for i in range(transport[tp]):
                    full_transport.append(
                        Truck('factory', {'port': 1, 'B': 5})
                    )
            elif tp == 'ships':
                for i in range(transport[tp]):
                    full_transport.append(
                        Ship('port', {'A': 4})
                    )
            else:
                raise AttributeError('wrong transport requested')

        self.full_current_transport = full_transport

    def process(self, delivery):
        transp_graph_situation = Deliver(
            self.full_current_transport, delivery, self.distances
        )
        return transp_graph_situation.calculate_time()


calc = Calculator({'A': 4, 'port': 1, 'B': 5}, num_trucks=2, num_ships=1)

assert calc.process('A') == 5
assert calc.process('AB') == 5
assert calc.process('BB') == 5
assert calc.process('ABB') == 7
calc.process('AABABBAB')
calc.process('ABBBABAAABBB')
