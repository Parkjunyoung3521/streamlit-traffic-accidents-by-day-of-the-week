import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import altair as alt



def run_graph_app() :

    st.subheader('사고 발생 시 피해 정도를 보여줍니다.')
    
    df1 = pd.read_csv('data/traffic-accidents-week.csv')

    taw_list = df1.columns.tolist()
    print(taw_list)

    taw_list = taw_list[1:]

    selected_taw_list = st.multiselect('선택하시오.',taw_list)

    print(selected_taw_list)

    if len(selected_taw_list) != 0 :

        
        df_selected = df1[selected_taw_list]
        
        st.line_chart(df_selected)

        st.area_chart(df_selected)

    st.write('Number_of_accidents : 사고 발생수')
    st.write('Death_toll : 사망자 수')
    st.write('Serious_injured_toll : 중상자 수')
    st.write('Slightly_injured_toll : 경상자 수')


