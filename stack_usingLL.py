# class to create new node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#class to implement stack

class stack:
    # to create stack using LL, need to intialise head
    def __init__(self):
        self.__head = None
        self.__count = 0
    def push(self,element):
        newnode = Node(element)
        newnode.next = self.__head
        self.__head = newnode
        self.__count = self.__count+1

    def pop(self):
        if self.isEmpty() is True:
            print("stack is empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count+1
        return data

    def top(self):
        if self.isEmpty() is True:
            print("stack is empty")
            return
        data = self.__head.data
        return data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

    print("Hello world")