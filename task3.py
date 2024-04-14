# Вам дан целочисленный массив nums. Изначально вы располагаетесь на первом индексе массива,
# и каждый элемент массива представляет собой максимальную длину вашего прыжка в этой позиции.
# Возвращается true, если вы можете достичь последнего индекса, или false в противном случае.
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible
# to reach the last index.

def foo(nums):
    max_step = 0
    for i in range(len(nums)):
        if i > max_step:
            return False

        max_step = max(max_step, i + nums[i])
        if max_step >= len(nums) - 1:
            return True

    return False


nums = [2, 3, 1, 1, 4]
print(foo(nums))

nums = [3, 2, 1, 0, 4]
print(foo(nums))