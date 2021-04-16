def func(numOfHouses, arr):
    arr.sort(key=lambda x: x[1])
    # print(arr)
    max_elem = 0
    diff = 0

    for i in range(len(arr) - 1):
        if arr[i + 1][1] - arr[i][1] > max_elem:
            max_elem = arr[i + 1][1] - arr[i][1]
            house1 = arr[i][0]
            house2 = arr[i + 1][0]
    result = sorted([house1, house2])
    print(str(result[0]) + " " + str(result[1]))


numOfHouses = 5
arr = [[3,7],[1,9],[2,0],[5,15],[4,30]]
func(numOfHouses, arr)
