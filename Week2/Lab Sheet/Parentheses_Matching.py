class ArrayStack:
    def __init__(self, data = []):
        self._size = 0
        self._data = data

    def push(self, data):
        self._data = self._data + [data]
        self._size += 1

    def pop(self):
        if not self._size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            last_item = self._data[-1]
            del self._data[-1]
            self._size -= 1
            return last_item

    def is_empty(self):
        if not self._size:
            return True
        return False

    def get_stack_top(self):
        if not self._size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self._data[-1]

    def get_size(self):
        return self._size

    def print_stack(self):
        return print(self._data)

OPEN_PARENTHESES = ArrayStack()

def is_parentheses_matching(expression):
    
    for i in expression:
        if i == "(":
            OPEN_PARENTHESES.push("(")
        if i == ")":
            OPEN_PARENTHESES.pop()

    if OPEN_PARENTHESES.get_size():
        print(f"Parantheses in {expression} are unmatched")
        return False
    else:
        print(f"Parantheses in {expression} are matched")
        return True

is_parentheses_matching(input())
