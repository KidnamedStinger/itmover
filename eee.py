nums = [2, 4, 6, 10, 3, 5, 1, 7]
target = 8
t = True
for i in range(len(nums)):
    n1 = nums[i]
    for j in range(len(nums)):
        if i == j:
            pass
        else:
            n2 = nums[j]
            if n1 + n2 == target:
                print(i, j)
                t = False
if t:
    print("пар нет")
    

    

