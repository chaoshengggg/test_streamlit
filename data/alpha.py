import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import win32com
import smtplib
import ssl
import pythoncom
from PIL import Image
import base64


# Tab Title
st.set_page_config(page_title='DBI BackOffice',page_icon='📊', layout='wide')

# Front Page
st.markdown("""
<style>
.big-font {
    font-size:100px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🔎 DBI BackOffice</p>', unsafe_allow_html=True)
st.subheader('Welcome to DBI BackOffice !')



def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()

# def add_logo():
#     with open("C:/Users/chaos/Dropbox/VSC/project/logo.png", "rb") as f:
#         image = f.read()
#         b64 = base64.b64encode(image).decode()
#         url = f"data:image/png;base64,{b64}"
        
#     st.markdown(
#         f"""
#         <style>
#             [data-testid="stSidebarNav"] {{
#                 background-image: url({url});
#                 background-repeat: no-repeat;
#                 padding-top: 120px;
#                 background-position: 50% 50%;
#                 background-size: contain;
#                 height: 150px;
#             }}
#             [data-testid="stSidebarNav"]::before {{
#                 content: "My Company Name";
#                 margin-left: 20px;
#                 margin-top: 20px;
#                 font-size: 30px;
#                 position: relative;
#                 top: 100px;
#             }}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

# add_logo()



# User Authentication
users = {
    "test": "1234",
}
def user_authentication():
    with st.sidebar:
        st.title("**Log in**")
        #st.markdown('Please fill in your credentials below to start using !')
        username = st.text_input('**Username**',placeholder='Enter your username')
        password = st.text_input('**Password**',placeholder='Enter your password',type='password')

        if st.sidebar.button('Login'):
            if username in users and users[username] == password:
                st.success("Logged in as {}".format(username))
            else:
                st.error("Incorrect username or password")
user_authentication()



## Animation
def load_lottie(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation=load_lottie('https://assets10.lottiefiles.com/packages/lf20_2UeWRZ.json')

with st.container():
    st.write('---')
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        with st.container():
            st.header('Harnessing the power of data to make better business decisions')
            st.markdown('*Our team of analysts & scientist leverages cutting-edge tools and techniques to deliver insights that drive your business forward*')
            image = Image.open(r'C:\Users\chaos\Dropbox\VSC\project\picture.PNG')
            resized_image = image.resize((500, 600))
            st.image(resized_image)
    with middle_column:
        with st.container():
            st.subheader('Who are we ?')
            st.markdown("We're a team of Data Analysts & Data Scientist who turns complex data into meaningful insights !")
            st.subheader('What sort of work do we specialize on ?')
            st.markdown("We cover anything related to automating, reporting & analysis, dashboarding, machine learning - you name it !")
            st.subheader('What is our working hour ?')
            st.markdown("Weekdays GMT+8 10AM to 7PM")

    with right_column:
        with st.container():
            st_lottie(animation, height=500, key='coding')


## Contact Form
def contact ():
    with st.container():
        st.header('Need insights ? Get in touch with us!')
        #st.subheader('Enter details below')
        with st.form('form1', clear_on_submit =True):
            name = st.text_input('Enter Name', placeholder='Please enter your name')
            email = st.text_input('Enter Email', placeholder='Please enter your email address')
            message = st.text_input('Message', placeholder='Please enter your text here')
            submit = st.form_submit_button('Submit')

            if submit == True:
                try:
                    pythoncom.CoInitialize()
                    outlook = win32com.client.Dispatch("Outlook.Application")
                    mail = outlook.CreateItem(0)
                    mail.To = 'cs.chong@blacksire.com'  # Replace with your email address
                    #mail.Subject = subject
                    mail.Body = f"Name: {name}\nEmail: {email}\n\n{message}"
                    mail.Send()
                    st.success('Thank you for your message! We will get back to you soon.')
                except AttributeError as e:
                    st.error('Please have your Outlook application open when submitting this form.')
                except Exception as e:
                    st.error(f"Error sending email: {e}")
                finally:
                    mail = None
                    outlook = None
                    pythoncom.CoUninitialize()
contact()


# Hide Footnote
hide_st_style= '''
                <style>
                #header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                '''
st.markdown(hide_st_style, unsafe_allow_html=True)

            







