# Program: Placement-Level Lambda Programs
# 1. Find second-largest number using lambda & filter
# 2. Find numbers greater than average
# 3. Top 3 students from list of records
# 4. IT department employees with salary > 50000

nums = [10, 45, 90, 23, 78, 89, 90]
avg_val = sum(nums) / len(nums)

# 1. Second largest
max_val = max(nums)
second_largest = max(filter(lambda x: x < max_val, nums))

# 2. Numbers > average
gt_avg = list(filter(lambda x: x > avg_val, nums))

# 3. Top 3 students
student_records = [("Amit", 82), ("Bhavya", 95), ("Chirag", 78), ("Diya", 91), ("Eshan", 88)]
sorted_students = sorted(student_records, key=lambda x: x[1], reverse=True)
top_3 = sorted_students[:3]

# 4. IT department with salary > 50000
employees = [
    {"name": "Rahul", "dept": "IT", "salary": 65000},
    {"name": "Sneha", "dept": "HR", "salary": 45000},
    {"name": "Karan", "dept": "IT", "salary": 48000},
    {"name": "Pooja", "dept": "IT", "salary": 72000}
]
it_high_salary = list(filter(lambda e: e["dept"] == "IT" and e["salary"] > 50000, employees))

print("Nums                    :", nums)
print("Second Largest          :", second_largest)
print("Numbers > Average       :", gt_avg)
print("Top 3 Students          :", top_3)
print("IT Employees > Rs.50000 :", [e["name"] for e in it_high_salary])
