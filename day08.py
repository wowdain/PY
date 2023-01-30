

def d(name, ps):
    print(name, ps)


m = int(input('1)피카츄 2) 꼬부기 3) 파이리'))
name = input('플레이어 이름 입력 : ')
skl = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
if m == 1:
    pika = d(name, skl)
    print(type(name), type(skl))
