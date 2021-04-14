# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Video Reference :https://www.youtube.com/watch?v=5EY9rHCfa8g
class Solution:
    def merge(self, intervals):
        if intervals==[]:
            return []

        intervals.sort()  # sorts intervals according to start time first.
        result = []

        for i in range(len(intervals)):
            if result == [] or result[-1][1] < intervals[i][0]:  # if result empty, or last interval added to result, its endtime < current interval's start time, then no overlap, simply add
                result.append(intervals[i])
            else:
                # OVERLAP ; keep updating the last added interval's values, dont add any new interval to result here
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result

obj = Solution()
result = obj.merge([[1,3],[2,6],[8,10],[15,18]])
print(result)
