import sqlite3
import random

connection = sqlite3.connect('D:\\question.db')
cursor = connection.cursor()

def format():
    global n
    n = random.randrange(1, 10)
    cursor.execute('SELECT * FROM quizQ WHERE id={};'.format(n))
    costya = cursor.fetchall()
    print(costya[0][1])
    cursor.execute('SELECT * FROM answer{}'.format(n))
    costya1 = cursor.fetchall()
    regina = [', '.join(map(str,x )) for x in costya1]
    regina1 = str(regina).replace("'", "")[1:-1]
    print(regina1)
def user():
    try:
        if n == 1:
            a = 1
        if n == 2:
            a = 3
        if n == 3:
            a = 3
        if n == 4:
            a = 2
        if n == 5:
            a = 3
        if n == 6:
            a = 2
        if n == 7:
            a = 1
        if n == 8:
            a = 1
        if n == 9:
            a = 4
        if n == 10:
            a = 3
        user_a = int(input('Your answer: '))
    except Exception as err:
        print('Erorr, go back!', err)
        quit()
    if user_a == int(a):
        print("That's right!")
        
    else:
        print('Not right! Do it again')
        quit()


print('\t***Level_1***')
format()
user()
format()
user()


print('\t***Level_2***')
format()
user()
format()
user()

print('\t***Level_3***')
format()
user()
format()
user()

print('\t***Level_4***')
format()
user()
format()
user()

print('\t***Level_5***')
format()
user()
format()
user()

print('\t***You win!***')

cursor.close()
connection.close()