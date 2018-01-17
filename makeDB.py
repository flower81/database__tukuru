# coding: utf-8

import sqlite3

# 入力の変数を宣言
dbName = input('作るデータベースの名前を入力してください' + '\n')
tbName = input('作るテーブルの名前を入力してください' + '\n')

# DBの作成とDBを操作するための変数を宣言
conn = sqlite3.connect(dbName + '.db')
curs = conn.cursor()

# テーブルを作成し、カラムは値・テキストが2つ
curs.execute('CREATE TABLE ' + tbName + ' (userID INTEGER, lastName TEXT, firstName TEXT)')

# テーブルにレコードを追加
sql = 'INSERT INTO ' + tbName + ' (userID, lastName, firstName) values (?, ?, ?)'

# レコードの内容を入力するための変数を宣言
ipID = input('ID（入社日+誕生日）は? => ')
lName = input('苗字は? => ')
fName = input('名前は? => ')

# 入力変数を使いテーブルに追加する構文を作成
sqlData = (ipID, lName, fName)

# 構文を実行する
curs.execute(sql, sqlData)

# 実行結果をDBに反映させる
conn.commit()

# テーブルの内容を全表示させる構文を宣言
sql = ("SELECT * FROM " + tbName)

# 構文を実行する
curs.execute(sql)

# 実行結果を変数に格納
result = curs.fetchall()

# 実行結果を1行ずつ出力させる
for userID, lastName, firstName in result:
    print(userID, lastName, firstName)
