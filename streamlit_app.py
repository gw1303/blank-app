import streamlit as st
import time
import pyperclip

# ============================================================================
# PLACEHOLDER FUNCTIONS - 사용자가 실제 로직을 구현할 부분
# ============================================================================

def search_naver_news(keyword):
    """
    Naver API를 통해 뉴스를 검색하는 함수
    Args:
        keyword (str): 검색할 키워드
    Returns:
        list: 100건의 뉴스 기사 리스트 (각 기사는 dict 형태)
    """
    # TODO: 실제 Naver API 호출 로직 구현
    # 임시 mock 데이터
    time.sleep(1)  # API 호출 시뮬레이션
    return [
        {"title": f"뉴스 제목 {i+1}: {keyword} 관련 기사", "url": f"https://news.example.com/{i+1}"}
        for i in range(100)
    ]


def filter_articles_with_llm(articles):
    """
    LLM을 통해 100건의 기사 중 5-7건을 필터링하는 함수
    Args:
        articles (list): 검색된 100건의 기사 리스트
    Returns:
        list: 필터링된 5-7건의 기사 리스트
    """
    # TODO: 실제 LLM 필터링 로직 구현
    time.sleep(1.5)  # LLM 처리 시뮬레이션
    return articles[:6]  # 임시로 앞 6건 반환


def crawl_article(article_url):
    """
    기사 URL을 크롤링하여 본문을 가져오는 함수
    Args:
        article_url (str): 기사 URL
    Returns:
        str: 기사 본문 텍스트
    """
    # TODO: 실제 크롤링 로직 구현
    time.sleep(0.1)  # 크롤링 시뮬레이션
    return f"이것은 {article_url}의 본문 내용입니다. 실제로는 크롤링된 전체 기사 내용이 여기에 들어갑니다."


def summarize_with_llm(article_content):
    """
    LLM을 통해 기사를 요약하는 함수
    Args:
        article_content (str): 기사 본문
    Returns:
        str: 요약된 기사 내용
    """
    # TODO: 실제 LLM 요약 로직 구현
    time.sleep(0.1)  # LLM 처리 시뮬레이션
    return "이것은 LLM이 생성한 기사 요약입니다. 주요 내용을 간결하게 정리한 텍스트가 여기에 표시됩니다."


# ============================================================================
# STREAMLIT UI
# ============================================================================

# 페이지 설정
st.set_page_config(
    page_title="뉴스 검색 & 요약",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS
st.markdown("""
<style>
    /* 전체 배경 및 폰트 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    /* 헤더 스타일 */
    .header-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #666;
        font-size: 1.1rem;
        font-weight: 300;
    }
    
    /* 검색 섹션 */
    .search-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* 기사 카드 */
    .article-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 4px solid #667eea;
    }
    
    .article-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    }
    
    .article-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 1rem;
        line-height: 1.4;
    }
    
    .article-summary {
        font-size: 1rem;
        color: #4a5568;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .article-url {
        font-size: 0.9rem;
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    .article-url:hover {
        color: #764ba2;
        text-decoration: underline;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* 입력 필드 */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 0.75rem;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* 로딩 스피너 */
    .stSpinner > div {
        border-color: #667eea !important;
    }
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("""
<div class="header-container">
    <div class="main-title">📰 뉴스 큐레이터</div>
    <div class="subtitle">키워드로 뉴스를 검색하고 AI가 핵심 내용을 요약해드립니다</div>
</div>
""", unsafe_allow_html=True)

# # 검색 섹션
# st.markdown('<div class="search-container">', unsafe_allow_html=True)

# Form을 사용하여 엔터키로 검색 가능하게 함
with st.form(key="search_form", clear_on_submit=False):
    col1, col2 = st.columns([4, 1])
    
    with col1:
        keyword = st.text_input(
            "검색 키워드",
            placeholder="예: 신세계백화점, 패션, 쇼핑 등...",
            label_visibility="collapsed",
            key="keyword_input"
        )
    
    with col2:
        search_button = st.form_submit_button("🔍 검색", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 세션 스테이트 초기화
if 'summarized_articles' not in st.session_state:
    st.session_state.summarized_articles = None

# 검색 실행
if search_button and keyword:
    # 1단계: Naver API로 100건 검색
    info_placeholder_1 = st.empty()
    success_placeholder_1 = st.empty()
    
    with st.spinner("🔍 뉴스를 검색하는 중..."):
        info_placeholder_1.info("📡 Naver API에서 뉴스를 검색하고 있습니다...")
        all_articles = search_naver_news(keyword)
        info_placeholder_1.empty()
        success_placeholder_1.success(f"✅ {len(all_articles)}건의 뉴스를 찾았습니다!")
        time.sleep(0.5)
        success_placeholder_1.empty()
    
    # 2단계: LLM으로 5-7건 필터링
    info_placeholder_2 = st.empty()
    success_placeholder_2 = st.empty()
    
    with st.spinner("🤖 AI가 중요한 기사를 선별하는 중..."):
        info_placeholder_2.info("🧠 LLM이 기사를 분석하고 필터링하고 있습니다...")
        filtered_articles = filter_articles_with_llm(all_articles)
        info_placeholder_2.empty()
        success_placeholder_2.success(f"✅ {len(filtered_articles)}건의 주요 기사를 선별했습니다!")
        time.sleep(0.5)
        success_placeholder_2.empty()
    
    # 3단계: 크롤링 및 요약
    info_placeholder_3 = st.empty()
    success_placeholder_3 = st.empty()
    
    info_placeholder_3.info("📝 선별된 기사를 크롤링하고 요약하고 있습니다...")
    
    summarized_articles = []
    progress_bar = st.progress(0)
    
    for idx, article in enumerate(filtered_articles):
        # 크롤링
        content = crawl_article(article['url'])
        # 요약
        summary = summarize_with_llm(content)
        
        summarized_articles.append({
            'title': article['title'],
            'summary': summary,
            # 'url': article['url']
            'url': 'https://www.naver.com'
        })
        
        progress_bar.progress((idx + 1) / len(filtered_articles))
    
    progress_bar.empty()
    info_placeholder_3.empty()
    success_placeholder_3.success("✅ 모든 기사 요약이 완료되었습니다!")
    time.sleep(0.5)
    success_placeholder_3.empty()
    
    # 세션 스테이트에 결과 저장
    st.session_state.summarized_articles = summarized_articles

# 결과 표시 (세션 스테이트에 결과가 있으면 표시)
if st.session_state.summarized_articles:
    summarized_articles = st.session_state.summarized_articles
    
    # 결과 표시
    st.markdown("---")
    st.markdown("## 📋 요약된 뉴스 기사")
    
    for idx, article in enumerate(summarized_articles, 1):
        st.markdown(f"""
        <div class="article-card">
            <div class="article-title">📌 {article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <a href="{article['url']}" target="_blank" class="article-url">🔗 원문 보기 →</a>
        </div>
        """, unsafe_allow_html=True)
        
        if idx < len(summarized_articles):
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # 클립보드 복사 버튼
    st.markdown("---")
    
    # 복사할 텍스트 생성
    clipboard_text = ""
    for idx, article in enumerate(summarized_articles, 1):
        clipboard_text += f"[ 기사 {idx} ]\n"
        clipboard_text += f"제목: {article['title']}\n"
        clipboard_text += f"요약: {article['summary']}\n"
        clipboard_text += f"URL: {article['url']}\n"
        clipboard_text += "\n\n"

    # 복사 버튼 (중앙 정렬)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📋 전체 뉴스 클립보드에 복사", use_container_width=True, key="copy_button"):
            pyperclip.copy(clipboard_text)
            success_placeholder_2 = st.empty()
            success_placeholder_2.success("✅ 클립보드에 복사되었습니다!")
            time.sleep(0.5)
            success_placeholder_2.empty()

elif search_button and not keyword:
    st.warning("⚠️ 검색할 키워드를 입력해주세요!")

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(0, 0, 0, 0.7); padding: 1rem;">
    <small>💡 Tip: 구체적인 키워드를 입력하면 더 정확한 결과를 얻을 수 있습니다</small>
</div>
""", unsafe_allow_html=True)
