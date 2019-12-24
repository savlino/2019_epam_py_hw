"""
calculates amount of time to deliver container from factory according give list
"""

class Transport:
    def __init__(self):
        # self.location = location
        self.oper_time = 0

    def travel(self, trav_time):
        self.oper_time += trav_time
        # self.location = destination


def delivers(deliv_list):
    to_deliver = [c for c in deliv_list]
    port_stack = []
    port_delay = 0
    port_stop = []
    b_stop = []
    a_stop = []


    class Truck(Transport):
        def factory_to_b(self):
            b_stop.append(factory_stop.pop(0))
            self.travel(5)

        def factory_to_port(self):
            port_stop.append(factory_stop.pop(0))
            self.travel(1)
            port_stack.append(self.oper_time)

        def b_to_factory(self):
            factory_stop.append(b_stop.pop(0))
            self.travel(5)

        def port_to_factory(self):
            factory_stop.append(port_stop.pop(0))
            self.travel(1)


    class Ship(Transport):
        def port_to_a(self):
            if port_stack[0] > self.oper_time:
                self.oper_time = port_stack[0]
            a_stop.append(port.pop(0))
            port_stack.pop(0)
            self.travel(4)

        def a_to_port(self):
            port.append(a_stop.pop(0))
            self.travel(4)


    truck1 = Truck()
    truck2 = Truck()
    boat = Ship()
    factory_stop = [truck1, truck2]
    port = [boat]

    while to_deliver:
        curr = to_deliver.pop(0)

        est_count = to_deliver.count('A') > 3 or to_deliver.count('B') > 1

        if factory_stop:
            if curr == 'A':
                factory_stop[0].factory_to_port()
            if curr == 'B':
                factory_stop[0].factory_to_b()

        if port_stop and len(to_deliver) >= 1:
            port_stop[0].port_to_factory()

        if b_stop and est_count:
            b_stop[0].b_to_factory()

        if port_stack:
            if port:
                port[0].port_to_a()
                continue
            if a_stop:
                a_stop[0].a_to_port()
                port[0].port_to_a()  #call 1

        if (port_stack or to_deliver.count('A')) and a_stop:
            a_stop[0].a_to_port()

    return max(truck1.oper_time, truck2.oper_time, boat.oper_time)


assert delivers('A') == 5
assert delivers('A') 
assert delivers('AB') == 5
assert delivers('BB') == 5
assert delivers('ABB') == 7
delivers('AABABBAB')
delivers('ABBBABAAABBB')
