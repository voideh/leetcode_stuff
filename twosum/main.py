import random

def opt_two_sum(nums: list[int], target: int) -> list[int]:

    n_map = {}
    for (i,n) in enumerate(nums):
        if target - n in n_map:
            return [n_map[target - nums[i]], i]
        n_map[nums[i]] = i
    return [-1, -1]


# naiive solution
def two_sum(nums: list[int], target: int) -> list[int]:
    for (i,n) in enumerate(nums):
        diff = target - n
        for (j,n) in enumerate(nums):
            if  i==j:
                continue
            if n == diff:
                return [i,j]
    return [-1,-1]


def pick2(nums: list[int]) -> list[int]:
    i1 = random.randint(0, len(nums))
    i2 = random.randint(0, len(nums))
    while i2 == i1:
        i2 = random.randint(0, len(nums))
    return [i1, i2]


nums = [3,3]

target = 6


i1, i2 = opt_two_sum(nums, target)

print(f'{nums=}\n{i1=} {i2=} {target=}\n{nums[i1]} + {nums[i2]} = {target}')

