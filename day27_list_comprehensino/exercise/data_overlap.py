file1_list = []
file2_list = []

with open("file1.txt") as file1:
  for line in file1:
    file1_list.append(int(line.strip()))
  #file1_list = file1.readlines() 도 가능

with open("file2.txt") as file2:
  for line in file2:
    file2_list.append(int(line.strip()))
#file2_list = file2.readlines() 도 가능

result = [ number for number in file1_list if number in file2_list ]

# Write your code above 👆
print(result)