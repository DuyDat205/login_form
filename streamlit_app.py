import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8501"

def get_access_token(code):
    url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

def get_user_info(token):
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    st.set_page_config(page_title="GitHub Login", page_icon="🔒")
    st.title("🔐 Login with GitHub")

    query_params = st.experimental_get_query_params()

    if "code" in query_params:
        code = query_params["code"][0]
        token = get_access_token(code)
        if token:
            user = get_user_info(token)
            st.success(f"✅ Logged in as {user['login']}")
            st.image(user['avatar_url'], width=100)
            st.write("👤 Name:", user.get("name", "Not available"))
            st.write("📧 Email:", user.get("email", "Not available"))
        else:
            st.error("⚠️ Failed to retrieve access token.")
    else:
        github_auth_url = (
            f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
        )
        st.markdown(f"[🔗 Click here to login with GitHub]({github_auth_url})")

if __name__ == "__main__":
    main()
