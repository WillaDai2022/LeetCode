class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #map key to node
        self.capacity = capacity
        
        #dummy head and tail
        self.head, self.tail = Node(0,0), Node(0,0)
        
        #head = LRU, tail = most recent used 
        self.head.next = self.tail 
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
        
    #remove node from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    #insert node at right
    def insert(self, node):
        prev,tail = self.tail.prev, self.tail
        prev.next = tail.prev = node
        node.next = tail
        node.prev = prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)