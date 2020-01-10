# 题目1：两数之和，给定一个数组nums和一个目标值target,找出数组中两个数之和等于target，并返回下标

# 解题思路：num2 = target - num1是否在list中，num2的查找不需要从nums查找一遍，只需要从num1位置之前或者之后查找即可，但为了从index这里选择从num1位置之前查找


def twosum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(1, lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break

    if j >= 0:
        return [j, i]
