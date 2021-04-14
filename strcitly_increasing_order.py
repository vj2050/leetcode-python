'''
In a new numbers game, players are given an integer array of length .

The players take turns, in each turn the current player does the following:

If a player can reorder the array elements to form a strictly increasing sequence, they win the game.
Otherwise the player can choose any element and remove it from the array.
Determine which player wins the game if both players play optimally and the first player plays first.

Input Format

The first line contains an integer , denoting the number of test cases.

Then, the description of  test cases follow. Each test case is given in two consecutive lines.

The first line of each test case contains an integer , denoting the number of elements in the array.

The second line of each test case contains  space-separated integers , denoting the array elements.

Constraints

Output Format

For each test case, print a single line contains "" (without the quotes) if the first player wins the game or "" (without the quotes) otherwise.

Sample Input 0

1
3
1 2 3
Sample Output 0

First
Explanation 0

Here the given sequence is strictly increasing. So, the first player wins.

Sample Input 1

2
4
1 2 2 3
5
3 1 2 5 4
Sample Output 1

Second
First
Explanation 1

In the first test case:

The given sequence is not strictly increasing. So, the first player has to remove an element. If the player removes any , this will lead to a winning state for the second player. So, it would be better if  or  is removed.

Let's assume the player removes . The second player can not reorder the elements and win. So, the second player has to remove an element. If the player removes any , this will lead to a winning state for the first player. So, it would be better if  is removed.

The remaining sequence is  . Which is not a strictly increasing sequence. So, the first player has to remove an element.

The second player wins since the remaining element is  and it is considered a strictly increasing sequence.
'''


def whoIsTheWinner(arr):
    # WRITE DOWN YOUR CODE HERE
    # print(set(arr))
    result = "First"

    if arr == [i for i in set(arr)]:
        return result
    else:
        res =[]
        for i in range(len(arr)):
            if arr[i] not in res:
                res.append(arr[i])
            else:

abc = whoIsTheWinner([1,2,3])
print(abc)
