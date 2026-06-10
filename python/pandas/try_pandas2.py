import pandas as pd

# เลือกตาม column
df = pd.read_csv('/workspaces/codespaces-blank/python_experiment/others/pokemon.csv', index_col= 'Name')

# ลอง print แบบรวมและแยก
print(df)
print(df.to_string())
print(df['Name'].to_string)
print(df['Attack'].to_string)
print(df['Name','Type 1','Type 2','Total'].to_string)

# เลือกตาม row
print(df.loc[6]) # Locate 
print(df.loc['Charizard' : 'Metapod', ['Attack', 'Sp. Atk']])
print(df.iloc[0 : 20, 0 : 4])


# ใช้ .loc เพื่อหา data ที่เราต้องการ
find_pokemon = input('What pokemon are you finding?\n')

try :
    print(df.loc[find_pokemon])
except KeyError :
    print(f'{find_pokemon} not found')


# หรือใช้ print(read.to_string()) เพื่อให้มาทั้งหมดเลยก็ได้ แต่ถ้า print(read) อย่างเดียว ข้อมูลจะมาแค่ 5 อันแรก และ 5 อันสุดท้าย

# Filtering โดยการเพิ่มเงื่อนไข
legend = df[df['Legendary'] == True]
print(legend.to_string)
print(legend['Legendary'].to_string())

fire1 = df[df['Type 1'] == 'Fire']
fire2 = df[df['Type 2'] == 'Fire']
fire1 = pd.concat([fire1 , fire2])
print(fire1[['Type 1','Type 2']].to_string())


# Aggregation

# 1. Whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count)

# 2. Single column
print(df['Attack'].mean()) # ตรงนี้ไม่ต้องใส่ (numeric_only = True ก็ได้ เพราะทั้งหมดเป็นตัวเลขอยู่แล้ว)
print(df['Total'].sum())
print(df['Attack'].min())
print(df['Defense'].max())
print(df[df['Legendary'] == True].count())

group = df.groupby('Type 1')
print(group['Attack'].mean())


# Data Cleaning 

# 1. เอาส่วนที่ไม่ต้องการให้แสดงข้อมูลออหก (ไม่ใช่การลบข้อมูลนะ)
df = df.drop(columns=['Legendary', 'Sp. Atk', 'Sp. Def'])
print(df)

# 2. เอาตัวที่เกิด missing data ออก (na = Not Available)
df = df.dropna(subset = ['Type 2'])
df = df.fillna({'Type 2' : 'ไม่มี'})

# 3. แทนที่ข้อมูลที่จะ output ออกมา
df = df['Type 1'].replace({'Fire'   : 'ไฟ',
                           'Water'  : 'น้ำ', 
                           'Grass'  : 'พืช',
                           'Poison' : 'พิษ'})
print(df)

# 4. Standardize โดยการทำให้เป็นทั้งพิมพ์เล็กทั้งหมด
df['Type 2'] = df['Name'].str.lower()
print(df)
