# 39) MEDIUM


class CombinationSum:
    def combination(self, candidates, target):
        result = []
        stack = []
        #### Candidates ARRAY has to be SORTED First!!!!
        self.backtracking(sorted(candidates), target, stack, result)
        return result


    def backtracking(self,candidates, target, stack, result):
        # BASE CASE:
        for i, c in enumerate(candidates):
            d = target - c

            if d ==0:
                result.append(stack + [c])
                break  #pop top of stack and hop on next iteration, increment i
            elif d > 0:
                self.backtracking(candidates[i:], d, stack + [c], result)
            else:
            # d < 0
                break   #pop top of stack and hop on next iteration, increment i



        # for start in range(len(candi)):
        #
        #     stack.append(candi[start])
        #     print(candi, start, target - candi[start], stack, result)
        #
        #     self.backtracking(candi, start, target - candi[start], stack, result)
        #     #print(candi, start, target - candi[start], stack, result)
        #     stack.remove(stack[-1])


obj = CombinationSum()
candidates = [2, 3, 6, 7]
target = 7
result = obj.combination(candidates, target)
print(result)



'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(tmpList, candidates, target):
            for i,c in enumerate(candidates):
                d = target - c
                if d == 0:
                    result.append(tmpList + [c])
                    break
                elif d > 0:
                    dfs(tmpList + [c], candidates[i:], d)
                else: # d < 0
                    break
        dfs([], sorted(candidates), target)
        return result
'''