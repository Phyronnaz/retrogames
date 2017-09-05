class Node(object):
    def __init__(self, next_node, previous_node, data):
        self.next_node = next_node
        self.previous_node = previous_node
        self.data = data


class CycleList(object):
    def __init__(self):
        self.pointer = None

    def push(self, data):
        '''Pushes the node <node> at the "front" of the ll
        '''
        if self.pointer is None:
            node = Node(None, None, data)
            node.previous_node = node
            node.next_node = node
            self.pointer = node
        else:
            prev = self.pointer
            nxt = self.pointer.next_node
            node = Node(nxt, prev, data)
            prev.next_node = node
            nxt.previous_node = node
            self.pointer=node
        return self

    def pop(self):
        '''Pops the last node out of the list'''

        if self.pointer is None:
            return None

        prev = self.pointer.previous_node
        nxt = self.pointer.next_node
        old_last_node = self.pointer
        self.pointer = nxt

        prev.next_node = nxt
        nxt.prev_node = prev

    def remove(self,node):
        '''Pops the last node out of the list'''

        if self.pointer is None:
            raise Exception("list empty")

        if self.pointer is node:
            self.pointer=node.next_node

        prev = node.previous_node
        nxt = node.next_node
        prev.next_node = nxt
        nxt.prev_node = prev

    def next(self):
        return self.pointer.next_node.data

    def prev(self):
        return self.pointer.previous_node.data

    def current(self):
        return self.pointer.data

    def __iter__(self):
        yield self.pointer
        ptr = self.pointer.next_node
        while ptr != self.pointer:
            yield ptr
            ptr = ptr.next_node


"""
cycle_list = CycleList()


for i in range(10):
    cycle_list.push(i)

for i in cycle_list:
    print(i.data)
"""