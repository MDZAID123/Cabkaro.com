from streamlit_option_menu import option_menu
import hydralit_components as hc
import streamlit as st
import time
import mysql.connector as c
import pandas as pd
import requests

from streamlit_lottie import st_lottie
from PIL import Image
from random import randint
# con=c.connect(host="localhost", user="root", passwd="12345", database="mideval")
con = c.connect(host="localhost", user="root",
                passwd="examination123", database="project")

# con = c.connect(host='localhost', user='root',password='5824',database='project',port='5824')
st.set_page_config(page_title="DBMS Project",
                   page_icon=":maple_leaf:", layout="wide")

# To store feedback
# feedbackList = []
# hed=[]
# hed.append("name")
# hed.append("feedback")
# feedbackList.append(hed)

# list2=[]
# list1=[]
# user_id=0
# class feedback:
#     def __init__(self, name, text):
#         self.feedback_name = name
#         self.feedback_text = text

#     def add_feedback(self):
#         feedbackList.append(self)
#         return 1


if con.is_connected:
    print("Successfully connected")
cursor = con.cursor()
st.title("CABKARO.com")
feedbackList = []
hed = []
hed.append("name")
hed.append("feedback")
feedbackList.append(hed)

list2 = []
list1 = []
user_id = 0


def streamlit_menu(example=2):

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "about-us", "signup/login",
                     "Faqs", "contact-us"],  # required
            icons=["house", "book", "envelope", "file", "contact"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "000000"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=3)


# st.image()


st.sidebar.success("cabkaro.com")


if selected == "contact-us":
    st.markdown("## 123A mall road AP building Gurugram Haryana")
    st.image("ju.jpg")


if selected == "Home":

    st.markdown("<h1 style='text-align: center; color: orange;'>welcome to CABKARO</h1>",
                unsafe_allow_html=True)
    # st.markdown("## book a ride")
    with st.container():
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        # Use local CSS

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",
                            unsafe_allow_html=True)

        local_css("style/style.css")

        # ---- LOAD ASSETS ----
        lottie_coding = load_lottieurl(
            "https://assets3.lottiefiles.com/private_files/lf30_hsabbeks.json")
        lottie_coding_email = load_lottieurl(
            "https://assets2.lottiefiles.com/packages/lf20_5wr08scz.json")

        # ---- HEADER SECTION ----
        with st.container():
            title_container = st.container()
            col1, col2 = st.columns([1, 20])
            # image = Image.open('images\\CabHUB.png')

            st.markdown(
                "<h2 style='text-align: center; color: orange;'>Book a Taxi in your city</h2>", unsafe_allow_html=True)
            st.markdown(
                "<h6 style='text-align: center; color: white;'>choose from a range of categories and prices</h6>", unsafe_allow_html=True)

        # ---- WHAT I DO ----
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("Book a Ride")
                left_column.text_input("Pick up")
                left_column.text_input("Drop")
                option = st.selectbox(
                    'Car type', ('Mini', 'Prime Sedan', 'Auto', 'Prime Play', 'Prime Suv'))
                st.write('You selected:', option)
            with right_column:
                st_lottie(lottie_coding, height=600, key="coding")

        # ---- CONTACT ----
        with st.container():
            st.write("---")
            st.header("Get In Touch With Me!")
            st.write("##")

            # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
            contact_form = """
            <form action="https://formsubmit.co/debjit20504@iiitd.ac.in.COM" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st_lottie(lottie_coding_email, height=300, key="email")


if selected == "about-us":
    st.markdown("""
       ### Our Founders
       ##### Arjun Temura, BTech Computer Science and Biosciences, IIIT Delhi
       ##### Aman Kumar, BTech Computer Science and Biosciences, IIIT Delhi   
       ##### Mohd Zaid, BTech Computer Science and Biosciences, IIIT Delhi
       ##### Debjit Pramanik, BTech Computer Science and Biosciences, IIIT Delhi 
       #### We are a Taxi booking company who are working hard to bring to you the best cab experience you can ever imagine!  
       #### :pray: :pray: :pray: **TRUST IS EARNED**:pray: :pray: :pray:
       ##### We are rated as the 3rd best taxi booking company in India. We are the first choice of all Indians, be it going to your institute or on a trip.
       ##### All are drivers are well trained and have a valid driving licences issued by the Govt. of India
       ##### They all are vaccinated and cabs are sanitised after every trip. :smile: 
         
    """, True)
    st.header("Some Customer Feedback: ")
    col1, col2 = st.columns(2)

    col1.subheader("Aman Gupta")
    col1.image("boy.jpg")
    col1.markdown("""
       _I am so lucky to be a regular customer of CABKARO. All rides are pocket friendly and are on time.Highly recommended!_
       :star::star::star::star::star:
    """)
    col2.subheader("Shubhangi Srinivas")
    col2.image("girl.jpg")
    col2.markdown("""
      _As someone who works in the IT sector for late night shifts, cab booking can be a headache.
      CABKARO's drivers are available 24x7 at your call with top notch service_
      :star::star::star::star: 
    """)
    st.subheader("Add your feedback")
    feedback_name = st.text_input("Enter your name: ")
    feedback_text = st.text_input("Write about us: ")
    if st.button("submit"):
        query = "insert into feedback values ('{}','{}')".format(
            feedback_name, feedback_text)
        cur = con.cursor()
        cur.execute(query)
        con.commit()

    if st.button("View_feedbacks"):
        query = "select * from feedback"
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        st.dataframe(data)

    # if st.button("submit"):
    #     p = feedback(feedback_name, feedback_text)
    #     if(feedback.add_feedback(p)):
    #         st.success("Feedback submitted successfully!")
    #         # st.write(feedback)
    # if col2.button("View Other feedbacks"):
    #     st.write(feedbackList)


# user_id1 = list2[-1]
if selected == "signup/login":
    st.title("Signup/ Login Page")
    login = st.selectbox("How do you want to login?",
                         ["Signup as Customer", "Login as Customer"])
    if login == "Login as Customer":
        userid = st.number_input("UserID: ")
        passwd = st.text_input("Password: ", type="password")
        query = "select user_id,pass_wd,name from customer"
        cursor.execute(query)
        data = cursor.fetchall()
        # list1=[]   #list containing user_id's
        # list2=[]   #list containing passwd's
        for i in range(len(data)):
            list1.append(data[i][0])
            list2.append(data[i][1])
        # print(list1[499])
        # print(list2[499])

        # print(data)
        c1, c2 = st.columns([7, 1])
        if c2.button("Submit"):
            # print("user", userid)
            bol1 = (userid in list1)
            bol2 = (passwd in list2)
            # print(bol1,bol2)
            if (bol1) and (bol2):
                st.success("sucessfully logedin....")
                st.success("Now u can book a ride, GO to Home page!...!")
                st.sidebar.write("WELCOME:\n")
                st.sidebar.write(data[int(userid)-1][2])
            else:
                st.error("user-id or password may not be correct")

    if login == "Signup as Customer":

        query = "select user_id from customer"
        cursor.execute(query)
        data = cursor.fetchall()
        # print(len(data))
        user_id = len(data)+1
        # print(user_id)
        first, last = st.columns(2)
        user_name = first.text_input("Name")
        email = last.text_input("E-mail")
        passw, phno = st.columns([3, 1])
        passwd = passw.text_input("Password: ", type="password")
        number = phno.text_input("Phone number")

        c1, c2 = st.columns([7, 1])
        if c2.button("Submit"):
            st.success("You have been successfully registered")
            st.success("Now you can go to HomePage")
            query = "insert into customer(user_id,name,email,pass_wd, mobile) values({},'{}','{}','{}',{})".format(
                    user_id, user_name, email, passwd, number)
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            user_id += 1


if selected == "Faqs":
    st.write("why cabkaro?")
    st.write("when discounts alloted")
    st.write("why ride with us")
    st.write("women safety ensured")
    st.write("are the drivers")

    # most booked car
    # most busy time
    # ways of payments
    # different car types
    # price hikes at different times
    faq = st.radio("faq", ("most-booked-car", "most-busy-time",
                           "payment-ways", "diff-car-types"))

    if faq == "prices":
        query = "select car_type,avg(cost_km) from fares group by car_type order by car_type"
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        st.dataframe(data)
        st.write(data)

    if faq == "most-booked-car":

        query = "select car_type,((select count(*) from rides r where r.registration_no in(select registration_no from cars  l where l.car_type=a.car_type)))as most_booked from cars a group by car_type order by most_booked"
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        st.dataframe(data)

    if faq == "most-busy-time":
        query="""select  start, end, count(*) 
              from fares f,cars c 
              where exists(select * from rides r where r.registration_no=c.registration_no and r.time>f.start and r.time<f.end and c.car_type=f.car_type) 
              group by start, end order by count(*)"""
        cur = con.cursor()
        cur.execute(query)
        data=cur.fetchall()
        count=cur.rowcount
        for row in data:
            count-=1
            st.write("Interval Start Time: ", row[0], "Interval End Time:", row[1], "No of Rides booked: ", row[2])
            if count==0:
                st.write("Interval: ", row[0],"to", row[1],"is the busiest time")
    if faq == "payment-ways":
        query = "select payment_type from payment"
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        st.dataframe(data)

    if faq == "diff-car-types":
        st.success("here are the different car types that you can book")
        query = "select distinct car_type from cars"
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        st.dataframe(data)
        # st.write(data)
st.sidebar.image("rf.jpg", use_column_width=True)
