#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Dog Name Here", breed="Mastiff"):
        self.name = name if (type(name) is (str)) and (1 <= len(name) <= 25) else print("Name must be string between 1 and 25 characters.") 
        self.breed = breed if (breed in APPROVED_BREEDS) else print("Breed must be in list of approved breeds.")