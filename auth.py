import streamlit as st

def create_user_data(username, password):
    user_data = {
        "username": username,
        "password": password
    }
    return user_data

def authenticate(username, password, user_data):
    if username in user_data.keys():
        if password == user_data[username]["password"]:
            return True
        else:
            return False
    else:
        return False