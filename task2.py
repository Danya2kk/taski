# Учитывая массив строк strs, сгруппируйте анаграммы вместе. Вы можете вернуть ответ в любом порядке.
# Анаграмма - это слово или фраза, образованная путем перестановки букв другого слова или фразы, обычно с использованием
# всех исходных букв ровно один раз.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]

def foo(strs):
    anagram_groups = {}

    for s in strs:

        sorted_str = ''.join(sorted(s))

        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(s)
        else:

            anagram_groups[sorted_str] = [s]

    return list(anagram_groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(foo(strs))
