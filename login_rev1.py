import streamlit as st
import requests

# ログイン関数
def login():
    st.title("ログイン")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")
    login_button = st.button("ログイン")

    if login_button:
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.experimental_rerun()

# ユーザー認証関数
def authenticate_user(username, password):
    # 実際のユーザー認証処理をここに追加する
    return username == "user" and password == "password"

def main():
    st.session_state.logged_in = getattr(st.session_state, "logged_in", False)

    if not st.session_state.logged_in:
        login()

if __name__ == '__main__':
    main()
