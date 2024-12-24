# Input: [-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
# Output : [4, 16, 25, 25, 49, 56, 121, 144, 225] 

numbers = input("enter your numbers:").split()

numbers = [int(num) for num in numbers]

squares = []
for i in numbers:
    squares.append(i ** 2)


for i in range(len(squares)):
    for j in range(i + 1, len(squares)):
        if squares[i] > squares[j]:
            squares[i], squares[j] = squares[j], squares[i]

print("number:", numbers)
print("squares before sorting", squares)
