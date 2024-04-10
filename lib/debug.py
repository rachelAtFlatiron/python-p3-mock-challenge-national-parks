#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    national_park_1 = NationalPark("Yellowstone National Park")
    national_park_2 = NationalPark("Yosemite National Park")
    national_park_3 = NationalPark("Grand Canyon National Park")
    national_park_4 = NationalPark("Glacier National Park")
    national_park_5 = NationalPark("Great Smoky Mountains National Park")
    national_park_6 = NationalPark("Zion National Park")
    national_park_7 = NationalPark("Grand Teton National Park")
    national_park_8 = NationalPark("Rocky Mountain National Park")
    national_park_9 = NationalPark("Arches National Park")
    national_park_10 = NationalPark("Acadia National Park")

    visitor1 = Visitor("Alice")
    visitor2 = Visitor("Bob")
    visitor3 = Visitor("Charlie")
    visitor4 = Visitor("David")
    visitor5 = Visitor("Emma")
    visitor6 = Visitor("Frank")
    visitor7 = Visitor("Grace")
    visitor8 = Visitor("Henry")
    visitor9 = Visitor("Ivy")
    visitor10 = Visitor("Jack")

    trip1 = Trip(visitor1, national_park_1, "May 3rd", "May 6th")
    trip2 = Trip(visitor2, national_park_3, start_date="May 5", end_date="May 8")
    trip3 = Trip(visitor1, national_park_2, "May 1st", "May 8th")
    

    ipdb.set_trace()
