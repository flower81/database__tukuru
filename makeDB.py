# coding: utf-8

import sqlite3

dbName = input('作るデータベースの名前を入力してください' + '\n')
tbName = input('作るテーブルの名前を入力してください' + '\n')

conn = sqlite3.connect(dbName + '.db')
curs = conn.cursor()

curs.execute('CREATE TABLE ' + tbName + ' (userID INTEGER, lastName TEXT, firstName TEXT)')

sql = 'INSERT INTO ' + tbName + ' (userID, lastName, firstName) values (?, ?, ?)'

ipID = input('ID（入社日+誕生日）は? => ')
lName = input('苗字は? => ')
fName = input('名前は? => ')

sqlData = (ipID, lName, fName)

curs.execute(sql, sqlData)

conn.commit()

sql = ("SELECT * FROM " + tbName)

curs.execute(sql)

result = curs.fetchall()

for userID, lastName, firstName in result:
    print(userID, lastName, firstName)
