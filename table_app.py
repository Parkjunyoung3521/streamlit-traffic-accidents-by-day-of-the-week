import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt




def run_table_app() :

    st.subheader('사고 발생수 표 화면입니다.')
    
    
    df = pd.read_csv('data/traffic-accidents-week.csv')

    df.index = pd.Index(df['Day_of_the_week'])

    plt.plot(df['Day_of_the_week'],df['Number_of_accidents'])
    plt.show()

    st.dataframe(df)


    st.write('Day_of_the_week : 요일')
    st.write('Number_of_accidents : 사고 발생수')
    st.write('Death_toll : 사망자 수')
    st.write('Serious_injured_toll : 중상자 수')
    st.write('Slightly_injured_toll : 경상자 수')

