import streamlit as st
import pandas as pd
import numpy as np
from table_app import run_table_app
from graph_app import run_graph_app






def main():
    st.title("교통사고 통계 데이터")

    menu = ['Home','Table','Graph','소계']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home' :
        st.subheader('요일별로 교통사고 발생 수를 보여주는 앱입니다.')

    elif choice == 'Table' :
        run_table_app()

    elif choice == 'Graph' :
        run_graph_app()

    else :
        st.subheader('데이터는 도로교통공단의 교통사고 통계 데이터입니다. (2019년도 데이터)')
        
        st.subheader('경찰에서 조사, 처리한 교통사고에 대한 통계 정보로 인적 피해가 있는 사고만 집계하였습니다.')

        st.subheader('요일별 교통사고의 사고 건수, 사망자 수, 중상자 수, 경상자 수, 부상신고자 수 통계자료')
    
        st.subheader('교통사고분석시스템(http://taas.koroad.or.kr)의 데이터를 바탕으로 하였습니다.')


if __name__ == '__main__' :
    main()