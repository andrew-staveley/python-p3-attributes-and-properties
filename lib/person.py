#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Person Name Here", job="Admin"):
        self.name = name.title() if (type(name) is (str)) and (1 <= len(name) <= 25) else print("Name must be string between 1 and 25 characters.")
        self.job = job if (job in APPROVED_JOBS) else print("Job must be in list of approved jobs.")