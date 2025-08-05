# std_num = input("Please enter your numbers: ").split(" ")
# count = 0
# total = 0

# for i in range(0, len(std_num)):
#     std_num[i] = int(std_num[i])
#     count += 1
#     total += std_num[i]
#     print(std_num[i])
#     print(count)
#     print(total)
#     print("==========")

# print(f"the total is: {total}")
# print(f"the number of ellerment is: {count}")

# print(f"The average is: {round(total/count)}")

# *. MAX

numbers = [78, 65, 89, 86, 55, 91, 64, 89, 99, 23, 25]

max_num = 0

for i in numbers:
    if i > max_num:
        max_num = i 

print(f"The highest score in the class is: {max_num}")