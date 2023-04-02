guess_me = 7
start = 1

while True:
    if start < guess_me:
        print(f"{start} too low")
    elif start == guess_me:
        print('found it!')
        break
    else:
        print("oops")
        break
    start += 1

print("-" * 80)

for number in [3, 2, 1, 0]:
    print(number)

print("-" * 80)

nums = range(1, 10)
nums_odd = []
for num in nums:
    if (num % 2) == 1:
        nums_odd.append(num)
print(nums_odd)

print("-" * 80)

nums_dict = {}
for num in range(0, 10):
    nums_dict[num] = pow(num, 2)
print(nums_dict)

print("-" * 80)

