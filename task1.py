# Задав массив nums из различных целых чисел, верните все возможные перестановки.
# Вы можете вернуть ответ в любом порядке.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]

def foo(nums):
    if len(nums) == 0:
        return [[]]

    result = []
    for i in range(len(nums)):
        current_num = nums[i]
        for j in foo(nums[:i] + nums[i + 1:]):
            result.append([current_num] + j)

    return result


# Пример использования
nums = [1, 2, 3]
print(foo(nums))

