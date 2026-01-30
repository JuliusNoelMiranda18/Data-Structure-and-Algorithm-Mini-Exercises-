class Stack:
    def __init__(self):
        self.table = []
        self.content = 0

    def push(self, x):
        self.table.append(x)
        self.content += 1

    def pop(self):
        if self.content == 0:
            return None
        self.content -= 1
        return self.table.pop()

    def peek(self):
        if self.content == 0:
            return None
        return self.table[-1]

    def isEmpty(self):
        return self.content == 0

    def size(self):
        return self.content

    def show(self):
        return list(self.table)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def show(self):
        return list(self.items)


class ParkingLot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cars = Stack()

    def arrive(self, plate: str):
        if self.cars.size() == self.capacity:
            return "Lot full"
        self.cars.push(plate)
        return self.cars.show()

    def depart(self):
        p = self.cars.pop()
        return p if p is not None else "Lot empty"
    
    def depart_specific(self, plate: str):
        if self.cars.isEmpty():
            return "Lot empty"
        temp = Stack()

        while not self.cars.isEmpty() and self.cars.peek() != plate:
            temp.push(self.cars.pop())

        if self.cars.isEmpty():
            while not temp.isEmpty():
                self.cars.push(temp.pop())
            return "Not found"

        removed = self.cars.pop()

        while not temp.isEmpty():
            self.cars.push(temp.pop())

        return removed

    def top_car(self):
        return self.cars.peek()

    def lot_size(self):
        return self.cars.size()

    def snapshot(self):
        return self.cars.show()
    

class TicketCounter:
    def __init__(self):
        self.line = Queue()

    def join(self, name: str):
        self.line.enqueue(name)
        return self.line.show()

    def serve(self):
        x = self.line.dequeue()
        return x if x is not None else "No one to serve"
    
    def move_to_front(self, name: str):
        if self.line.isEmpty():
            return "No one to move"

        n = self.line.size()
        count_before = 0
        found = False

        for i in range(n):
            x = self.line.dequeue()
            self.line.enqueue(x)
            if x == name and not found:
                found = True
                count_before = i

        if not found:
            return "Not found"

        for _ in range(count_before):
            self.line.enqueue(self.line.dequeue())
        
        target = self.line.dequeue()
        
        self.line.enqueue(target)
        
        for _ in range(self.line.size() - 1):
            self.line.enqueue(self.line.dequeue())

        return self.line.show()


    def rotate(self, k: int):
        if self.line.isEmpty() or k <= 0:
            return self.line.show()
        steps = k % self.line.size()
        for _ in range(steps):
            x = self.line.dequeue()
            if x is not None:
                self.line.enqueue(x)
        return self.line.show()


    def next_up(self):
        return self.line.peek()
        
    def line_size(self):
        return self.line.size()
    
    def snapshot(self):
        return self.line.show()


def print_section(title):
    print("\n" + "=" * 10, title, "=" * 10)

def demo_scenarios():
    print_section("PARKING LOT (STACK)")
    lot = ParkingLot(capacity=3)

    print("Start:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())
    print("> arrived           →", lot.arrive("AAA-111"))
    print("> arrived           →", lot.arrive("BBB-222"))
    print("> arrived           →", lot.arrive("CCC-333"))
    print("> arrived           →", lot.arrive("DDD-444"))
    print("Now:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())

    print("> depart()          →", lot.depart())
    print("Now:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())
    print("> depart()          →", lot.depart())
    print("> depart()          →", lot.depart())
    print("> depart()          →", lot.depart())
    print("End:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())

    print_section("TICKET COUNTER (QUEUE)")
    tc = TicketCounter()

    print("Start:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())
    print("> join             →", tc.join("Irene"))
    print("> join             →", tc.join("Jasper"))
    print("> join             →", tc.join("Kyla"))
    print("Now:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())

    print("> serve()           →", tc.serve())
    print("Snapshot            →", tc.snapshot())
    print("> serve()           →", tc.serve())
    print("> serve()           →", tc.serve())
    print("> serve()           →", tc.serve())
    print("End:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())

    print("\n--- EXTRA TESTS: depart_specific / move_to_front / rotate ---")

    lot2 = ParkingLot(capacity=5)
    for p in ["AAA-111", "BBB-222", "CCC-333", "DDD-444"]:
        print("> arrive", p, "→", lot2.arrive(p))
    print("Snapshot:", lot2.snapshot())
    print("depart_specific('CCC-333') →", lot2.depart_specific("CCC-333"))
    print("After:", lot2.snapshot())
    print("depart_specific('ZZZ-999') →", lot2.depart_specific("ZZZ-999"))
    print("After:", lot2.snapshot())

    tc2 = TicketCounter()
    for n in ["Irene", "Jasper", "Kyla", "Luis"]:
        print("> join", n, "→", tc2.join(n))
    print("Snapshot:", tc2.snapshot())
    print("move_to_front('Kyla') →", tc2.move_to_front("Kyla"))
    print("After:", tc2.snapshot())
    print("rotate(2) →", tc2.rotate(2))
    print("After:", tc2.snapshot())
    print("move_to_front('Zed') →", tc2.move_to_front("Zed"))
    print("After:", tc2.snapshot())

if __name__ == "__main__":
    demo_scenarios()