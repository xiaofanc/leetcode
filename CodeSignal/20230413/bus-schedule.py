"""
Given an array of schedule that represents the schedule of bus arrival times and a string time that represents the current time.
Find out how many minutes ago the last bus left. If the first bus has yet to leave, return -1.
If the bus is scheduled to leave at the current time, it has not left yet.

schedule = ["12:30", "14:00", "19:55"], time = "14:30"
res = 30

schedule = ["00:00", "14:00", "19:55"], time = "00:00"
res = -1

schedule = ["12:30", "14:00", "19:55"], time = "14:00"
res = 90
"""

