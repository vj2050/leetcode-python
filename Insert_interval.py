# Same as merge interval
class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        #print(intervals)
        result = []
        if intervals == []:
            return []
        for i in range(len(intervals)):
            if result == [] or result[-1][1] < intervals[i][0]:
                # no overlap
                result.append(intervals[i])
            else:
                # overlap
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result

obj = Solution()
result = obj.insert([[1,3],[6,9]],[2,5])
print(result)