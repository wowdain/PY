#list

bigbang = ['지디', '태양', '탑', '대성', '승리']
exo = ['백현', '첸']

exo.insert(1, '시우민')
exo.append(bigbang) # ['백현', '시우민', '첸', ['지디', '태양', '탑', '대성', '승리']]

exo[3].pop() # 승리 제거

exo[3].pop(2) # 탑 제거

#exo.remove('대성') # 대성못찾음
exo[3].remove('대성') # 대성제거

del exo[2] # 첸 제거