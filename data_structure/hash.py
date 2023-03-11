# Hash
# 리스트를 쓸 수 없을 때 -> 인덱스 값을 숫자가 아닌 값으로 사용하고 싶을 때
# 빠른 접근 / 탐색이 필요할 때 -> 시간복잡도가 O(1)이므로
# 집계가 필요할 때 

Animals = {
    'Dog' : {
        'name' : '아롱다롱',
        'age' : 5
    },

    'Cat' : {
        'name' : '야옹이',
        'age' : 7 
    }
}

# 원소 가지고 오기 
# 1. [] 사용
print(Animals['Dog'])

# 2. get()메소드 이용 -> 해당하는 키가 있는 경우, 대응하는 value값을 가지고 옴.

print(Animals.get('Cat',0))

# set
# 값을 넣거나 수정할때 사용.

Animals['Rabbit'] = {'name': '아롱이', 'age': 3}
print(Animals)

# 삭제
# 1. del
# del Animals['Rabbit']
# print(Animals)

# 2. pop
#print(Animals.pop('Rabbit'))

# iterate

# 1. key로만 순회
for key in Animals:
    print(key)

# 2. key - value 동시 순회
for key, value in Animals.items():
    print(key, value)    

# key또는 value만 뽑아내는 방법
# 1. key : keys()
print(Animals.keys())

# 2. value : values()
print(Animals.values())

# 3. 모두: items()
print(Animals.items()) 