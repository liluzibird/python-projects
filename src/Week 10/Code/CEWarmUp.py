import sqlite3
con = sqlite3.connect("D:\\Skool\\SAC\\FALL 2022\\CMPR 114\\Week 10\\Code\\ContactsDB.db")
cur = con.cursor()

cur.execute('''Select * from Contacts where phone like '%112%' ''')

results = cur.fetchall()


print('ContactID	Name	Phone	Address	City	State')
for id_, name, phone, address, _addressneveruse, city, state, in results:
	print(f'{id_:9} {name:14} {phone:11} {address:9} {address:9} {str(city):9} {state:2}')


con.commit()
con.close()