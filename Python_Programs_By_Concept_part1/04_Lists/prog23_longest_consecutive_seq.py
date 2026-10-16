# Program: Longest Consecutive Sequence of Numbers
# Find length of longest sequence of consecutive integers in a list.

numbers = [100, 4, 200, 1, 3, 2]
print("Input list:", numbers)

num_set = set(numbers)
longest_streak = 0

for num in num_set:
    # check if it is start of sequence
    if num - 1 not in num_set:
        current_num = num
        current_streak = 1

        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1

        if current_streak > longest_streak:
            longest_streak = current_streak

print("Length of Longest Consecutive Sequence:", longest_streak)
