import streamlit as st
from streamlit_lottie import st_lottie
import requests

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
        # Load animations
        about_animation = self.load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_khzniaya.json")
        skills_animation = self.load_lottie_url("https://lottie.host/11b0507d-a3e3-42f2-b132-d99987108b8e/kD6JveEHks.json")
        fun_animation = self.load_lottie_url("https://lottie.host/366d5fd0-6c1c-4ed8-82bd-65ea3e32f5a2/2ZC5H08LKH.json")

        # Title and Introduction
        st.title("Welcome to My Digital Portfolio 🌟")
        st.write("""
        Hi there! I'm thrilled to have you here. This space showcases my professional journey, personal interests, 
        and the projects that inspire me. Feel free to explore, engage, and connect!
        """)

        # Interactive Tabs for Content Sections
        tab1, tab2, tab3 = st.tabs(["About Me", "Skills & Expertise", "Fun Facts 🎉"])

        with tab1:
            st_lottie(about_animation, height=300, key="about")
            st.header("About Me")
            st.write("""
            I'm an information security enthusiast diving deep into modern systems and technologies. 
            My work focuses on analyzing security frameworks, exploring cutting-edge research, 
            and enhancing digital safety.
            """)
            # Interactive Form
            st.subheader("Connect with Me!")
            with st.form("contact_form"):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Message")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    st.success("Thank you for reaching out! I'll respond to your message soon.")

        with tab2:
            st_lottie(skills_animation, height=300, key="skills")
            st.header("Skills & Expertise")
            st.write("""
            Here's a snapshot of my skills:
            - **Information Security**: Threat analysis, risk assessment, and policy design.
            - **Research & Literature Reviews**: Synthesizing complex ideas into actionable insights.
            - **Programming & Tools**: Python, Streamlit, and more!
            """)
            selected_topics = st.multiselect(
                "Explore more about my skills:",
                ["Threat Mitigation", "Streamlit Development", "Research Analysis", "Python Programming"]
            )
            if selected_topics:
                st.write("You picked these topics:")
                for topic in selected_topics:
                    st.markdown(f"- **{topic}**")

        with tab3:
            st_lottie(fun_animation, height=300, key="fun")
            st.header("Fun Facts 🎉")
            st.write("""
            When I'm not working, I enjoy:
            - Listening to lyrical music with rich medium and low frequencies.
            - Watching epic shows like 'Game of Thrones' or 'Breaking Bad.'
            - Discovering unconventional ways to tackle problems.
            """)
            # Interactive Slider
            fun_level = st.slider(
                "Rate how much fun this page is (be honest!):",
                1, 10, value=7
            )
            if fun_level >= 8:
                st.balloons()
                st.write("Yay! I'm glad you're enjoying it. 🎈")
            elif fun_level <= 4:
                st.write("Let me know how I can improve!")

        # Sidebar: Quick Links
        st.sidebar.title("Connect with Me 💌")
        st.sidebar.write("Quick links to my profiles:")
        st.sidebar.button("Email Me")
        st.sidebar.button("Visit LinkedIn")
        st.sidebar.button("Check GitHub")

# Instantiate and run the Home app
if __name__ == "__main__":
    home = Home()
    home.app()
