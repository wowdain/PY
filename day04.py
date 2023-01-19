import random


#list comprehension
#numbers = [random.randint(1,100) for k in range(5)]


# 홀수로만 5개의 숫자가 담긴 리스트 생성 후 join 활용
numbers = [k for k in range(1, 11) if k % 2]
# index 사용
#for i in range(len(numbers)) :
#    numbers[i] = str(numbers[i])
#print(numbers)
#' '.join(numbers)
#print(numbers)

#list
#temp = list()
#for number in numbers :
#    temp.append(str(number))
#print(temp)

# enumerate
for item in enumerate(numbers) : #(index, value) 튜플 형태로 리턴
    numbers[item[0]] = str(item[1])
print(numbers)

print(' '.join(numbers))

