print ('Hello' , 'World')

if 6 < 7 :
print ('6767')

Premium_Gourmet = ('Full Course')
print (Premium_Gourmet)
# ห้ามใช้ตัวแปรซ้ำ และตัวเลขเป็นตัวกำหนดตัวแปร

# เก็บข้อมูล
x = ('Hello' , 3 , 6.7 , True , False , 3 + 2i)

income = 3000
expense = 150
remain = (income - expense)
print (remain)

# มี Operator + - * / ด้วย ไล่ตาม PEMDAS เลย (ถ้าเป็น ** จะเป็นเลขยกกำลัง)
# มี % ด้วย เรียกว่า modulo ใช้ในการหาเศษเหลือ เช่น x % y
x = 10
y = 2
z = 6
result = ((x + y) / z)
if result := 2 :
    print (result)

# ใช้ ชนิดข้อมูล(input(ใส่ข้อความข้างหน้าอินพุทตรงนี้)) ตรงนี้ถ้าไม่ครอบจะนับว่าเป็น str ไปโดยปริยาย (แต่ก็ยังใช้ใช้เป็น str ไปได้นะ)
pi = 3.14
r = int(input('Enter your Radius : '))
area = pi * r * r # หรือใช้เป็น pi * r ** 2 ก็ได้
print(area)

# อย่างเช่น พื้นที่สามเหลี่ยมจะได้ดังนี้
x = int(input('Enter your Base width :'))
y = int(input('Enter your Height :'))
area = (1 / 2) * x * y
print('Area of your triangle is ' , area ,'sq.m')

# ถ้าใช้ if แล้ว ต้องใช้ " == " เพื่อเปรียบเทียบค่า (ถ้าใช้ " = " จะทำให้คิดว่าเป็นการกำหนดดัวแปรแทน)
if 5 == 2 :
    print('yes yes yes')
else :
     print('no no no')

# และ and or สามารถใช้ได้เหมือนในตรรกศาสตร์ ม.4 เลย
# แล้วตรง if อาจใส่วงเล็บเพื่อความเรียบร้อยได้ อย่าง if(ประพจน์ใด ๆ) :

import time
word = input('Insert your word here : ')
for n in range(len(word) + 1) :
    print(word[0:n])
    time.sleep(0.06)

a = int(input('Insert your number here : '))

if a % 2 == 0 :
    print('It\'s an even number!')
else :
    print('It\'s an odd number!')

mylist = ['banana' , 'หมู หมึก ไก่' , 256 , 6.7 , True ]

print(mylist)

# ใช้ .append เพื่อเพิ่มข้อมูลตรงตำแหน่งท้ายสุด
mylist.append(input('What do you want to add right here :\n' ))
print(mylist)

# ใช้ .insert เพื่อแทรกข้อมูลเข้าที่ตำแหน่งนั้น ๆ
mylist.insert(int(input('Which position do you want to add :\n')),
input('What do you want to add :\n'))
print(mylist)

# mylist[1] = 'ปลาทอง'  <- เพื่อเปลี่ยนข้อมูลในตำแหน่งนั้น ๆ ให้เป็น input ที่เราใส่เข้าไปใหม่

# ใช้ .remove เพื่อเอาข้อมูลที่เราพิมพ์ไปออก (ถ้าข้อมูลชื่อเหมือนกัน จะเอาตัวที่อยู่หน้าก่อนออก)


# i ย่อมาจาก index นะ
# ส่วน import time แค่อยากใส่ time.sleep() ให้มันช้า ๆ เล่นเฉย ๆ
import time
mylist = ['banana' , 'หมู หมึก ไก่' , 256 , 6.7 , True ]

i = 0

while i < 5 :
    print(mylist[i])
    i = i + 1
time.sleep(0.5)

print('Ended')
time.sleep(0.5)


i = 0
mylist2 = []
print('What 5 things do you want to add here ?')
while i < 5 :
    mylist2.append(input())
    i = i + 1

print('Here you are!\n' , mylist2)

mylist2.sort()
print(mylist2)

mylist2.sort(reverse = True)
print(mylist2)

mylist_extra = [123 , 256 , 6.7]
mylist_extra.extended(mylist2)
print(mylist2)

print(mylist_extra.index(6.7))
# .index จะบอกตำแหน่งออกมาเป็น int (โดยเริ่มจากตำแหน่งที่ 0 เหมือนเดิม)

mylist_extra = ['123' , '256' , '6.7']

i = mylist_extra.index('256')
mylist_extra[i] = input('What do you want to replace?\n: ')

print(mylist_extra)

mylist_extra.reverse()
print(mylist_extra)

# ตัว for ลูป จะใช้รันสมาชิกทั้งหมดในเซต อย่างเช่น ตัวอักษรใน str หรือจะเป็นสมาชิกใน [] ก็ได้ (หรือนำไปทำอย่างอื่นได้อีก)
# และไม่ต้องใส่ i = i + 1 เหมือนใน  while ลูป ด้วย

for i in 'Hello World' :
     print(i)

mylist3 = ['ยาย' , 'กิน' , 'ลำไย' , 'น้ำลาย' , 'ยาย' , 'ไหล' , 'ย้อย']
for i in mylist3 :
    print(i) 
print('\n')
      
i = 0
while i < 7 :
    print(mylist3[i])
    i = i + 1

# break เป็นโอเปอเรเตอร์ที่เอาไว้ใส่หลัง ลูป (while loop / for loop) แล้วทำให้ตอนโค้ดรัน จะหลุดออกจากลูปไปเลย
for i in range(10) : 
    if i == 7 :
        break
    print(i)

# และอย่าลืมว่าลำดับบรรทัดและการวรรคในแต่ละ condition มีความสำคัญด้วย
for i in range(10) :
        print(i)
        if i == 7 :
            break

# sort ตัวเลข
# a = []
# n = input('')
# x = int(n)
# for i in range(x) :
#   a.append(int(input()))
# a.sort()
# print(a)
# print(a[0])
# print(a[x - 1])

# a=input()
# b=input()
# c=input()
# d=int(a)
# e=int(b)
# f=int(c)
# x=d+e+f

# if x>=80 :
#   print('A')
# elif x>=75 :
#   print('B+')
# elif x>=70 :
#   print('B')
# elif x>=65 :
#   print('C+')
# elif x>=60 :
#   print('C')
# elif x>=55 :
#   print('D+')
# elif x>=50 :
#   print('D')
# else :
#   print('F')

# if a.isupper() :
#  print('All Capital Letter')
# elif a.islower() :
#  print('All Small Letter')
# else :
#  print('Mix')
