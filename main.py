import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)

todos = functions.get_todos()


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This is for your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add new todo",placeholder="Add new todo...",
              on_change=add_todo,key="new_todo")
print("Hello")
