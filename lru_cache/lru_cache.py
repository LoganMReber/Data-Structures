from doubly_linked_list import DoublyLinkedList as DLL


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.cache = DLL()
        self.storage = {}
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:

            val = self.storage[key].value['v']
            self.cache.delete(self.storage[key])
            del self.storage[key]

            self.cache.add_to_head({'k': key, 'v': val})
            self.storage[key] = self.cache.head

            return self.cache.head.value['v']
        else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.storage:
            self.cache.delete(self.storage[key])
            del self.storage[key]

            self.cache.add_to_head({'k': key, 'v': value})
            self.storage[key] = self.cache.head

        elif self.cache.length < self.limit:
            self.cache.add_to_head({'k': key, 'v': value})
            self.storage[key] = self.cache.head

        else:
            del self.storage[self.cache.tail.value['k']]
            self.cache.remove_from_tail()
            self.cache.add_to_head({'k': key, 'v': value})
            self.storage[key] = self.cache.head
