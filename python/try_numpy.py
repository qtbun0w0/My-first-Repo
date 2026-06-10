# อันนี้คือ list ธรรมดาเฉย ๆ

# mylist = [1, 2, 3, 4]
# mylist = mylist*2
# print(mylist)

# ส่วนอันนี้คือในส่วนของ numpy

import numpy as np

array_num1= np.array([1, 2, 3, 4])

# array_num1 = array_num1 ** 2
print(array_num1)
print(type(array_num1),'\n')
# ตัว operation จะทำงานต่างกันเมื่อใช้ตัว array

array_0dim = np.array('A')
array_1dim = np.array(['A', 'B', 'C'])
array_2dim = np.array([['A', 'B', 'C'],
                      ['D', 'E', 'F'],
                      ['G', 'H', 'I']])
array_3dim = np.array([
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]
])

print(array_0dim)
print(array_0dim.ndim,array_0dim.shape,'\n')
print(array_1dim)
print(array_1dim.ndim,array_1dim.shape,'\n')
print(array_2dim)
print(array_2dim.ndim,array_2dim.shape,'\n')
print(array_3dim)
print(array_3dim.ndim,array_3dim.shape,'\n')
# อันนี้คือ Dimension ของ array ซึ่งจะมีมากกว่านี้ก็ได้

# การเรียกใช้สมาชิก จะสามารถเรียกได้โดยใช้ array[row,column,depth,...]
print(array_3dim[0,2,2],'\n') # จะได้ 'I' ออกมา
print(array_3dim[2],'\n') # จะได้ ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' '] มาหมดเลย

# Note : Column = 1 แถวแนวตั้ง , Row = 1 แถวแนวนอน
# เราสามารถ slice สมาชิกใน array ได้ด้วย
print(array_3dim[0:1]) # จะได้ row แรกมา (เริ่มนับแถว 0 หยุดที่แถว 1 แต่ไม่นับ 1)

# สามารถสั่งให้ array ไล่ index กลับหลังได้โดยการใส่เลขติดลบเช่นกัน
# print(array(row_start : row_end : row_stop , column_start : column_end : column_stop , ... ))

# Scalar arithmetics
print(array_num1)
print(array_num1 + 1)
print(array_num1 - 2)
print(array_num1 * 3)
print(array_num1 / 4)
print(array_num1 ** 5)
# ข้างบนกำหนดไว้ก่อนหน้านี้ว่า array_num = np.array([1, 2, 3, 4])


# Vectorized Math Functions
array_num2 = np.array([1.2 , 5.33 , 9.81 , 3.14])

print(np.sqrt(array_num2))
print(np.round(array_num2)) 
print(np.floor(array_num2))
print(np.ceil(array_num2))
print(np.pi) # pi = π

# Element-wise arithmetic
array_num3 = np.array([1, 3, 5, 7, 9 ])
array_num4 = np.array([2, 4, 6, 8, 10])

print(array_num3 + array_num4)
print(array_num3 - array_num4)
print(array_num3 * array_num4)
print(array_num3 / array_num4)
print(array_num3 ** array_num4)

# Comparison Operators

array_scores = np.array([75, 87, 39, 59, 100, 95, 44, 67])

print(array_scores == 100) # This will print as boolean values (True / False)
print(array_scores >= 50)

array_scores[array_scores < 60] = 0 # Right here, if anyone gets below 60, their scores will automately become 0
print(array_scores)

# Brodcasting เป็นการทำ operation ระหว่าง 2 array ที่ต่างกัน โดยต้องเข้าหนึ่งในเงื่อนไขต่อไปนี้
# ต้องมีมิติที่เท่ากันทุกประการ เช่น 3*3 & 3*3 , 2*4 & 2*4
# ต้องมีมิติในด้านใดที่มี index เพียง 1 ตัว เช่น 3*1 & 1*3 , 1*5 & 5*1
# นอกจากนั้นจะขึ้น ValueError


array41 = np.array([1, 2, 3, 4])
array14 = np.array([[1], [2], [3], [4]])

print(array41.shape)
print(array14.shape)
print(array41*array14)

# Aggregate functions เป็นการสรุปข้อมูลทั้งหมด
array_num5 = np.array([[1, 2, 3, 4, 5],
                       [6, 7, 8, 9, 10]])

print(np.sum(array_num5))
print(np.mean(array_num5))
print(np.std(array_num5))
print(np.var(array_num5))
print(np.min(array_num5))
print(np.max(array_num5))
print(np.argmin(array_num5)) # บอกตำแหน่งของค่าที่น้อยที่สุด
print(np.argmax(array_num5)) # บอกตำแหน่งของค่าที่มากที่สุด

print(np.sum(array_num5 , axis = 0)) # รวมข้อมูล row 1 & row 2
print(np.sum(array_num5 , axis = 1)) # รวมข้อมูล column 1 & column 2

# Filtering

array_age = np.array([[19, 23, 18, 20, 17, 45, 16, 21],
                       [21, 19, 20, 23, 28, 18, 16, 51]])

teenager = array_age[array_age < 18]
print(teenager)

adult = array_age[(array_age >= 18) & (array_age < 65)] # and = & และ or = |
print(adult)

senior = array_age[array_age >= 40]
print(senior)

even = array_age[array_age % 2 == 0]
print(even)

odd = array_age[array_age % 2 != 0]
print(odd)

adult2 = np.where(array_age >= 18 , array_age , 0)
print(adult2) # กำหนดว่าใครที่อายุไม่เข้า 18 ให้เลขเป็น 0 ไป (หรือจะกำหนดเป็นอย่างอื่นก็ได้)

# Random numbers

rand = np.random.default_rng(seed = 999) # ตรง seed เป็นชุดข้อมูลของค่าที่ล็อกไว้ ทำงานเหมือน seed ใน Minecraft เลย
print(rand.integers(low = 1, high = 7, size = (3, 3)))
# กำหนดให้สุ่มจำนวนเต็ม โดยที่ค่าต่ำสุดเป็น 1, ค่าสูงสุดเป็น 6 (ไม่นับ 7), ขนาด array/เมทริกซ์ คือ 3*3

np.random.seed(seed = 111)
rand_float = np.random.uniform(low = -1, high = 1, size = (2, 3))
print(rand_float)

# สลับตำแหน่งของ index แบบสุ่ม
rng = np.random.default_rng()

array_rand = np.array([1, 2, 3, 4, 5])
rng.shuffle(array_rand)
print(array_rand)

# หยิบสุ่ม index มาแบบ  n * n มิติ
rng = np.random.default_rng()

fruits = np.array(['แอปเปิล', 'มะละกอ', 'กล้วย', 'ส้ม'])
fruits = rng.choice(fruits, size = (5, 5))
print(fruits)

fruits_slot = np.array(['💰','7️⃣','🍎','🧧'])
fruits_slot = rng.choice(fruits_slot, size = (3, 5))
print(fruits_slot)
