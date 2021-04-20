# Time Complexity  : O(N+M) where N is length of original list and M is length of dictionary
class Solution:
    def highFive(self, items):
        dictt = {}
        li = []

        for idx, score in items:
            if idx not in dictt:
                dictt[idx] = [score]  # first score put it in a list and then add it to dictionary as Value
            else:  # if some score already present, then append the remaining scores for that id
                dictt[idx].append(score)

        for idx, scores in dictt.items():
            sortedscores = sorted(scores, reverse=True)
            avg = (sum(sortedscores[:5])) // 5
            # print("Average", avg)
            li.append([idx, avg])
        return sorted(li)
obj = Solution()
print(obj.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))










