# Print numbers from 1 to 5
for i in range(1, 6):
    print(f"Number: {i}")



# Print numbers until the sum exceeds 10
sum_ = 0
count = 1
while sum_ <= 10:
    sum_ += count
    print(f"Count: {count}, Sum: {sum_}")
    count += 1



# Print multiplication table
for i in range(1, 4):  # Rows
    for j in range(1, 4):  # Columns
        print(f"{i} x {j} = {i * j}", end="\t")
    print()  # Newline after each row
