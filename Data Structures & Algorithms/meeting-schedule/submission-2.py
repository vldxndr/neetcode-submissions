"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        intervals.sort(key=lambda i: i.start)
        if len(intervals) == 0:
            return True

        for i in range(len(intervals)):
            if i == len(intervals) - 1:
                return True
            else:
                if intervals[i].end > intervals[i + 1].start:
                    return False
            