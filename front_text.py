import streamlit as st
import pandas as pd

# 타이틀 적용 예시
st.title('AI News')

# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
#st.title('스마일 :sunglasses:')

# Header 적용
st.header('#01')
# 일반 텍스트
st.text('#날짜 표시에 대해서 고민중입니다.')



# CSV 파일을 읽어와서 데이터 테이블로 노출
@st.cache_data  # 데이터를 캐싱하여 빠르게 로드할 수 있도록 함
def load_data(file_path):
    data = pd.read_csv(file_path,index_col=0)
    return data


# CSV 파일 로드
csv_file_path = "AI.csv"
data = load_data(csv_file_path)



# Section1
html_code = """
<div style='background-color: #f0f0f0; padding-left: 10px; border-radius: 5px;'>
    <h3 style='text-align: left; color: #333;'>Section 1</h1>
</div>
"""

# st.markdown() 함수에 HTML 코드 문자열 전달
st.markdown(html_code, unsafe_allow_html=True)

# Streamlit 앱 제목 설정
st.title('크롤링한 데이터 표시 예제')

# 데이터 프레임 출력
st.write("크롤링한 데이터:")
st.data_editor(data,column_config={'주소': st.column_config.LinkColumn('주소')},hide_index=True)

#Section2
html_code = """
<div style='background-color: #f0f0f0; padding-left: 10px; border-radius: 5px;'>
    <h3 style='text-align: left; color: #333;'>Section 2</h1>
</div>
"""

# st.markdown() 함수에 HTML 코드 문자열 전달
st.markdown(html_code, unsafe_allow_html=True)

# Streamlit 앱 제목 설정
st.title('크롤링한 데이터 표시 예제')

# 데이터 프레임 출력
st.write("크롤링한 데이터:")
st.data_editor(data,column_config={'주소': st.column_config.LinkColumn('주소')},hide_index=True)

#Section3
html_code = """
<div style='background-color: #f0f0f0; padding-left: 10px; border-radius: 5px;'>
    <h3 style='text-align: left; color: #333;'>Section 3</h1>
</div>
"""

# st.markdown() 함수에 HTML 코드 문자열 전달
st.markdown(html_code, unsafe_allow_html=True)

# Streamlit 앱 제목 설정
st.title('크롤링한 데이터 표시 예제')

# 데이터 프레임 출력
st.write("크롤링한 데이터:")
st.data_editor(data,column_config={'주소': st.column_config.LinkColumn('주소')},hide_index=True)