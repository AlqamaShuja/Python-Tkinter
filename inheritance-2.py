# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#

class Animal:
    def eat(self):
        print("Eat")

class Mammal(Animal):
    def walk(self):
        print("Walk")

class Fish(Animal):
    def swim(self):
        print("Swim")

f = Fish();

# print(isinstance(f, Animal))
# print(isinstance(f, object))
# print(issubclass(f, object))


from abc import ABC,abstractmethod


class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already Opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already Closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Read from a File")


class NetworkStream(Stream):
    def read(self):
        print("Read from a Network")










