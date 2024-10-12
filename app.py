# https://qiita.com/sypn/items/80962d84126be4092d3c

import streamlit as st
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree


# === 基礎機能 ===
st.title('streamlit Tutorial')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('---------- Hello World! ----------')

# x**2
input_num = st.number_input('Input a number', value=0)
result = input_num ** 2
st.write('Result: ', result)

# ダミーデータの作成
st.text('--------------------')
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
})
st.write(df)
st.dataframe(df)

# ファイルのアップロード
st.text('--------------------')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(uploaded_file)

# ボタン
st.text('--------------------')
if st.button('Say hello'):
    st.write('Hello World!')

# チェックボックス
st.text('--------------------')
if st.checkbox('Show/Hide'):
    st.write('Some text')

# ラジオボタン
st.text('--------------------')
option = st.radio(
    'Which number do you like best?', 
    ['1', '2', '3']
)

# スライダー
st.text('--------------------')
value = st.slider('Select a value', 0, 100, 50) # min, max, default

# テキスト入力ボックス
st.text('--------------------')
text_input = st.text_input('Input', 'Input some text here.')
text_area = st.text_area('Text Area', 'Input some text here.')

# ボタンを押したら3秒間出力を待つ
st.text('--------------------')
if st.button('start'):
    with st.spinner('processiong...'):
        time.sleep(3)
        st.write('end!')

# Sidebarの選択肢を定義する
st.text('--------------------')
options = ["Option 1", "Option 2", "Option 3"]
choice = st.sidebar.selectbox("Select an option", options)

# 2列のカラムを作成
st.text('--------------------')
col1, col2 = st.columns(2)
# col1にテキストを表示
with col1:
    st.header("Column 1")
    st.write("This is column 1.")
# col2にDataFrameを表示
with col2:
    st.header("Column 2")
    # DataFrameを表示
    st.write(df)


# === グラフの描画 ===
st.text('--------------------')
# グラフを描画する
def plot_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)
# グラフを表示するボタンを表示する
if st.button('Plot graph'):
    plot_graph()

# === データベースとの連携 ===
st.text('--------------------')
# データベースに接続する
conn = sqlite3.connect('example.db')
c = conn.cursor()
# データを表示する
def show_data():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    for d in data:
        st.write(d)
# データを追加する
def add_data(name, age):
    c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    st.write('Data added. Please reload page.')
# データベースにテーブルを作成する
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)')
# データの表示
show_data()
# データの追加
name = st.text_input('Name')
age = st.number_input('Age')
if st.button('Add data'):
    add_data(name, age)
# データベースをクローズする
conn.close()

# === 機械学習モデルの可視化 ===
st.text('--------------------')
# Warningの非表示
#st.set_option('deprecation.showPyplotGlobalUse', False)  # なぜか使えない
# データをロードする
iris = load_iris()
X, y = iris.data, iris.target
# モデルを学習する
model = DecisionTreeClassifier()
model.fit(X, y)
# モデルを可視化する
def plot_model():
    plot_tree(model)
    st.pyplot()
# モデルを表示するボタンを表示する
if st.button('Plot model'):
    plot_model()
