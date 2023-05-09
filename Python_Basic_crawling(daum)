# 파이썬 심화과정
# - 웹 크롤링: 웹 페이지에서 원하는 데이터를 수집
# -모듈: beautifulesoup4, selenium, requests



#인공지능 개발 과정
# 1.데이터 수집
# 2.데이터 저장
# 3.탐색적 데이터 분석(EDA)
# 4.데이터 전처리
# 5.데이터 변환
# 6.베이스라인 모델 개발
# 7.성능 향상
# 8.시각화
# 9.배포 및 서비스


# 웹 서비스
# - HTML(메인), CSS, Javascript : 웹 표준



# Daum News의 제목, 본문 수집 코드

import requests
from bs4 import BeautifulSoup

# requests:웹 사이트 코드 복사 GET
# BeautifulSoup: requests Get 해온 코드에서 필요한 정보만 find해서 가져오기


url="https://v.daum.net/v/20230509090530015"  # 수집 할 페이지 주소
result = requests.get(url)


# 웹 브라우저                                 네이버 서버
#           request  ----------->>>>>>>>
#                     <<<<<<<<<<<<<<----------- response
# response[200]: success
# response[400~500]: fail
print(result)
print()
print(result.text)


# requests로 가져온 코드 -> Beasutifulsoup한테 넘겨주고 읽기(request는 요청밖에 못하니까)
doc= BeautifulSoup(result.text, "html.parser")  # beautifulsoup화 한것, buaufifulsoup을 이용할 거니까
title=doc.select("h3.tit_view")[0].get_text() # 기존에 값이 하나인 리스트 였으므로 []를 빼주기 위해 [0]을 적음
contents = doc.select("section>p")  # section 태그 안에 있는 p 태그들


print("@"*100)
print(f"뉴스제목: {title}")
print("@"*100)
content=""  # 전체 본문을 담을 변수
contents.pop(-1)  # 제보는 뭐시기 내용 삭제
for tag in contents:
   content+=tag.get_text()
print(f"뉴스본문: {content}")



