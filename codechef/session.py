# WARNING
# this script assumes everything to go well and doesn't check
# username pass are correct, connection yet
# TODO fix error checking soon

import requests
from bs4 import BeautifulSoup
import getpass
import pprint
import time

url="https://www.codechef.com/"
codechef_session=requests.session()
verbose=True

def if_verbose_print(*args, **kwargs):
    if 'verbose' in globals() and verbose == True:
        print(*args, **kwargs)

# this function is significantly general for filling forms try to make it more general
# use the value attribute of forms
def login():
    login_url=url
    global codechef_session
    login_page=codechef_session.get(login_url)
    if_verbose_print("got the login page")
    form_feilds=BeautifulSoup(login_page.text,"html.parser").findAll("input")
    form_data={}

    for i in form_feilds:
        attrs=i.attrs
        print(i)
        if "name" in attrs:
            if "value" in attrs and attrs["value"]:
                form_data[attrs["name"]]=attrs["value"]
            else:
                if "type" in attrs:
                    if_verbose_print("Field type:",str(attrs["type"]).lower())
                    if str(attrs["type"]).lower() == "password":
                        form_data[attrs["name"]]=getpass.getpass("Enter "+ attrs["placeholder"] +": ")

                if attrs["name"] not in form_data:
                    form_data[attrs["name"]]=input("Enter " + attrs["placeholder"] +": ")

    if_verbose_print("The following is the form data that will be sent:\n",\
                     pprint.pformat(form_data,indent=2))
    print("logging you into codechef... please wait...")
    logged_page=codechef_session.post(login_url,form_data)
    title = BeautifulSoup(logged_page.text,"html.parser").head.title.text
    if_verbose_print("title: ",title)

    
    # logout all other sessions as codechef doesn't allows multiple sessions
    while "session/limit" in logged_page.url:
        print("sle")
        logout_other_session()
        logged_page=codechef_session.post(url,form_data)

    # codechef doesn't check cookies and trivially displays the latest as current session
    # handle this using modifying logout_other_session by logging out after checking session cookies
    # and matching with form data. trivially the following solution works

    logged_page=codechef_session.post(url,form_data)
    if len(BeautifulSoup(logged_page.text,"html.parser").findAll("input"))> 0:
        print("you are/have tried to login to codechef while the script was running\n should i try to login again(Y/N)")
        if input()=="Y":
            login()
        else:
            print("You chose not to login")
    else:
        print("logged in to codechef")


def logout_other_session():
    global codechef_session
    sess_url=url+"session/limit"
    session_page=codechef_session.get(sess_url)
    if_verbose_print("got the session page")
    form_feilds=BeautifulSoup(session_page.text,"html.parser").findAll("input")
    form_data={}
    for j in [0,-1,-2,-3,-4]:
        i=form_feilds[j]
        attrs=i.attrs
        if "name" in attrs:
            if "value" in attrs and attrs["value"]:
                form_data[attrs["name"]]=attrs["value"]
            else:
                print(attrs)

    if_verbose_print(form_data)
    a=codechef_session.post(sess_url,data=form_data)
    title=BeautifulSoup(a.text,"html.parser").head.title.text
    if_verbose_print(title)
    
def logout():
	global codechef_session
	logout_url=url+"/logout"
	a=codechef_session.get(logout_url)
	print("you are logged out")