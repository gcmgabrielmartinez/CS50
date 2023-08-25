import sys

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return "🍪"*self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():

    cookie_jar = Jar(-12)
    print(cookie_jar.size)
    print(cookie_jar.capacity)

    cookie_jar.deposit(2)
    print(cookie_jar.size)
    print(str(cookie_jar))

if __name__ == "__main__":
    main()