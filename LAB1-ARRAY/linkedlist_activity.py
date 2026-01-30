class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            print("Index out of bounds")
            return
        
        if index == 0:
            self.insert_head(value)
            return
        
        if index == self.size:
            self.insert_tail(value)
            return
        
        new_node = Node(value)
        current = self.head
        index_counter = 0
        while current is not None and index_counter < index - 1:
            current = current.next
            index_counter += 1
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_head(self):
        if self.head is None:
            print("Operation failed: List is empty")
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            print("Operation failed: Invalid index")
            return
        
        if index == 0:
            self.delete_head()
            return
        
        current = self.head
        index_counter = 0
        while current is not None and index_counter < index - 1:
            current = current.next
            index_counter += 1
        
        if current is None or current.next is None:
            print("Index out of bounds")
            return
        
        if current.next == self.tail:
            self.tail = current
        
        current.next = current.next.next
        self.size -= 1
    
    def delete_value(self, value):
        if self.head is None:
            print("Operation failed: List is empty")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        print("Value not found")

    def index_of(self, value):
        current = self.head
        index_counter = 0
        while current is not None:
            if current.data == value:
                return index_counter
            current = current.next
            index_counter += 1
        return -1
    
    def peek_head(self):
        if self.head is None:
            return None
        return self.head.data

    def peek_tail(self):
        if self.tail is None:
            return None
        return self.tail.data
    
    def create_from_list(self, values):
        for value in values:
            self.insert_tail(value)
    
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

print("=== CLINIC QUEUE ===")
clinic_queue = LinkedList()
list_of_patients = ["Ana", "Bob", "Cara"]
print("Created list: " + str(list_of_patients) + "\n")
clinic_queue.create_from_list(list_of_patients)

print("Insert " + "'Zed'" + " at head...")
clinic_queue.insert_head("Zed")
print("List now: " + str(clinic_queue.to_list()) + "\n")

print("Insert " + "'Liam'" + " at tail...")
clinic_queue.insert_tail("Liam")
print("List now: " + str(clinic_queue.to_list()) + "\n")

print("Insert " + "'Mia'" + " at position 2...")
clinic_queue.insert_at(2, "Mia")
print("List now: " + str(clinic_queue.to_list()) + "\n")

print("Delete head...")
clinic_queue.delete_head()
print("List now: " + str(clinic_queue.to_list()) + "\n")

print("Delete node with value " + "'Mia'" + "...")
clinic_queue.delete_value("Mia")
print("List now: " + str(clinic_queue.to_list()) + "\n")

print("Searching for " + "'Cara'" + "...")
index = clinic_queue.index_of("Cara")
print("Found at index " + str(index) + "\n")

print("Peek head: " + str(clinic_queue.peek_head()))
print("Peek tail: " + str(clinic_queue.peek_tail()))
print("")

print("Deleting last node...")
clinic_queue.delete_value(clinic_queue.tail.data)
print("List now: " + str(clinic_queue.to_list()) + "\n")

print("Trying to delete from empty list...")
empty_queue = LinkedList()
empty_queue.delete_head()