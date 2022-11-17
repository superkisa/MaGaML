class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class List:
    def __init__(self):
        # creating service node:
        self.head, self.tail = ListNode(None, self.tail, None), ListNode(None, None, self.head)
        self.len = 0

    def insert(self, previous_node, val):
        new_node = ListNode(val, previous_node.next, previous_node)
        if previous_node.next is not None:    
            previous_node.next.prev = new_node
        previous_node.next = new_node
        self.len += 1
        if new_node.next is None:
            self.tail = new_node
        return new_node

    def push_front(self, val):
        return self.insert(self.head, val)

    def push_back(self, val):
        return self.insert(self.tail, val)

    def pop_back(self):
            self.remove(self.tail)

    def pop_front(self):
            self.remove(self.head.next)

    def __len__(self):
            return self.len


cin = []
with open("algo\HW3\input.txt", "r") as i_f:
    for s in i_f.readlines():
        cin.append(list(map(int, s.rstrip("\n").split())))

print(cin)
