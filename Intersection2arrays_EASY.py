class Solution:
    def intersection(self, nums1,nums2):

        dictt = {}
        result = []
        for i in nums1:
            if i not in dictt:
                dictt[i] = 1  # first time, hence set occurrence to 1
            else:
                dictt[i] += 1  # increment occurrence

        for j in nums2:
            if j in dictt and dictt[j] > 0 and j not in result:
                result.append(j)
        # print(dictt)
        return result

obj = Solution()
print(obj.intersection([1,2,2,4], [2,4]))