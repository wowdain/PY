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
#for item in enumerate(numbers) : #(index, value) 튜플 형태로 리턴
#    numbers[item[0]] = str(item[1])
#print(numbers)
#
#print(' '.join(numbers))


#copy

#copy
#a = [1, 2, 3]
#b = a.copy()
#c = list(a)
#d = a[:]
#print(a, b, c, d)

#a = [1, [9, -7], 3]
#b = a.copy()
#c = list(a)
#d = a[:]
#a[1][0] = -99 # b, c, d 전부 바뀌어버림, 왜냐 리스트 안의 리스트는 mutable 하므로 -> 얕은 복사가 이루어 진 것
#print(a, b, c, d)

#import copy
#b=copy.deepcopy(a)
#a[1][1] = 'inha' # b는 바뀌지 않음 -> 깊은 복사를 했음
#print(a, b)



# test01
groups = {
    '빅뱅': ['GD', '태양', '탑', '대성', '승리'],
    '마마무' : ['문별', '솔라', '휘인', '화사']}

if(groups.keys == '빅뱅' & )
