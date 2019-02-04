class Queue:
    def __init__(self):
        self.__arr = []
        self.__len = 0

    def push(self, elem):
        self.__arr.append(elem)
        self.__len += 1

    def pop(self):
        extelem = self.__arr[0]
        self.__len -= 1
        self.__arr = self.__arr[1:]
        
        return extelem

    def len(self):
        return self.__len

    def top(self):
        if self.__len:
            return self.__arr[self.__len - 1]

        return Queue()

    def last(self):
        if self.__len:
            return self.__arr[0]

        return Queue()

    def at(self, idx):
        if self.__len and idx < self.__len and idx >= 0:
            return self.__arr[self.__len - idx - 1]

        return Queue()

q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.top())
print(q.last())
print(q.len())
print(q.at(2))
