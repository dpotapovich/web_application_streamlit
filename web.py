import streamlit as st
import functions

todos = functions.get_mylist()


def add_todo():
    new_todo = st.session_state["new_todo"]+"\n"
    todos.append(new_todo)
    functions.write_mylist(todos)


st.title("My Todo App")

st.write("This App increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_mylist(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo..", on_change=add_todo, key="new_todo")

