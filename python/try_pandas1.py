import pandas as pd
# Series = 1D 

data_num = [1, 2, 3, 4, 5]
data_flt = [1.2, 0.7 , 34.25, 0.0027, 3.14159]
data_obj = ['A', 'B', 'C', 'D', 'E']
data_bln = [True, False, True, True, False]
series_num = pd.Series(data_num)
series_flt = pd.Series(data_flt)
series_obj = pd.Series(data_obj)
series_bln = pd.Series(data_bln)
print(series_num)
print(series_flt)
print(series_obj)
print(series_bln)

data_num2 = [100, 102, 104, 106, 108, 110]
series_num2 = pd.Series(data_num2, index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(series_num2, '\n')
# ตัว index สามารถ customize หัวข้อข้อมูลได้ โดยจะใส่อะไรก็ได้ ทั้ง int, float, string, bool, etc.

print(series_num2.loc['a'],'\n') # .loc เป็นการ locate โดยการเรียกหัวข้อขึ้นมา

series_num2.loc['c'] = 6767
print(series_num2,'\n')

print(series_num2.iloc[2]) # เหมือน .loc แต่ใช้ int ในการระบุแทน โดยเริ่มที่ 0 

print(series_num2[series_num2 >= 108])
print(series_num2[series_num2  < 106], '\n')

data_calories = {'Day 1' : 1850 , 'Day 2' : 1720 , 'Day 3' : 1560}
series_calories = pd.Series(data_calories)

series_calories.loc['Day 3'] += 360
series_calories.loc['Day 2'] -= 120
print(series_calories, '\n')

# Dataframes = 2D

data_employee = {
    'Name' : ['Jane', 'Noon', 'Bow'], 
    'Age' : [20, 21, 20]
}

df = pd.DataFrame(data_employee, index = ['Employee #1', 'Employee #2', 'Employee #3'])

print(df, '\n')
print(df.loc['Employee #2'])
print(df.iloc[1], '\n')

# เพิ่ม Column
df['Job'] = ['HR', 'Assistant', 'Developer']
print(df, '\n')

# เพิ่ม Row
new_employee4 = pd.DataFrame([{'Name' : 'Kai', 'Age' : 23, 'Job' : 'N/A'}], 
                              index = ['Employee #4'])
df = pd.concat([df, new_employee4])
print(df, '\n')

# เพิ่มมากกว่า 1 rows
new_employees = pd.DataFrame([{'Name' : 'Shifu',  'Age' : 71,          'Job' : 'Master'           }, 
                              {'Name' : 'Oogway', 'Age' : 'Undefined', 'Job' : 'Transcendentalist'}, 
                              {'Name' : 'Po',     'Age' : 23,          'Job' : 'Dragon Warrior'  }], 
                              index = ['Employee #5', 'Employee #6', 'Employee #7'])
df = pd.concat([df, new_employees])
print(df, '\n')

# Importing (ใช้ไฟล์ชื่อ read_pokemon.py ในไฟล์ others แทนละกัน เดี๋ยวเครื่องจะพังก่อน)
