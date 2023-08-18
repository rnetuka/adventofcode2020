class Schedule:

    def __init__(self):
        self.departures = []

    def test(self, time):
        for bus, offset in self.departures:
            if (time + offset) % bus != 0:
                return False
        return True



if __name__ == '__main__':
    with open('../res/day13.txt') as file:
        time = int(file.readline())
        line = file.readline().rstrip()

        #line = '7,13,x,x,59,x,31,19'

        buses = [int(n) for n in line.split(',') if n != 'x']
        departures = [n for n in line.split(',')]

    waiting_times = [bus - (time % bus) for bus in buses]

    waiting_time = min(waiting_times)
    bus = buses[waiting_times.index(waiting_time)]

    print(f'Bus: {bus} (waiting time: {waiting_time}) ... {bus * waiting_time}')


    dep = []
    for i, bus in enumerate(departures):
        if bus != 'x':
            dep.append((int(bus), i))

    sch = Schedule()
    sch.departures = dep

    t = 100000000000000
    while True:
        t += 1
        if sch.test(t):
            print(t)
            break


