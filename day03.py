# prime number v0.4

number = int(input('input integer number : '))
is_prime = True #True가 유지되면 소수

for k in range(2, number) :
    if number % k == 0 :
        is_prime = False
        break # 첫번째 약수 발견시 for문 탈출

if is_prime : # is_prime 변수의 True 값이 유지되면 소수
    print(f'{number} is prime number.')
else :
    print(f'{number} is NOT prime number.')
