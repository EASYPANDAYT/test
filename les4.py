name = 'Добрыня Попович'
hp = 100
horse = 1
slave = 2
print ( 'У ', name, 'есть', hp, 'жизней,', horse, 'конь,', slave, 'раба.' )
print (name, 'путешествует, и на пути ему встретилась река с мостом хрупким.')
print ('Перед', name, 'стоит выбор: бросить коня, или попытаться пройти с ним.')
choice = input ('Что выберешь? ')
if choice == 'Бросить коня':
    print ('С', name, 'всё хорошо и он пошел дальше с', slave , 'рабами')
elif choice == 'Пройти с ним':
    hp = hp - 30
    print ('Конь утонул а,',name , 'потерял 30 жизней, и у него осталось', hp , 'жизней')
else:
    print ('Нет такого выбора или напиши с заглавной')
if hp == 100:
    print (name ,'вскоре встретились татаро-монголы и требуют в дань одного раба')
    choice = input ("Отдать раба или биться?")
    if choice == 'Отдать раба':
        slave = slave - 1
        print ('Монголы забрали раба, и у', name, 'осталось',slave'рабов')
    elif choice = 'Биться' :
        hp == hp - 30
        print ('Ты потерял 30 жизней,но отбил раба, теперь у тебя', hp ,'жизней')

