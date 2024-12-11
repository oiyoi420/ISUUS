import streamlit as st
from streamlit_lottie import st_lottie
import requests
from datetime import datetime

class Home:
    def __init__(self):
        pass

    def load_lottie_url(self, url):
        """Load Lottie animation from a URL."""
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()

    def app(self):
        st.set_page_config(
            page_title="Creative One Page App",
            page_icon="🌟",
            layout="centered",
            initial_sidebar_state="collapsed",
        )

        # Apply custom styles for dark theme


        # Header
        st.markdown(
            """
            # 🌟 Welcome to the Dark Themed App!
            A single-page app designed with creativity and simplicity in mind.
            """
        )

        # Display the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.markdown(f"**Current Time:** {current_time}")

        # User Interaction Section
        st.markdown("## ✨ Interact with the App")
        user_name = st.text_input("What's your name?", placeholder="Enter your name...")

        if user_name:
            st.success(f"Hello, {user_name}! Enjoy exploring this creative space.")

        # Fun Feature: Random Motivational Quote
        st.markdown("## 💡 Motivation of the Moment")
        quotes = [
            "Believe in yourself and all that you are!",
            "Your limitation—it’s only your imagination.",
            "Dream it. Wish it. Do it.",
            "Stay positive. Work hard. Make it happen.",
            "Success is not final; failure is not fatal."
        ]
        import random
        if st.button("Get a Quote"):
            st.markdown(f"**Quote:** _{random.choice(quotes)}_")

        # Image Section
        st.markdown("## Add Some Color")
        fun_animation = self.load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_49rdyysj.json")
        st_lottie(fun_animation, height=300, key="travel")

        # Footer
        st.markdown("""
        ---
        **Crafted with love and creativity.**
        """)

if __name__ == "__main__":
    home = Home()
    home.app()