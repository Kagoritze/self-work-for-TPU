class Node:
    def __init__(self, coefficient=0, power=0):
        self.coefficient = coefficient
        self.power = power
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, coefficient, power):
        new_node = Node(coefficient, power)
        if not self.head or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.power >= power:
                current = current.next
            if current.power == power:
                current.coefficient += coefficient
            else:
                new_node.next = current.next
                current.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(
                f"[{current_node.coefficient} | {current_node.power}]",
                end=" => " if current_node.next else "\n",
            )
            current_node = current_node.next


Q = LinkedList()
Q.append(-5, 3)
Q.append(2, 4)
Q.append(3, 2)
Q.append(-1, 1)
Q.append(7, 0)

Q.print_list()
