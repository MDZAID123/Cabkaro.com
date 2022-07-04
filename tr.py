from turtle import distance
from streamlit_option_menu import option_menu
import hydralit_components as hc
import streamlit as st
import time as tt
import mysql.connector as c
import pandas as pd
import requests
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

from streamlit_lottie import st_lottie
from PIL import Image
from random import randint

user_idf=0
con=c.connect(host="localhost", user="root", passwd="examination123", database="project")
#con = c.connect(host="localhost", user="root",
#                passwd="examination123", database="project")

# con = c.connect(host='localhost', user='root',password='5824',database='project',port='5824')
st.set_page_config(page_title="DBMS Project", page_icon=":maple_leaf:", layout="wide")

# To store feedback
feedbackList=[]


list2=[]
list1=[]
user_id=0
# class feedback:
#     def __init__(self, name, text):
#         self.feedback_name = name
#         self.feedback_text = text

#     def add_feedback(self):
#         feedbackList.append(self)
#         return 1


if con.is_connected:
    print("Successfully connected")
cursor = con.cursor(buffered=True)
st.title("CABKARO.com")


def streamlit_menu(example=2):

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "about-us","signup/login","Faqs","contact-us"],  # required
            icons=["house", "book", "envelope", "file","contact"],  # optional
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

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_hsabbeks.json")
lottie_coding_email = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5wr08scz.json")
lottie_sidebar = load_lottieurl("https://assets9.lottiefiles.com/datafiles/akoBQNZ4VfYIciL/data.json")

lottie_facebook = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_xwabp3dh.json")
lottie_twiter = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5mhyg2hz.json")
lottie_insta = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_86afyky0.json")
lottie_you = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ej2lfhv2.json")



if selected =="contact-us":
    st.markdown("## 123A mall road AP building Gurugram Haryana")
    with st.container():
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")
        with st.container():
            st.write("---")
            st.header("Get In Touch With Us!")
            st.write("##")

           # Documention: https://formsubmit.co/debjit20504@iiitd.ac.in
            contact_form = """
            <form action="https://formsubmit.co/ac8aef252eaa135532159bd4950bfa61" method="POST">
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
    with st.container():
        face_col, twiter_col, insta_col, you_col = st.columns(4)
        with face_col:
            st_lottie(lottie_facebook, height=100, key="lottie_facebook")
        with twiter_col:
            st_lottie(lottie_twiter, height=100, key="lottie_twiter")
        with insta_col:
            st_lottie(lottie_insta, height=100, key="lottie_insta")
        with you_col:
            st_lottie(lottie_you, height=100, key="lottie_you")





if  selected == "Home":

    st.markdown("<h1 style='text-align: center; color: orange;'>welcome to CABKARO</h1>", unsafe_allow_html=True)
    query = "select booking_id,pickup,destination from booking"
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data)
    bok = []
    pick = []
    dest = []
    for i in range(len(data)):
        bok.append(data[i][0])
        pick.append(data[i][1])
        dest.append(data[i][2])

    old_bookingid = -1
    new_bookingid = bok[-1] + 1
    e_name = ""
    e_ph = 0
    e_id = 0

    # st.markdown("## book a ride")
    with st.container():
        # Use local CSS
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")

        # ---- HEADER SECTION ----
        with st.container():
            title_container = st.container()
            col1, col2 = st.columns([1, 20])
            # image = Image.open('images\\CabHUB.png')

            st.markdown("<h2 style='text-align: center; color: orange;'>Book a Taxi in your city</h2>",
                        unsafe_allow_html=True)
            st.markdown(
                "<h6 style='text-align: center; color: white;'>choose from a range of categories and prices</h6>",
                unsafe_allow_html=True)

        # ---- WHAT I DO ----
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("Book a Ride")
                pick_up = left_column.text_input("Pick up")
                drop = left_column.text_input("Drop")
                option = st.radio("car type", ("mini", "auto", "prime sedan", "prime play", "prime suv"))

                if pick_up in pick and drop in dest:
                    for i in range(len(pick)):
                        if pick_up == pick[i] and drop == dest[i]:
                            old_bookingid = bok[i]
                            print("old_bookingid", old_bookingid)
                            print("new_bookingid", new_bookingid)
                            break

                if st.button("Select a ride"):

                    
                    query = "select * from rough"
                    cur = con.cursor()
                    cur.execute(query)
                    data = cur.fetchall()
                    # for i in range(len(data)):
                    rt = data[-1][0]
                    print("rt",rt)

                    query = "insert into booking(user_id,booking_id,current_location,pickup,destination) values({},{},'{}','{}','{}')".format(
                        rt, new_bookingid, pick_up, pick_up, drop)
                    cur = con.cursor()
                    cur.execute(query)
                    con.commit()
                    # fetching distance btw pickup and drop
                    distance1 = -1
                    time = '00:00:00'
                    query1 = "select distance from distance where booking_id={}".format(old_bookingid)
                    cur = con.cursor()
                    cur.execute(query1)
                    data1 = cur.fetchall()
                    print("data",data1)
                    for i in range(len(data1)):
                        distance1 = int(data1[i][0])

                    query3 = "select current_time"
                    cur = con.cursor()
                    cur.execute(query3)
                    data3 = cur.fetchall()
                    for row in data3:
                        time = row[0]

                    cost = []
                    cost1 = [1, 2, 3, 4]
                    # auto, mini , primeplay ,prime sedan, prime suv
                    query2 = "select cost_km from fares where start<='{}' and end>='{}'".format(time, time)
                    cur = con.cursor()
                    cur.execute(query2)
                    data2 = cur.fetchall()
                    for i in range(len(data2)):
                        cost.append(data2[i][0])

                    print(cost)
                    # option = st.selectbox("Car type", [
                    # "Mini Rs.{}".format(cost[0] * distance1), "Prime Sedan Rs.{}".format(cost[1] * distance1),
                    # "Auto  Rs.{}".format(cost[2] * distance1), "Prime Play Rs.{} ".format(cost[3] * distance1),
                    # "Prime Suv Rs.{}".format(cost[4] * distance1)])

                    # option = st.selectbox("Car type", [
                    #     "Mini", "Prime Sedan",
                    #     "Auto", "Prime Play",
                    #     "Prime Suv"])


                    # login = st.selectbox("How do you want to login?",
                    #
                    #                      ["Signup as Customer", "Login as Customer", "Signin_as_administrator"])
                    # fetching employee id name phone no.
                    
                    query4 = "select e_id,first_name,last_name,phone_no from employees where availability=1"
                    cur = con.cursor()
                    cur.execute(query4)
                    data4 = cur.fetchone()
                    print(data4[0])
                    print(data4[1])
                    print(data4[2])
                    print(data4[3])
                    e_name = e_name + data4[1]
                    e_name = e_name + " " + data4[2]
                    e_id = data4[0]
                    e_ph = data4[3]
                    store_price=0 
                    # st.success("successfully booked")
                    if option == "mini":
                        st.success('You selected: Mini')
                        st.write(distance1*cost[1])
                        store_price=distance1*cost[1]
                    if option == "prime sedan":
                        st.success('You selected: Prime Sedan')
                        st.write(distance1*cost[3])
                        store_price=distance1*cost[3]
                    if option == "auto":
                        st.success('You selected: Auto')
                        st.write(distance1*cost[0])
                        store_price=distance1*cost[0]
                    if option =="prime suv":
                        st.success("You selected Prime SUV")
                        st.write(distance1*cost[4])
                        store_price=distance1*cost[4]
                    if option=="prime play":
                        st.success("You selected Prime Play")
                        st.write(distance1*cost[2]) 
                        store_price=distance1*cost[2]

                
                    progress=st.progress(0)
                    for i in range(100):
                            tt.sleep(0.0001)
                            progress.progress(i+1)
                    st.success("Successfully found your driver")
                        
                    st.write("Employee ID: ",e_id)
                    st.write("Name: ",e_name)
                    st.write("Phone no: ",e_ph)
                    st.write("Contact the driver for further details")
                    st.write(option)    


                    query="select registration_no from cars where car_type='{}'".format(option)
                    
                    # cur.execute(query)
                    # dataa = cur.fetchall()
                    # for row in dataa:
                    #     print(row[0])
                    #     st.write("Registration no. of car", row[0])
                    #     break



                    queryrid="insert into rides(booking_id,registration_no,e_id) values ({}, {}, {})".format(new_bookingid, "DL3450", e_id)
                    
                    # cur.execute(queryrid)
                    # con.commit()

                    queryrid="insert into distance(total_price,booking_id,distance) values ({}, {}, {})".format(store_price,new_bookingid, distance1)
                    
                    # cur.execute(queryrid)
                    # con.commit()


                    
                    # query12 = "delete from rough"
                    # cur = con.cursor()
                    # cur.execute(query12)
                    # con.commit()

            with right_column:
                st_lottie(lottie_coding, height=600, key="coding")
    


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
    col1.image("boy.jpg", width=200)
    col1.markdown("""
       _I am so lucky to be a regular customer of CABKARO. All rides are pocket friendly and are on time.Highly recommended!_
       :star::star::star::star::star:
    """)
    col2.subheader("Shubhangi Srinivas")
    col2.image("girl.jpg", width=200)
    col2.markdown("""
      _As someone who works in the IT sector for late night shifts, cab booking can be a headache.
      CABKARO's drivers are available 24x7 at your call with top notch service_
      :star::star::star::star: 
    """)
    st.subheader("Add your feedback")
    feedback_name = st.text_input("Enter your name: ")
    feedback_text = st.text_area("Write about us: ")
    
    if st.button("submit"):
        query="insert into feedback values('{}','{}')".format(feedback_name, feedback_text)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        st.success("Feedback submitted successfully!")
        

    if st.button("View Other feedbacks"):
            query="select name as \"Name\", feedback as \"Feedback\"  from feedback"
            cur=con.cursor()
            cur.execute(query)
            data=cur.fetchall()
            for row in data: 
                st.write("Name: ", row[0])
                st.write("Feedback: ", row[1])
                st.write("=========================================")
            
    


# user_id1 = list2[-1]
if  selected == "signup/login":
    
    st.title("Signup/ Login Page")
    login = st.selectbox("How do you want to login?",
    
                         ["Signup as Customer", "Login as Customer","Signin_as_administrator"])

    if login == "Signin_as_administrator":
        # reconnect
        if con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection is closed")

        con = c.connect(host="localhost", user="boss",
                        passwd="aman", database="mideval")
        if con.is_connected():
            print("successfully connected as admin")
            st.success("welcome admin")

            choice = st.radio("see data",
                              ('rides', 'employee', 'booking', 'payment', 'fares', 'distance',
                               'customers', 'luxury_cars', 'cars'))

            if choice == 'rides':
                query = "select * from rides"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df


                
                
                # AgGrid(df)

            if choice=='employee':
                query = "select * from employees"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)                


            if choice == 'booking':
                query = "select * from booking"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)

            if choice =='payment':
                query = "select * from payment"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)

            if choice == 'fares':
                query = "select * from fares"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)

            if choice == 'distance':
                query = "select * from distance"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)

            if choice == 'customers':
                query = "select * from customer"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)

            if choice == 'luxury_cars':
                query = "select * from luxury_cars"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)

            if choice == 'cars':
                query = "select * from cars"
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                data=pd.read_sql(query,con);
                gb = GridOptionsBuilder.from_dataframe(data)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                grid_response = AgGrid(
                    data,
                    gridOptions=gridOptions,
                    data_return_mode='AS_INPUT', 
                    update_mode='MODEL_CHANGED', 
                    fit_columns_on_grid_load=False,
                    theme='blue', #Add theme color to the table
                    enable_enterprise_modules=True,
                    height=350, 
                    width='100%',
                    reload_data=True
                        )

                data = grid_response['data']
                selected = grid_response['selected_rows'] 
                df = pd.DataFrame(selected)
    if login == "Login as Customer":
        
        userid=st.number_input("UserID: ")
        
        user_idf=userid
        query="insert into rough values ({})".format(user_idf)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        #print(user_idf)
        passwd=st.text_input("Password: ", type="password")
        query="select user_id,pass_wd,name from customer"
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
        user_id=len(data)+1
        user_idf=user_id
        query="insert into rough values ({})".format(user_idf)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        
        first, last = st.columns(2)
        user_name=first.text_input("Name")
        email=last.text_input("E-mail")
        passw, phno = st.columns([3, 1])
        passwd=passw.text_input("Password: ", type="password")
        number=phno.text_input("Phone number")

        c1, c2 = st.columns([7, 1])
        if c2.button("Submit"):
            st.success("You have been successfully registered")
            st.success("Now you can go to HomePage")
            query = "insert into customer(user_id,name,email,pass_wd, mobile) values({},'{}','{}','{}',{})".format(
		    user_id,user_name,email, passwd, number)
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            user_id+=1

    
    

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
    
    if faq=="prices":
        query="select car_type,avg(cost_km) from fares group by car_type order by car_type"
        cur=con.cursor()
        cur.execute(query)
        data=cur.fetchall()
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
with st.sidebar:
    st_lottie(lottie_sidebar, height=300, key="lottie_sidebar")

