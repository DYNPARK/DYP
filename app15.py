
 

[딥러닝 포트폴리오를 화려하게9] 모델 생성만큼 중요한 사용자 인터페이스

 

사용자 인터페이스 스케치 부터 결제 페이지 생성 까지 구현하여 수익 구조 만드는 파일럿 프로젝트

 

사용자 인터페이스 = 상용화 

 

yk.mp4
670.12KB
test.mp4
1.70MB
hitter_trained_model.pt
5.95MB
 

 

예제1. streamlit 에서 영상 업로드후 play 시키기 

 


import streamlit as st

# 제목 설정
st.title("Video Player App")

# 파일 업로드
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

# 파일이 업로드되었는지 확인
if uploaded_file is not None:
    # 비디오 플레이어
    st.video(uploaded_file)
else:
    st.write("Please upload a video file to play.")
 

예제2. 원본 영상 옆에 결과 영상 나오게하기


import streamlit as st

# 전체 레이아웃을 넓게 설정
st.set_page_config(layout="wide")

# 제목 설정
st.title("비디오 사물 검출 앱")

# 전체 레이아웃을 컨테이너로 감싸기
with st.container():
    col1, col2 = st.columns(2)  # 열을 균등하게 분배하여 넓게 표시

    # 파일 업로드
    uploaded_file = st.file_uploader("비디오 파일을 업로드하세요", type=["mp4", "mov", "avi"])

    with col1:
        st.header("원본 영상")
        if uploaded_file is not None:
            st.video(uploaded_file)
        else:
            st.write("원본 영상을 표시하려면 비디오 파일을 업로드하세요.")

    with col2:
        st.header("사물 검출 결과 영상")
        if "processed_video" in st.session_state:
            st.video(st.session_state["processed_video"])
        else:
            st.write("여기에 사물 검출 결과가 표시됩니다.")

# 사물 검출 버튼 추가
if st.button("사물 검출 실행"):
    if uploaded_file is not None:
        st.session_state["processed_video"] = uploaded_file
        st.success("사물 검출이 완료되어 오른쪽에 표시됩니다.")
    else:
        st.warning("사물 검출을 실행하려면 비디오 파일을 업로드하세요.")
예제3. 파일 업로드하는 버튼을 위로 올리기

 


import streamlit as st

# 전체 레이아웃을 넓게 설정
st.set_page_config(layout="wide")

# 제목 설정
st.title("비디오 사물 검출 앱")

# 파일 업로드 버튼을 상단으로 이동
uploaded_file = st.file_uploader("비디오 파일을 업로드하세요", type=["mp4", "mov", "avi"])

# 전체 레이아웃을 컨테이너로 감싸기
with st.container():
    col1, col2 = st.columns(2)  # 열을 균등하게 분배하여 넓게 표시

    with col1:
        st.header("원본 영상")
        if uploaded_file is not None:
            st.video(uploaded_file)
        else:
            st.write("원본 영상을 표시하려면 비디오 파일을 업로드하세요.")

    with col2:
        st.header("사물 검출 결과 영상")
        if "processed_video" in st.session_state:
            st.video(st.session_state["processed_video"])
        else:
            st.write("여기에 사물 검출 결과가 표시됩니다.")

# 사물 검출 버튼 추가
if st.button("사물 검출 실행"):
    if uploaded_file is not None:
        st.session_state["processed_video"] = uploaded_file
        st.success("사물 검출이 완료되어 오른쪽에 표시됩니다.")
    else:
        st.warning("사물 검출을 실행하려면 비디오 파일을 업로드하세요.")
 

예제4. 원본영상 옆에 빈화면 표시


import streamlit as st

# 전체 레이아웃을 넓게 설정
st.set_page_config(layout="wide")

# 제목 설정
st.title("비디오 사물 검출 앱")

# 파일 업로드 버튼을 상단으로 이동
uploaded_file = st.file_uploader("비디오 파일을 업로드하세요", type=["mp4", "mov", "avi"])

# 전체 레이아웃을 컨테이너로 감싸기
with st.container():
    col1, col2 = st.columns(2)  # 열을 균등하게 분배하여 넓게 표시

    with col1:
        st.header("원본 영상")
        if uploaded_file is not None:
            st.video(uploaded_file)
        else:
            st.write("원본 영상을 표시하려면 비디오 파일을 업로드하세요.")

    with col2:
        st.header("사물 검출 결과 영상")
        # 사물 검출 결과가 나타날 자리 확보 및 고정 높이 회색 박스 스타일 추가
        result_placeholder = st.empty()
        if "processed_video" in st.session_state and st.session_state["processed_video"] is not None:
            result_placeholder.video(st.session_state["processed_video"])
        else:
            result_placeholder.markdown(
                """
                <div style='width:100%; height:620px; background-color:#d3d3d3; display:flex; align-items:center; justify-content:center; border-radius:5px;'>
                    <p style='color:#888;'>여기에 사물 검출 결과가 표시됩니다.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# 사물 검출 버튼 추가
if st.button("사물 검출 실행"):
    if uploaded_file is not None:
        # 여기에 사물 검출을 수행하는 코드를 추가하고, 결과를 st.session_state["processed_video"]에 저장
        st.session_state["processed_video"] = None  # 실제 결과 영상으로 바꿔야 함
        result_placeholder.markdown(
            "<div style='width:100%; height:500px; background-color:#d3d3d3; display:flex; align-items:center; justify-content:center; border-radius:5px;'>"
            "<p style='color:#888;'>사물 검출 결과 영상이 여기에 표시됩니다.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.success("사물 검출이 완료되어 오른쪽에 표시됩니다.")
    else:
        st.warning("사물 검출을 실행하려면 비디오 파일을 업로드하세요.")
예제5. 사물검출 버튼 색깔 변경하기


import streamlit as st

# 전체 레이아웃을 넓게 설정
st.set_page_config(layout="wide")

# 제목 설정
st.title("비디오 사물 검출 앱")

# 파일 업로드 버튼을 상단으로 이동
uploaded_file = st.file_uploader("비디오 파일을 업로드하세요", type=["mp4", "mov", "avi"])

# 전체 레이아웃을 컨테이너로 감싸기
with st.container():
    col1, col2 = st.columns(2)  # 열을 균등하게 분배하여 넓게 표시

    with col1:
        st.header("원본 영상")
        if uploaded_file is not None:
            st.video(uploaded_file)
        else:
            st.write("원본 영상을 표시하려면 비디오 파일을 업로드하세요.")

    with col2:
        st.header("사물 검출 결과 영상")
        # 사물 검출 결과가 나타날 자리 확보 및 고정 높이 회색 박스 스타일 추가
        result_placeholder = st.empty()
        if "processed_video" in st.session_state and st.session_state["processed_video"] is not None:
            result_placeholder.video(st.session_state["processed_video"])
        else:
            result_placeholder.markdown(
                """
                <div style='width:100%; height:620px; background-color:#d3d3d3; display:flex; align-items:center; justify-content:center; border-radius:5px;'>
                    <p style='color:#888;'>여기에 사물 검출 결과가 표시됩니다.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# 버튼 스타일 설정
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #4d4d4d;  /* 진한 회색 */
        color: #ffffff;             /* 흰색 텍스트 */
        font-weight: bold;          /* 굵은 글씨 */
        padding: 12px 24px;
        font-size: 16px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #333333;  /* 호버 시 더 진한 회색 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 사물 검출 버튼 추가 및 클릭 이벤트 처리
if st.button("사물 검출 실행"):
    if uploaded_file is not None:
        # 여기에 사물 검출을 수행하는 코드를 추가하고, 결과를 st.session_state["processed_video"]에 저장
        st.session_state["processed_video"] = None  # 실제 결과 영상으로 바꿔야 함
        result_placeholder.markdown(
            "<div style='width:100%; height:620px; background-color:#d3d3d3; display:flex; align-items:center; justify-content:center; border-radius:5px;'>"
            "<p style='color:#888;'>사물 검출 결과 영상이 여기에 표시됩니다.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.success("사물 검출이 완료되어 오른쪽에 표시됩니다.")
    else:
        st.warning("사물 검출을 실행하려면 비디오 파일을 업로드하세요.")
