import streamlit as st
import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from apscheduler.schedulers.blocking import BlockingScheduler


# 실행할 함수 선언
global df

def news_crawling():
    # (1) 링크 생성 (네이버 뉴스)
    # keyword = input("수집하고자 하는 앱 이름을 입력하세요 :")
    keyword = 'upstage'
    url = f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}'

    # (2-1) 브라우저를
    browser = webdriver.Chrome()
    time.sleep(3)

    # (2-2)  페이지 이동
    browser.get(url)
    time.sleep(3)

    # (3) 주단위 선택(1주)
    browser.find_element(By.XPATH, '//*[@id="snb"]/div[1]/div/div[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="snb"]/div[2]/ul/li[3]/div/div[1]/a[4]').click()

    # (4) 뉴스기사 스크랩
    parent = browser.find_element(By.CLASS_NAME, "list_news._infinite_list").find_elements(By.CLASS_NAME, "bx")

    news_list = []

    for elem in parent:
        company = elem.find_element(By.CLASS_NAME, "info.press").text
        headline = elem.find_element(By.CLASS_NAME, "news_contents").find_element(By.CLASS_NAME, "news_tit").text
        News_summary = elem.find_element(By.CLASS_NAME, "news_contents").find_element(By.CLASS_NAME,
                                                                                      "api_txt_lines.dsc_txt_wrap").text
        link = elem.find_element(By.CLASS_NAME, "news_contents").find_element(By.CLASS_NAME, "news_tit").get_attribute(
            'href')

        news_list.append({
            "발행사": company,
            "제목": headline,
            "요약": News_summary,
            "주소": link
        })

    # (5) 데이터 프레임 및 저장
    df = pd.DataFrame(news_list)
    #df.to_csv(f'{keyword}.csv', encoding='utf-8-sig')

    st.title('데이터프레임 튜토리얼')

    # DataFrame 생성

    # DataFrame
    # use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
    st.dataframe(df, use_container_width=False)

    # 테이블(static)
    # DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
    st.table(df)


# 스케줄러 인스턴스 생성
scheduler = BlockingScheduler()

# 매일 정해진 시간에 작업 예약
scheduler.add_job(news_crawling, 'cron',  second=0) #1분마다 실행
#scheduler.add_job(news_crawling, 'cron',  hour=8, minute=0)  # 매일 오전 8시 00분에 실행
#매주 아침 8시
# scheduler.add_job(my_job, 'cron', day_of_week='mon', hour=8, minute=30)

# 스케줄러 시작
scheduler.start()




