import random
import time
print('Добро пожаловать в игру камень-ножницы-бумага!')
bot = 0
ti = 0
game = True
while game:
 print('1: камень,  2: ножницы, 3: бумага, 4: закончить игру')
 a = random.randint(1, 3)
 c = int(input())
 if a == 1 and c != 4:
  print('Бот выбрал камень')
 elif a == 2 and c != 4:
  print('Бот выбрал ножницы')
 elif a == 3 and c != 4:
  print('Бот выбрал бумагу')
 if a == c:
  print('Ничья')
 elif a == 1 and c == 2:
  bot += 1
  print('Бот победил')
 elif a == 1 and c == 3:
  ti += 1
  print('Ты победил')
 elif a == 2 and c == 1:
  ti += 1
  print('Ты победил')
 elif a == 2 and c == 3:
  bot += 1
  print('Бот победил')
 elif a == 3 and c == 1:
  bot += 1
  print('Бот победил')
 elif a == 3 and c == 2:
  ti += 1
  print('Ты победил')
 elif c == 4:
  game = False
  print(f'Бот набрал {bot} очков, ты набрал {ti} очков')
  if bot > ti:
   print('Бот тебя победил')
  elif ti > bot:
   print('Ты победил бота')
  elif ti == bot:
   print('Ничья')
 time.sleep(3)
 print('\n')