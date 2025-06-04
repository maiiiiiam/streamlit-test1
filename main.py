import streamlit as st
# import numpy as np
import pandas as pd
# from PIL import Image
import time
st.title('Streamlit 入門')
st.write('Display Image')

#データフレームの表示
df = pd.DataFrame(
    {
        '1列目':[1,2,3,4],
        '2列目':[10,20,50,40],
    }
)
#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=1000,height=1000)#動的
#st.table(df)#静的


# """
# # 章
# ## 節
# ### 項

# python
# import streamlit as st
# import numpy as np
# import pandas as pd
# '''
# """

#グラフ
df2 = pd.DataFrame(
    np.random.randn(20,3),
    columns=list('abc')
)

#st.line_chart(df2)
#st.area_chart(df2)
#st.bar_chart(df2)

#map
df3 = pd.DataFrame(
    np.random.randn(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)
# st.map(df3)

#img

img = Image.open('img/neko.jpg')
# st.image(img,caption='neko',use_column_width=True)

#checkbox
# if st.checkbox('Show Image'):
#     st.image(img,caption='neko',use_column_width=True)

#select box
# option = st.selectbox(
#     '好きな数字を教えて',
#     list(range(1,10))
# )

# st.write('数字は',option,'です。')

#text input
# text = st.text_input('趣味は？')
# st.write('趣味は',text,'です。')


#slider
# condition = st.slider('調子は？',0,100,4)
# st.write('コンデション：',condition)

#side bar
# text = st.sidebar.text_input('趣味は？')
# condition = st.sidebar.slider('調子は？',0,100,4)

# st.write('趣味は',text,'です。')
# st.write('コンデション：',condition)

#カラム分割
# left_column,right_coulumn = st.columns(2)
# button = left_column.button('右カラムに文字を表示')

# if button:
#     right_coulumn.write('右カラム')

#エクスパンだー
# expander = st.expander('問い合わせ')
# expander.write('問い合わせをかく')


#プログレスバー
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(1)

expander = st.expander('問い合わせ')
expander.write('問い合わせをかく')
