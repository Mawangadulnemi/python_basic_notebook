import requests
from bs4 import BeautifulSoup
from daum_new_fnc import get_news_title_and_content
# 다음뉴스 목록 페이지에서 여러건의 뉴스(제목+본문) 수집
url="https://news.daum.net/breakingnews/digital"  # 뉴스 목록  url

# 1.뉴스 목록 URL에서 1 건의 뉴스 URL 추출
result=requests.get(url)  # 해당 URL의 전체 소스코드 get
soup=BeautifulSoup(result.text,"html.parser")  # 전체소스코드 bs4 읽기(BS4화)

title_list=soup.select("ul.list_news2 a.link_txt") # BS4로 뉴스제목 목록 추출

for i,content in enumerate(title_list):
    new_url = content["href"]
    title,content=get_news_title_and_content(new_url)  # tuple로 받아 오는 거 그리고 언패킹해서 각각 할당
    print("@"*100)
    print(f'URL: {new_url}')
    print(f"{i+1}뉴스제목: {title}")
    print("@"*100)
    print(f"뉴스본문: {content}")
