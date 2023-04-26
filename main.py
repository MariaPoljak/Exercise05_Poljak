#selection_sort(numbers: list)

def selection_sort(numbers: list):
    for fill_slot in range (0, len(numbers) -1):
        position_of_max = fill_slot
        for location in range(fill_slot +1, len(numbers)):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location
        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp
        return numbers


#binary_search(text: list, target: str)

def binary_search(text: list, target: str):
    first = 0
    last = len(text) - 1
    found = False
    while first is not found:
        mid = (first + last) // 2
        if text[mid] == target:
            found = True
        return found


#HashTable()

class HashTable(list):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size


#put(self, key, data)

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] is key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] is not key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

#get(self, key)

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = true
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data