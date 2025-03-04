"""Insert Index"""
class DataNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        current = self.head
        if current is None:
            print("This is an empty list.")
        else:
            while current is not None:
                if current.next is not None:
                    print(current.data, end=" ")
                else:
                    print(current.data)
                current = current.next

    def insert_last(self, data):
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_before(self, node, data):
        new_node = DataNode(data)
        current = self.head
        prev = None
        while current is not None:
            if current.data == node:
                if prev is None:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    prev.next = new_node
                    new_node.next = current
                self.count += 1
                return 0
            prev = current
            current = current.next
        else:
            print("Cannot insert, " + node + " does not exist.")

    def delete(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if self.head.data == data:
                    self.head = self.head.next
                elif current.next is not None:
                    prev.next = current.next
                    self.count -= 1
                else:
                    prev.next = None
                return 0
            current = current.next
            prev = current
        print("Cannot delete, " + data + " does not exist.")

def main():
    """main function"""
    data = SinglyLinkedList()
    # Input
    for _ in range(int(input())):
        data.insert_last(int(input()))

    in_data = int(input())
    ins_data = int(input())
    index = 0
    neg = 0
    current = data.head

    # if input index is neg
    if in_data < 0:
        neg = in_data + data.count

    # if input index is 0 when list is empty
    if not in_data:
        data.insert_front(ins_data)
        data.traverse()
        return

    #if you want insert data to the last node
    if in_data == data.count:
        data.insert_last(ins_data)
        data.traverse()
        return

    # Loop till reach excepted index and insert before data at index
    while current:
        # If index is negative
        if in_data < 0:
            in_data = neg
            prev = None
            while current:
                if index == in_data:
                    prev = current.next
                    data.insert_before(prev.data, ins_data)
                    break
                prev = current.next
                current = current.next
                index += 1
            break
        else:
            if index == in_data:
                data.insert_before(current.data, ins_data)
                break
            current = current.next
            index += 1

    data.traverse()

main()
