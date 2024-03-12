# Libraries used: streamlit (custom webpage library),
# functions (custom text file library made by me)
# time (python built-in library used to display the current date)
import streamlit as st
import functions
import time

todos = functions.read_files() # The list of to-do's
current_date = time.strftime("%b %d, %Y")

def add_todo():
    """
    Function Description: Adds a new to-do when we enter a to-do inside text input.
    Error: Empty string added to the list of to-do's.
        If condition statement - error fixed; if user clicked out of text box with nothing in it
        an empty to-do will automatically add itself. The condition checks if the session state is
        not empty and if so then it will perform add_todo function

    :return: None; performs a write_files() function by overwritting the old todos with
    the new added to-do + the old to-do's
    """
    if st.session_state["todo_input"] != "":

        new_todo = st.session_state["todo_input"] + "\n"
        todos.append(new_todo)
        functions.write_files(todos)

def remove_todos(item):
    """
    Function description: Gets called when a checkbox has been checked, which will then delete
    the to-do
    :param item: The checkboxed item that is to be removed
    :return: None; performs operations of list removal and file re-write to update todos in todos.txt
    also will rerun the program automatically as well as delete the item from our session state.
    """
    todos.remove(item)
    functions.write_files(todos)
    del st.session_state[item]
    st.experimental_rerun()

st.title("To-Do App") # Webpage Title
st.subheader("Welcome to your personal To-Do App!") # Webpage subheader
st.subheader("Date: {}"
             .format(current_date))
st.write("A message from the owner: \"A to-do app is a great tool to increase your productivity. Use it wisely!\"")  # Webpage text

# HashMap which will hold all my to-do's as keys and their current state
checkbox_states_todos = {}

for item in todos:
    checkbox_states_todos[item] = st.checkbox(item,
                                              key=item)

for item, state in checkbox_states_todos.items():
    # Item - key(our to-do);
    # State - value(True or False; checked or unchecked)
    if state:  # If a checkbox was checked
        remove_todos(item)


# Input box for adding new to-do's;
st.text_input(label="Add your new to-do inside of this text box!",
              placeholder="Add a new to-do here...",
              max_chars=250,
              key="todo_input",
              on_change=add_todo)


