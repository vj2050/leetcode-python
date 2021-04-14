# 39) MEDIUM

class CombinationSum:
    def combination(self, candidates, target):
        result = []
        stack = []
        #### Candidates ARRAY has to be SORTED First!!!!
        self.backtracking(sorted(candidates), 0, target, stack, result)
        return result

    def backtracking(self, candidates, index, target, stack, result):
        print(candidates, index, target - candidates[index], stack, result)
        if (target == 0):
            result.append(stack[:])
            return

        for i in range(index, len(candidates)):
            if (candidates[i] > target):       #current element > reduced target   2 > 1
                break
            stack.append(candidates[i])
            self.backtracking(candidates, i, target - candidates[i], stack , result)
            stack.pop()

obj = CombinationSum()
candidates = [2, 3, 6, 7]
target = 7
result = obj.combination(candidates, target)
print(result)
