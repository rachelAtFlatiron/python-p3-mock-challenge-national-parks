#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    park1 = NationalPark("Yellowstone")
    park2 = NationalPark("Yosemite")
    park3 = NationalPark("Grand Canyon")
    park4 = NationalPark("Zion")
    park5 = NationalPark("Rocky Mountain")

    visitor1 = Visitor("Alice")
    visitor2 = Visitor("Bob")
    visitor3 = Visitor("Charlie")
    visitor4 = Visitor("David")
    visitor5 = Visitor("Eve")
    visitor6 = Visitor("Frank")
    visitor7 = Visitor("Grace")
    visitor8 = Visitor("Hannah")
    visitor9 = Visitor("Ian")
    visitor10 = Visitor("Judy")

    trip1 = Trip(visitor1, park1, "August 10", "August 10")
    trip2 = Trip(visitor2, park2, "August 10", "August 10")
    trip3 = Trip(visitor3, park3, "August 10", "August 10")
    trip4 = Trip(visitor2, park1, "August 10", "August 10")
    trip5 = Trip(visitor5, park1, "August 10", "August 10")
    ipdb.set_trace()
