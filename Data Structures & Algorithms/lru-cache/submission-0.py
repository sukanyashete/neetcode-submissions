class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node

        # Initialize dummy boundary nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # Link them to each other
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _insert(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._insert(node)
            if len(self.cache) > self.capacity:
                deletenode = self.head.next
                self._remove(deletenode)
                del self.cache[deletenode.key]
        