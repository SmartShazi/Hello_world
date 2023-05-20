# def decode_map(mapfile,ddict,outfile):

#     f = open(mapfile,'r')
#     data = f.read()

#     a = ''
#     for i in data:
#         if i in ddict:
#             a += ddict[i]
#         else:
#             a += i
#     f.close()
#     f = open(outfile,'w')
#     f.write(a)
#     f.close()

# d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', '#': ' '}
# decode_map('encoded_map.txt',d1,'decoded_map.txt')

#     for i in mapfile:
#         if i in ddict:
#             a += ddict[i]
#         else:
#             a += i
#     f.close()
#     f = open(outfile,'w')
#     f.write(a)
#     f.close()

# d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', '#': ' '}
# decode_map('encoded_map.txt',d1,'decoded_map.txt')

# l = [1,2,3,4,5]

# def add(x):
#     a = [1,2,3,4,5]
#     b=[]
#     for i in a:
        
#         print(i, end= ' ')
#         i= i+x
#         print(i)
#     print(a)
# add(1)    


# def func(x):
#     return x+1

# for x in l:
#     func(x)
# print(l)


# print([func(x) for x in l])



# dic1={"a":1,"b":2}
# for (key, value) in dic1.items():
#     print(f'{key}'+'c')

# pdict={"a":1,"b":2}

# print(1 in pdict.values())

# class value1():
#     def __init__(self, is_in_value):
#         for key,value in pdict.itmes():
#             if in f'{value}':


# def check(name1, name2, pdict):
#     if pdict[name1] and pdict[name2] in value1:
        


# def is_related(name1,name2,pdict):
#     set1 = {}
#     for key,value in pdict.items():
#       while pdict[name1] and pdict[name2] in f'{value}':
#         try:
#             set1.append(name1,name2)
#             name1 = pdict[name1]
#             name2 = pdict[name2]
#             if pdict[name1] and pdict[name2] not in f'{value}':
#                 return False
            
#             # is_related(name1,name2,pdict)
#         except:
#             return True


# dic= {'a':1, 'b':2}
# for (key, value) in dic:
#     print(f'{value}')

# pdict={"a":1,"b":2}
# if 1 in pdict.values():
#     print('yes')

# def decode_map(mapfile,ddict):
#     with open(mapfile,'r') as f:
#         for line in f:
#             print(line)
        # data = f.read()
        # a = ''
        # for i in data:
        #     print(i)

# d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', '#': ' '}
# decode_map('encoded_map.txt', d1)


# def create_game_matrix(r,c):
#     output = []
#     for i in range(r):
#         row = []
#         for j in range(c):
#             row.append(0)
#         output.append(row)
#     return output

# def print_TTT(game):
#     for i in range(3):
#         print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
#         if i !=2:
#             print('-----')

# def ttt_gameplay():
#     game = create_game_matrix(3,3)
#     for i in range(3):
#         for j in range(3):
#             game[i][j] = i*3+j+1
#     player = 0

#     print_TTT(game)
#     for i in range(9): 
#         print()
#         valid_move = False
#         while not valid_move:
#             pos = int(input(f'Player {piece[player]} move:'))
#             valid_move = check_valid_move(game,pos)
#             if not valid_move:
#                 print(f'Your move {pos} is not valid')
#         pos -= 1
#         game[pos//3][pos%3] = piece[player]
#         winner = check_win(game)
#         if winner:
#             print(f'Player {winner} won!!! Game over.')
#             print_TTT(game)
#             return
#         player = 1 - player
#         print_TTT(game)

#     print('No one won. It\'s a tie game.')

# piece = ['X','O']
# game1 = [[1,2,3],[4,5,6],[7,8,9]]
# game2 = [['X',2,3],['X',5,6],['X',8,9]]
# game3 = [['O',2,3],[4,'O',6],[7,'O',9]]
# game4 = [['X',2,'X'],[4,'O',6],['X','O','X']]
# game5 = [['X','X','O'],['X','O','X'],['O','X','X']]

############################################
########### End of do not modify ###########
############################################

############
## Task 1 ##
############

# def check_valid_move(game,inp):
#     return True

# print(check_valid_move(game1, 4))
# print(check_valid_move(game1, 10))
# print(check_valid_move(game2, 4))
# print(check_valid_move(game4, 4))
# print(check_valid_move(game5, 4))
# print(check_valid_move(game2, 1))
# print(check_valid_move(game5, -9))

############
## Task 2 ##
############

# def check_win(game):
#     return ''

# print(check_win(game1))
# print(check_win(game2))
# print(check_win(game3))
# print(check_win(game4))
# print(check_win(game5))

#############################################################
## Uncomment and run ttt_gameplay() below to test the game ##
#############################################################



# def check_valid_move(game,inp):
#         for lists in game:
#                 if inp not in game:
#                         return False
#                 elif inp >= 10:
#                         return False
#                 elif inp<= 0:
#                         return False
#                 else:
#                         return True


# game2 = [['X',2,3],['X',5,6],['X',8,9]]
# def check_win(game):
#         a = 0
#         b = 0
#         c = 0
#         d = 0
#         e = 0
#         f = 2
#         g = 0
#         h = 2 
#         i = 0
        
#         for lists in game:
#                 print(lists)
#                 if lists == ['O','O','O']:
#                         return 'O'
#                 if lists == ['X','X','X']:
#                         return 'X'
#                 if lists[a] == 'O':
#                         b+=1
#                         print('b=' + b)
#                         if b == 3:
#                                 return 'O'
#                 if lists[a] == 'X':
#                         c+=1
#                         print(c)
#                         if c == 3:
#                                 return 'X'
#                 if lists[d] == 'X':
#                         d+=1
#                         if d == 3:
#                                 return "X"
#                 if lists[e] == 'O':
#                         e+=1
#                         if e == 3:
#                                 return "O"
#                 if lists[f] == 'X':
#                         f-=1
#                         g+=1
#                         if g == 3:
#                                 return 'X'
#                 if lists[h] == 'X':
#                         h-=1
#                         i+=1
#                         if i == 3:
#                                 return 'X'
#                 else:
#                         a+=1
#         if 3 not in [b,c,d,e]:
#                 return ''
# check_win(game2)


# x = "awesome"

# def myfunc():
#         global x
#         x = "fantastic"
#         print("Python is " + x)

# myfunc()

# int1 = 6
# while x != 0:
#         x = int1%2
#         a = str(6%2)
#         b = 6//2
#         c = str(b)+a
# print(c)

# for i in range(4):
#         print(i)


# 字符串 string 字母或者数字
# variable 变量 名字的代称
# integer 整数

# list 目录 清单

# list1 = [2,3,4]
# list1.insert(0,1)
# list1.reverse()
# list1.append(1)
# list1.reverse()
# print(list1)


# print(list1[1] + 5)
# print(list1)
# list1.append(1)
# print(list1)
# list1.insert(1 , 5)
# list1.sort()
# print(list1)
# list1.remove(2)
# print(list1)
# dictionary 字典 格式{x:a}
# a = "strings"
# dict_friends_age = {'FengHa':21, 'Cai': 18}
# print(dict_friends_age['FengHa'])
# tuple 
# b = ('anything')
# tuple1 = (4,5)

# float 带小数点的数字
# bool 区分正负 对错 1+1=2-》 True   1+1 = 3 False
# function 函数 一个编辑出来的功能


# print('hello world')
# print('1+1')
# age_Cai = 18 
# name_Cai = 'Cai XinZhi'
# my_name = ' and Feng Ha'
# # print(age_Cai)
# print(name_Cai)
# print('Cai XinZhi')

# print(5/3)
# print(5%2)

# number = input('Enter a number: ')
# print('the number is: ', number)

# abcd

# return 返回一个值 值得类型可以是integer, string, bool,list

# def fk(number1, num2):
#         list1 = [1,2,3]
#         list1.append(number1)
#         list1.append(num2)

#         return  list1

# print(fk(10,20))

# print(add(10,40))


# def say_hi():
#         print("hello_world")

# say_hi()

# for loop while loop

# list1 = [1,2,3]
# list2 = []
# for eachthing in list1:
#         list2 = []
#         list2.append(eachthing+1)
# print(list2)


# print(a)
# while a < 10 :
#         a += 1 
#         print(a)


# def check(a):
#         if a < 10:
                
#                 a += 1
#                 print(a)
#         # else if 
#         elif 20 < a < 30:
#                 a -= 1
#                 print(a)
#         elif a >=30:
#                 pass
#         else:
#                 print('wrong number')

# check(15)

# list1 = [1,2,3,4,5,6,7]
# print(len(list1))
# # for i in list1:
# #         print(i)
# def check_list():
#         while len(list1) >= 5:
#                 list1.pop()
#                 print(list1)
# check_list()

# a = 0
# list1 = []
# def make_list():
#         while a <=5 :
#                 a += 1
#                 list1.append(a)
                
#                 print(list1)



# for i in range(10):
#         print((i))
# 12 = list1[:]
# print(list1[:])
# print(list1)

# print([1,2,3,4,5,6,7][2:4])

# print(int('1'))
# []


# def can_nm(parameter):
#         return 'can nmlgb can ', parameter

# print(can_nm('can'))

# print(ord("d"))
# print(ord('D'))

# dict1 = {'a':1, 'b':2}
# print(dict1.values())

# DIR_UP = "u"
# DIR_DOWN = "d"
# DIR_LEFT = "l"  
# DIR_RIGHT = "r"
# BLANK_PIECE = "Z"
# def legal_move(board, position, direction):
#     # position is (row, col)
#     col_num = position[1]
#     row_num = position[0]
#     row_max = len(board[0])
#     col_max = len(board)

#     if direction == 'd':
#         col_num += 1
#     if direction == 'u':
#         col_num -= 1
#     if direction == 'l':
#         row_num -= 1
#     if direction == 'r':
#         row_num += 1 

#     if col_num > col_max or col_num < 0:
#         return False
#     if row_num > row_max or row_num < 0:
#         return False
#     # if board[][]
#     # position1 = (row_num, col_num)
#     color = board[row_num][col_num]
#     try:
        
#         if board[row_num+1][col_num] == color:
#             return True
#     except: pass    
#     try:
#         if board[row_num][col_num+1] == color:
#             return True
#     except: pass
#     try:
#         if board[row_num-1][col_num] == color:
#             return True
#     except:pass
#     try:
#         if board[row_num][col_num-1] == color:
#             return True
#     except:pass

#     return False

# print(legal_move([["A", "A", "D", "C"], ["A", "B", "C", "A"], ["C", "B", "B", "A"], ["C", "D", "D", "D"]], (1, 2), "u"))
def ret_fal():
    return  False
def che():
    ret_fal()
    print(1)
print(che())
def check():
    return ret_fal
check()




# def validate_input(board, position, direction):
#     dict1 = {}
#     for i in board:
#         if len(i) != len(board):
#             return False
#         if len(i) < position[1]:
#             return False
#     if len(board) < 2 or len(board[0]) < 2:
#         return False
#     for i in board:
#         for j in i:
#             if j.isupper() == False:
#                 return False
            
#     if len(board) < position[0]:
#         return False
#     if direction not in 'udlr':
#         return False
#     for i in board:
#         for j in i:
#             if j not in dict1:
#                 dict1[j] = 1
#             elif j in dict1:
#                 dict1[j] += 1
#     for key,value in dict1.items():
#         if value%4 != 0:
#             return False
    
#     return True

# print(validate_input([["A", "A", "A", "A"], ["A", "A", "A", "A"]], (0, 0), "u"))