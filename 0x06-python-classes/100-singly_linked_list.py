#!/usr/bin/python3
""""Define classes for a singly-linked list."""


class Node:
    """
    Node classs: defines a node of a singly-linked list.

    Attributes:
        __data (int): private instance attribute
        __next_node (Node): private instance attribute
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new instance of the node class.

        Args:
            data (int): the data of the node
            next_node: the next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data att

        Returns:
            int: the data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for data att

        Args:
            value (int): new data set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next_node att

        Returns:
            Node: the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """"
        setter method for next_node att

        Args:
            value (Node): the new next node.

        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class: defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize a new instsnace

        Attributes:
            head (Node): the head node of the linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the corrected sorted position

        Args:
            value (int): value of the new node to insert.
        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list
        """

        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
