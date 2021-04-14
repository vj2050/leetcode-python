def twosum(nums, target):

    #NOTE : Cannot use Two-pointer technique which involves sorting of array,since here we have to return INDEX of the two nums and NOT the nums itself.
    # Sorting will change the original INDEXES, hence opt for dictionary method.
    dictt = {}

    if not nums:
        return False

    for i in range(len(nums)):
        if nums[i] not in dictt:
            dictt[target - nums[i]] = i
        else:
            return [dictt[nums[i]], i]

        # buff_dict[nums[i]], i

print(twosum([3,2,4],6))