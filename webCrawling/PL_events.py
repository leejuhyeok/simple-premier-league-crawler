from selenium import webdriver
from bs4 import BeautifulSoup
import os.path
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome("D:/chromedriver.exe",options=options)

def PL_match_list(year, month):
    for i in month:
        url_2019 = "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=" + str(year) + "&month=" + str(
            i) + "&category=premier"
        driver.get(url_2019)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        day_list = []
        timeList = []
        left_team = []
        left_team_score = []
        right_team_score = []
        right_team = []
        check = True
        size = 1

        day = ""
        time = ""
        left = ""
        right = ""
        while check:
            day_list = soup.select(
                '#_monthlyScheduleList > tr:nth-child(' + str(size) + ') > th > div > em'
            )
            timeList = soup.select(
                '#_monthlyScheduleList > tr:nth-child(' + str(size) + ') > td.time_place > div > span.time'
            )
            left_team = soup.select(
                '#_monthlyScheduleList > tr:nth-child(' + str(size) + ') > td > div > span.team_left > span.name'
            )
            left_team_score = soup.select(
                '#_monthlyScheduleList > tr:nth-child(' + str(size) + ') > td > div > span.team_left > span.score'
            )
            right_team_score = soup.select(
                '#_monthlyScheduleList > tr:nth-child(' + str(size) + ') > td > div > span.team_right > span.score'
            )
            right_team = soup.select(
                '#_monthlyScheduleList > tr:nth-child(' + str(size) + ') > td > div > span.team_right > span.name'
            )
            # 날짜가 없는 child도 있기 때문에 day로 미리 저장해둠
            if day_list and timeList:
                day = day_list[0].get_text()
            if timeList and not left_team_score:
                print(day + " : " + timeList[0].get_text() + "  " + left_team[0].get_text() + " vs " + right_team[
                    0].get_text())
            if timeList and left_team_score and right_team_score:
                print(day + " : " + timeList[0].get_text() + "  " + left_team[0].get_text() + "  " + left_team_score[
                    0].get_text() + " : " + right_team_score[0].get_text() + " " + right_team[
                          0].get_text())
            if not day_list and not timeList:
                break
            # 다음 child 탐색을 위해 size +1 씩 증가시키며 탐색
            size += 1

PL_match_list(2019,range(8,13))
PL_match_list(2020,range(1,6))
driver.quit()