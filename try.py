class Pokemon:

    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성 :', end=' ')

    def skill(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬')
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')

    def attack(self, idx):
        pass

class Pickachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f'{self.name}')
    def attack(self, idx):
        self.idx = int(idx)
        print(f'[피까피까] {self.owner}의 {self.name}가 {self.skills[self.idx-1]} 공격 시전!')

class Ggoboogie(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f'{self.name}')
    def attack(self, idx):
        self.idx = int(idx)
        print(f'[꼬북꼬북] {self.owner}의 {self.name}가 {self.skills[self.idx-1]} 공격 시전!')

class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f'{self.name}')
    def attack(self, idx):
        self.idx = int(idx)
        print(f'[파이리이] {self.owner}의 {self.name}가 {self.skills[idx-1]} 공격 시전!')

while True:
    x = int(input('1) 포켓몬 생성 2) 프로그램 종료 :'))
    if x == 1:
        m = int(input('1)피카츄 2) 꼬부기 3) 파이리'))
        o =input('플레이어 이름 입력 : ')
        s = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')

        if m == 1:
            pika = Pickachu(o, s)
            pika.skill()
            atk = input("공격 번호 선택 : ")
            pika.attack(atk)
        elif m == 2:
            ggo = Ggoboogie(o, s)
            ggo.skill()
            atk = input("공격 번호 선택 : ")
            ggo.attack(atk)
        elif m == 3:
            pai = Pairi(o, s)
            pai.skill()
            atk = input("공격 번호 선택 : ")
            pai.attack(atk)
        else :
            print('메뉴에서 골라주세요.')
    elif x == 2:
        print("프로그램을 종료합니다.")
        break
    else :
        print('메뉴에서 골라주세요.')

