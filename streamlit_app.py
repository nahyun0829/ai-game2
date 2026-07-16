import random
import streamlit as st

st.set_page_config(page_title="영단어 & BTS", page_icon="✨", layout="centered")

WORDS = [
    ("friend", "친구"),
    ("beautiful", "아름다운"),
    ("school", "학교"),
    ("happy", "행복한"),
    ("library", "도서관"),
    ("science", "과학"),
    ("exercise", "운동"),
    ("favorite", "가장 좋아하는"),
    ("important", "중요한"),
    ("together", "함께"),
]


def start_game():
    quiz_words = WORDS[:]
    random.shuffle(quiz_words)
    st.session_state["quiz_words"] = quiz_words
    st.session_state["current_index"] = 0
    st.session_state["score"] = 0
    st.session_state["checked"] = False
    st.session_state["game_started"] = True


if "game_started" not in st.session_state:
    start_game()

st.title("🌟 영어 공부 + BTS 소개")
st.write("영단어 게임도 하고 BTS도 알아보세요!")

word_tab, bts_tab = st.tabs(["📚 영단어 게임", "🎤 BTS 소개"])

with word_tab:
    st.subheader("영단어 게임")
    st.write("한국어 뜻을 보고 영어 단어를 맞혀보세요.")

    with st.sidebar:
        st.header("게임 방법")
        st.write("1. 뜻을 읽고 영어 단어를 입력해요.")
        st.write("2. 정답 확인 버튼을 눌러요.")
        st.write("3. 다음 문제로 넘어가요.")
        st.button("🎮 새 게임 시작", on_click=start_game, use_container_width=True)

    quiz_words = st.session_state["quiz_words"]
    current_index = st.session_state["current_index"]
    score = st.session_state["score"]

    if current_index >= len(quiz_words):
        st.success("게임이 끝났어요!")
        st.metric("점수", f"{score}/{len(quiz_words)}")
        if score == len(quiz_words):
            st.write("완벽해요! 정말 멋져요. 🎉")
        elif score >= len(quiz_words) // 2:
            st.write("좋아요! 더 많이 맞혀볼까요?")
        else:
            st.write("한 번 더 도전해보세요. 😊")
        st.button("🔁 다시 도전", on_click=start_game, use_container_width=True)
        st.stop()

    word, meaning = quiz_words[current_index]
    st.subheader(f"문제 {current_index + 1}/{len(quiz_words)}")
    st.markdown(f"### 뜻: **{meaning}**")

    answer = st.text_input("영어로 써보세요", key=f"answer_{current_index}")

    if st.button("✅ 정답 확인", use_container_width=True):
        if not answer.strip():
            st.warning("답을 입력해 주세요.")
        else:
            if answer.strip().lower() == word.lower():
                st.success("정답입니다! 🌟")
                st.session_state["score"] += 1
            else:
                st.error(f"아쉬워요. 정답은 '{word}' 입니다.")
            st.session_state["checked"] = True

    if st.session_state.get("checked", False):
        st.write("")
        if st.button("➡️ 다음 문제", use_container_width=True):
            st.session_state["current_index"] += 1
            st.session_state["checked"] = False

    st.write(f"현재 점수: {score}점")

with bts_tab:
    st.subheader("BTS 소개")
    st.write("BTS는 방탄소년단으로, 음악과 메시지로 많은 사람들에게 사랑받는 그룹입니다.")
    st.write("멤버들은 각자 다른 매력을 가지고 있어요.")

    members = [
        ("RM", "리더", "멤버들을 잘 이끌어요."),
        ("Jin", "서브 보컬", "따뜻한 목소리로 유명해요."),
        ("Suga", "래퍼", "감각적인 가사로 유명해요."),
        ("J-Hope", "메인 댄서", "에너지 넘치는 춤이 멋져요."),
        ("Jimin", "메인 댄서", "유려한 춤과 보컬이 좋아요."),
        ("V", "서브 보컬", "부드러운 목소리가 매력적이에요."),
        ("Jungkook", "메인 보컬", "강한 목소리와 춤실력이 뛰어나요."),
    ]

    for name, role, description in members:
        st.markdown(f"- **{name}** ({role}) : {description}")

    st.info("BTS는 '작은 것에서 시작해 큰 꿈을 이루자'라는 메시지를 전해요.")
    st.write("BTS의 음악을 들으면 영어와 한국어를 함께 배우는 재미도 있어요.")
