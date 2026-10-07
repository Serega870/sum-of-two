def add(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

# Тесты
print(add([2, 7, 11, 15], 9))
print(add([3, 2, 4], 6))
print(add([3, 3], 6))