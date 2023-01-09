#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """the singly linked list"""

    def __init__(self):
        """initialise instance attribute of the class
        creates the singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """that inserts a new Node into the correct sorted position in the list (increasing order)
        Args:
            value (Node): node to be added to list"""
        new = Node(value)
        if self.__head == None:
            new.next_node = None
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node):
                temp = temp.next_node
            new.nextnode = None
            temp.next_node = new

        if not new.next_node:
            temp = self.__head
            index = temp.next_node
            while (index):
                if temp.data > index.data:
                    hold = temp.data
                    temp.data = index.data
                    index.data = hold
                index = index.next_node
                temp = temp.next_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
