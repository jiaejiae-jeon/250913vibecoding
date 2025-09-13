import streamlit as st
st.title('지애의 첫 웹앱!')
st.title('이걸 내가 만들었다고?!')


import streamlit as st
"각 사이트의 '트렌드' 페이지로 바로 이동할 수 있는 링크를 제공해요."
)


# User selection
category = st.selectbox("관심 있는 항목을 고르세요:", [
"전체 추천 (기본)",
"매거진 / 에디토리얼 (Vogue, Harper's Bazaar, ELLE)",
"트렌드 리포트 / 데이터 (Pinterest, WGSN)",
"온라인 트렌드 & 쇼핑 가이드 (WhoWhatWear 등)",
"소셜 미디어 트렌드 추적 (TikTok, Vogue Business)",
])


st.write("---")


# Hard-coded curated list (keeps app simple & reliably runnable)
SITES = [
{
"name": "Vogue — Trends",
"desc": "런웨이와 셀럽 스타일을 반영한 시즌별 트렌드 기사와 룩북.",
"url": "https://www.vogue.com/fashion/trends",
"tag": "매거진"
},
{
"name": "Who What Wear — Trends",
"desc": "실용적인 스트리트스타일, 쇼핑 팁, 소셜 미디어 트렌드 정리.",
"url": "https://www.whowhatwear.com/fashion/trends",
"tag": "쇼핑/온라인"
},
{
"name": "Pinterest Predicts / Trend Reports",
"desc": "데이터 기반의 시즌별 트렌드 예측(무료 리포트 포함).",
"url": "https://business.pinterest.com/pinterest-predicts/",
"tag": "데이터/리포트"
},
{
"name": "Harper's Bazaar — Fashion",
"desc": "하이패션과 대중 트렌드를 폭넓게 다루는 에디토리얼.",
"url": "https://www.harpersbazaar.com/fashion/",
"tag": "매거진"
},
{
"name": "Vogue Business — TikTok Trend Tracker",
"desc": "TikTok에서 떠오르는 패션 관련 바이럴 아이템과 데이터를 정기적으로 분석.",
"url": "https://www.voguebusiness.com/fashion/the-vogue-business-tiktok-trend-tracker",
"tag": "소셜"
},
{
"name": "WGSN (예측, 유료)",
"desc": "전문 패션 예측 서비스(기업/디자이너 대상). 무료는 아님.",
"url": "https://www.wgsn.com/en/products/fashion",
"tag": "예측(유료)"
},
]


# Filter by category
if category.startswith("전체"):
filtered = SITES
elif "매거진" in category:
filtered = [s for s in SITES if s["tag"] == "매거진"]
elif "데이터" in category:
filtered = [s for s in SITES if s["tag"] == "데이터/리포트" or s["tag"] == "예측(유료)"]
elif "쇼핑" in category:
filtered = [s for s in SITES if s["tag"] == "쇼핑/온라인"]
else:
filtered = [s for s in SITES if s["tag"] == "소셜"]


for s in filtered:
st.subheader(s["name"])
st.write(s["desc"])
st.markdown(f"[사이트 열기]({s['url']})")
st.write("\n")


st.write("---")


st.sidebar.header("사용법 & 배포")
st.sidebar.write(
"1. 이 코드를 `app.py` 로 저장하세요.\n"
"2. GitHub에 푸시한 뒤 Streamlit Cloud(https://streamlit.io/cloud)에서 리포지토리를 연결하면 바로 배포됩니다.\n"
)


st.sidebar.write("앱 개선 아이디어:")
st.sidebar.write("- 각 사이트의 최신 기사 제목을 자동으로 가져오기(추가로 requests/BeautifulSoup 필요)\n- TikTok/Instagram의 해시태그 실시간 트래킹(공식 API 필요)\n- 지역/스타일(스트리트/하이패션/빈티지) 필터 추가")


st.caption("참고: 일부 전문 예측 서비스(WGSN 등)는 유료입니다.")


st.success("완료! 위 링크를 눌러 지금 유행하는 스타일을 확인해보세요.")
