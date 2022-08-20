from typing import Dict, Any
import datetime as dt
import streamlit as st
import pandas as pd
import pickle

from st_aggrid import AgGrid
from data_fxs import *
import json
from streamlit_timeline import timeline
import datetime
from st_aggrid.shared import JsCode
myjson={
    "title": {

        "text": {
          "headline": "My Shaadi",
          "text": "<p>A Streamlit Timeline component by integrating TimelineJS from Knightlab</p>"
        }
    },
    "events": [
      {
        "start_date": {
            "month":"8",
          "day": "4",
          "hour":"10"
        },
        "text": {
          "headline": "Haldi",
          "text": "<p>TimelineJS is a populair tool from Knightlab. It has been used by more than 250,000 people to tell stories seen hundreds of millions of times, and is available in more than sixty languages. </p>"
        }
      },
      {

        "start_date": {
          "month":"8",
          "day": "4",
          "hour":"15"
        },
        "text": {
          "headline": "Bhaat",
          "text": "Streamlit lets you turn data scripts into sharable web apps in minutes, not weeks. It's all Python, open-source, and free! And once you've created an app you can use our free sharing platform to deploy, manage, and share your app with the world."
        }
      },
        {

            "start_date": {
                "month": "8",
                "day": "5",
                "hour": "10"
            },
            "text": {
                "headline": "Sangeet",
                "text": "Streamlit lets you turn data scripts into sharable web apps in minutes, not weeks. It's all Python, open-source, and free! And once you've created an app you can use our free sharing platform to deploy, manage, and share your app with the world."
            }
        },
        {

            "start_date": {
                "month": "8",
                "day": "5",
                "hour": "20"
            },
            "text": {
                "headline": "Shaadi",
                "text": "Streamlit lets you turn data scripts into sharable web apps in minutes, not weeks. It's all Python, open-source, and free! And once you've created an app you can use our free sharing platform to deploy, manage, and share your app with the world."
            }
        }

    ]
}


def add_function():
    name = st.text_input("name", key=1)
    ddate = st.date_input("Function Date")

    g1, g2 = st.columns(2)
    g1.write("Main contacts for function")
    main_ppl_add = g2.checkbox("add People", key=1)
    if main_ppl_add:
        n1 = g2.text_input("name", key=11)
        n2 = g2.text_input("contact", key=12)
        n3 = g2.button("done", key=2)
        if n3:
            get_data("Name").append(n1)
            get_data("Contact").append(n2)
            st.success("people added:" + n1)

    Main_ppl = {"name": get_data("Name"), "Contact": get_data("Contact")}
    myrequest={}
    f1, f2 = st.columns(2)
    f1.write("Requirements for function")
    req_add = f2.checkbox("add req", key=34)
    if req_add:
        ff1 = f2.text_input("item", key=31)

        ff2 = f2.number_input("quantity")
        ff3 = f2.text_input("Units", key=32)
        ff4 = f2.text_input("Agg_item", key=33)
        ff5 = f2.button("done", key=35)
        if ff5:
            myrequest = {"item": ff1, "quantity": ff2, "Units": ff3, "agg_item": ff4}
            st.success("Requirements added:" + ff1)

        # st.write(json.dumps(req))
    ret_gift={}
    p1, p2 = st.columns(2)
    p1.write("return gifts for function")
    ret_add = p2.checkbox("add return gift")
    if ret_add:
        pp1 = p2.text_input("Name", key=41)
        pp2 = p2.text_input("Contact", key=43)
        pp3 = p2.text_input("Return Gift", key=42)
        pp4 = p2.button("add Gift", 0)
        ret_gift = {"name": pp1, "contact": pp2, "return gift": []}
        if pp4:
            get_data("return gift").append(pp3)
            st.success("Gift added:" + pp3)

        pp5 = p2.button("done")
        if pp5:
            ret_gift["return gift"] = str(get_data("return gift"))
    comms=""
    comments = st.text_area("enter comments")
    aa = st.button("Save comments")
    if aa:
        comms=comments

    u1, u2 = st.columns(2)
    u1.header("Events")
    u = u2.checkbox("Add", key=999)
    events={}
    if u:
        Name = u2.text_input("Event", key=111)
        Date = u2.date_input("Date of Event", key=122)
        Time_event = u2.time_input("Time of Event", key=133)
        save_events=u2.button("Add Event", key=144)
        if save_events:
            try:
                events['Event'].append(Name)
                events['Date'].append(Date)
                events['Time'].append(Time_event)
            except:
                events={'Event':[Name],'Date':[Date],'Time':[Time_event]}
            st.success("Event added:" + Name)


    k=[name,ddate,json.dumps(Main_ppl),json.dumps(myrequest),json.dumps(ret_gift),comms,json.dumps(events,default=convert_timestamp)]
    gg=st.button("Done",key=178)
    if gg:
        add_data(1, k)

def add_guest():
    name = st.text_input("Name", 0)
    category = st.selectbox("Category", ["Senior", "Cousin", "Child", "Friend"])
    Family = st.number_input("Family No.", 0, 1000, step=1)
    E_arrival_d=st.date_input("Arrival Date")
    E_arrival_t = st.time_input("Arrival Time")
    E_dep_d=st.date_input("Departure Date")
    E_dep_t = st.time_input("Departure Time")
    g1, g2 = st.columns(2)
    gift_add = g2.checkbox("Add Gifts", 0)
    if gift_add:
        Gift = g1.text_input("Gift")
        gh = g1.button("Done")
        if gh:
            g1.write(gh)
            get_data("mygifts").append(Gift)
            st.success("Gift added:" + Gift)

    confirmed = st.selectbox("Confirmed", ["Yes", "No"])
    contact_no = st.text_input("Contact", 1)
    done_guest = st.button("Done", 1)
    if done_guest:
        add_data(0, [name, category, Family, str((E_arrival_t,E_arrival_d)), str((E_dep_t,E_dep_d)), str(get_data("mygifts")), confirmed, contact_no])
        st.success("{} added in Guests".format(name))
def display_guest(guest,data):

    st.title(guest)
    guest_data=[]
    for i in data:
        if i[0]==guest:
            guest_data=i
    print(guest_data[5])
    a1,a2=st.columns(2)
    a1.subheader("category")
    a2.write(guest_data[1])
    b1,b2=st.columns(2)
    b1.subheader("Family Number")
    b2.write(guest_data[2])
    c1,c2=st.columns(2)
    c1.subheader("Arrival")
    c2.write(guest_data[3])
    d1, d2 = st.columns(2)
    d1.subheader("Departure")
    d2.write(guest_data[4])
    gifts = AgGrid(pd.DataFrame(eval(guest_data[5]),columns=["Gifts"]), editable=False, fit_columns_on_grid_load=True)
    e1, e2 = st.columns(2)
    e1.subheader("Confirmed")
    e2.write(guest_data[6])
    f1, f2 = st.columns(2)
    f1.subheader("Contact")
    f2.write(guest_data[7])

def display_Function(function,data):
    st.title(function)
    function_data=[]
    for i in data:
        if i[0]==function:
            function_data=i

    st.date_input("Date",dt.datetime.strptime(function_data[1],'%Y-%m-%d').date())

    st.subheader("Main People")
    main_ppl = AgGrid(pd.DataFrame.from_dict(eval(function_data[2])), editable=False, fit_columns_on_grid_load=True)
    st.subheader("Requirements")
    requi = AgGrid(pd.DataFrame.from_dict(eval(function_data[3])), editable=False, fit_columns_on_grid_load=True,key=1)
    st.subheader("Return Gifts")
    requi2 = AgGrid(pd.DataFrame.from_dict(eval(function_data[4])), editable=False, fit_columns_on_grid_load=True)
    print(requi)
    st.subheader("Comments")
    comments=st.write(function_data[5])
    timeline(myjson, height=800)
def convert_timestamp(item_date_object):
    if isinstance(item_date_object, (datetime.date, datetime.datetime)):
        return item_date_object.timestamp()
def edit_guest(guest,data):

    guest_data=[]
    for i in data:
        if i[0]==guest:
            guest_data=i
    name = st.text_input("Name",guest)
    category_options=["Senior", "Cousin", "Child", "Friend"]
    category = st.selectbox("Category",category_options ,category_options.index(guest_data[1]))
    Family = st.number_input("Family No.", 0, 1000, step=1,value=guest_data[2])
    arv1,arv2=st.columns(2)
    dep1,dep2=st.columns(2)
    E_arrival_d = arv1.date_input("Arrival Date")
    E_arrival_t = arv2.time_input("Arrival Time")
    E_dep_d = dep1.date_input("Departure Date")
    E_dep_t = dep2.time_input("Departure Time")
    print((guest_data[5]))
    print("*********************************************************")
    gifts = AgGrid(eval(guest_data[5])['data'], editable=True, fit_columns_on_grid_load=True,reload_data=True)
    g1, g2 = st.columns(2)
    gift_add = g2.checkbox("Add Gifts", 0)
    if gift_add:
        Gift = g1.text_input("Gift")
        gh = g1.button("Done")
        if gh:
            g1.write(gh)
            get_data("gifts").append(Gift)
            update_guest_gift(Gift,guest)
            st.success("Gift added:" + Gift)
            st.success(get_data("gifts"))
    else:
        g2.button("Save Changes",on_click=update_guest_gift_all(gifts,guest))
    confirmed = st.selectbox("Confirmed", ["Yes", "No"])
    contact_no = st.text_input("Contact", 1)
    done_guest = st.button("Done", 1)
    if done_guest:
        add_data(0, [name, category, Family,  str((E_arrival_t,E_arrival_d)), str(E_dep_t,E_dep_d), str(get_data("gifts")), confirmed, contact_no])

def edit_function(function,data):
    st.title(function)
    function_data = []
    for i in data:
        if i[0] == function:
            function_data = i

    st.date_input("Date", dt.datetime.strptime(function_data[1], '%Y-%m-%d').date())
    x1, x2 = st.columns(2)
    x1.header("Main_ppl")
    x = x2.checkbox("Add")
    main_ppl = AgGrid(pd.DataFrame.from_dict(eval(function_data[2])), editable=True, fit_columns_on_grid_load=True,reload_data=True)
    print("type:", type(main_ppl), dt.datetime.now())
    if x:
        add_name = x2.text_input("name")
        add_contact = x2.text_input("contact")
        x2.button("Done", on_click=update_main_ppl, args=((add_name, add_contact), function,0))
    else:
        print(type(main_ppl))
        x2.button("Save Changes",on_click=update_main_ppl(main_ppl,function,1),key=67)
    z1, z2 = st.columns(2)
    z1.header("Requirements")
    z = z2.checkbox("Add", 2)
    requi = AgGrid(pd.DataFrame.from_dict(eval(function_data[3])), editable=True, fit_columns_on_grid_load=True, key=1,
                   reload_data=True)
    if z:
        item = z2.text_input("Item", 1)
        Quantity = z2.text_input("Quantity")
        Units = z2.text_input("Units", 2)
        Agg = z2.text_input("Agg", 3)
        z2.button("Done", on_click=update_req, args=((item, Quantity, Units, Agg), function,0), key=3)
    else:
        z2.button("Save Changes", on_click=update_req(requi, function, 1),key=89)


    y1, y2 = st.columns(2)
    y1.header("Return Gifts")
    y = y2.checkbox("Add", key=99)
    requi3 = AgGrid(pd.DataFrame.from_dict(eval(function_data[4])), editable=True, fit_columns_on_grid_load=True,
                    reload_data=True)
    if y:
        Name = y2.text_input("Name", key=11)
        Contact = y2.text_input("Contact", key=12)
        Return_Gift = y2.text_input("Return Gift", key=13)

        y2.button("Done", on_click=update_ret_gift,args=((Name, Contact, Return_Gift), function,0,), key=14)
    else:
        y2.button("Save Changes", on_click=update_ret_gift(requi3, function, 1),key=45)

    st.subheader("Comments")
    comments = st.text_area(function_data[5])

    aa = st.button("Save comments", on_click=update_comments(comments, function))
    if aa:
        update_comments(comments, function)

    u1, u2 = st.columns(2)
    u1.header("Events")
    u = u2.checkbox("Add", key=999)
    requi4 = AgGrid(pd.DataFrame.from_dict(eval(function_data[6])), editable=True, fit_columns_on_grid_load=True,
                    reload_data=True)
    if u:
        Name = u2.text_input("Event", key=111)
        Date = u2.date_input("Date of Event", key=122)
        Time_event = u2.time_input("Time of Event", key=133)
        u2.button("Done", on_click=update_events, args=(( Name, Date,Time_event), function,0,), key=144)
    else:
        u2.button("Save Changes", on_click=update_events(requi4, function, 1),key=122)
    timeline(myjson, height=800)

def main_page():
    All_Guests = view_all_data("Guests")
    All_Functions = view_all_data("Functions")
    b=""
    a=st.sidebar.selectbox("Select one",["Guest","Functions"],key=0)

    print(All_Guests)
    if a=="Guest":
        b = st.sidebar.selectbox("What would you like to do?", ["Add", "View", "Edit"],0)
        if len(All_Guests)>0:
            c=st.sidebar.selectbox("Select Guests",[i[0] for i in All_Guests])
        else:
            c = st.sidebar.selectbox("Select Guests", [i[0] for i in All_Guests],disabled=True)
        if b=="Add":
            add_guest()
        if b=="View":
            display_guest(c,All_Guests)

        if b=="Edit":
            edit_guest(c,All_Guests)

    if a=="Functions":
        b = st.sidebar.selectbox("What would you like to do?", ["Add", "View", "Edit"],1)
        if len(All_Functions)>0:
            c=st.sidebar.selectbox("Select Functions",[i[0] for i in All_Functions])
        else:
            c = st.sidebar.selectbox("Select Functions", [i[0] for i in All_Functions],disabled=True)

        if b == "Add":
            add_function()
        if b == "View":
            display_Function(c, All_Functions)
        if b == "Edit":
            edit_function(c, All_Functions)

@st.cache(allow_output_mutation=True)
def get_data(url):
    return []

if __name__=="__main__":
    st.clear_cache()
    create_table()
    main_page()
