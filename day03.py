# prime number v0.5
# 두 개의 숫자 사이(입력된 두 수 포함)의 소수를 출력하는 프로그램

number_list = input('input 2 integer number : ').split()
start = int(number_list[0]) #first number
end = int(number_list[1]) #second number

for number in range(start, end+1):
    is_prime = True

    if number <= 1 :
        is_prime = False
    else :
        for k in range(2, number) :
            if number % k == 0 :
                is_prime = False
                break
        else :
            print(number, end=' ')
