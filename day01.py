import copy
a = ['김지혜', '곽다인', '김설화', '이영철', '조희령']
b = copy.deepcopy(a)
c = a
print(a, b, c)
a[0] = '김인하'
print(a, b, c)
print(id(a), id(b), id(c)) #id가 다름



# literal
# 77=99 에러남
# 'univ' = 'inha' 에러남
# l value = r value

#help("keyword")


# type
#for countdown in 5, 4, 3, 2, 1, "hey!" :
#    print(countdown)
#
#countdown_tuple = (5, 4, 3, 2, 1, "hey!")
#
# countdown_tuple[2] = -99 에러남
#print(countdown_tuple[2]) # 3
#for countdown in countdown_tuple :
#    print(countdown)
#
#tuple을 변경할 수 없으므로 list로 바꿔서 변경
#temp = list(countdown_tuple)
#temp[2] = -99
#countdown_tuple = tuple(temp)
#print(countdown_tuple)



# 화씨 섭씨 온도 변환 프로그램
#(32°F − 32) × 5/9 = 0°C

#fahrenheit = float(input("Imput fahrenheit : "))
#celsius = (fahrenheit - 32.0) * (5.0 / 9.0)
#print('화씨 온도', fahrenheit, '는 섭씨 온도', celsius, '도 입니다.') #comma
#print('화씨 온도 %.2f는 섭씨 온도 %.2f도 입니다.' %(fahrenheit, celsius)) #old style
#print('화씨 온도 {0:.2f}는 섭씨 온도 {1:.2f}도 입니다.'.format(fahrenheit, celsius)) #modern style, format()
#print(f'화씨 온도 {fahrenheit:.2f}는 섭씨 온도 {celsius:.2f}도 입니다.') #newest style, f-string