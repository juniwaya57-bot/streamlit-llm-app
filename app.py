from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

def call_llm(user_text: str, expert_type: str) -> str:
    if expert_type == "健康アドバイザー":
        system_prompt = "あなたは健康に関するアドバイザーです。安全で信頼できるアドバイスだけを提供してください。"
    elif expert_type == "ITコンサルタント":
        system_prompt = "あなたは経験豊富なITコンサルタントです。ビジネスや技術に関する分かりやすい助言を提供してください。"
    else:
        system_prompt = "あなたは親切なアシスタントです。"

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_text),
    ]

    result = llm.invoke(messages)
    return result.content

st.title("LLMアプリ（LangChain × Streamlit）")
st.write("### LangChain を使った LLM Web アプリのデモ")
st.write(
    """
    このアプリでは、入力フォームに相談内容を入力し、AI が回答を返します。
    また、ラジオボタンで AI に振る舞わせる専門家を選択できます。
    """
)

expert_type = st.radio(
    "アシスタントのタイプ（専門家）を選択してください：",
    ["健康アドバイザー", "ITコンサルタント"],
)

user_text = st.text_input("質問や相談内容を入力してください：")

if st.button("送信"):
    if user_text:
        with st.spinner("AI が回答を生成しています..."):
            answer = call_llm(user_text, expert_type)
        st.success("回答：")
        st.write(answer)
    else:
        st.error("入力内容を入力してから送信してください。")
