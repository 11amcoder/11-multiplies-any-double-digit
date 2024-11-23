import streamlit as st

# App title
st.title("Multiply a Two-Digit Number by 11")

# Input section
st.write("Enter a two-digit number to see its multiplication by 11:")

ui = st.number_input("Two-digit number:", min_value=10, max_value=99, step=1, format="%d")

# Convert the input into a list
list1 = list(str(ui))
breakthroughnumber = int(list1[0]) + int(list1[1])  # Adding elements of list and making them numbers
list1.append(breakthroughnumber)  # Add the sum to the list
list1 = [int(x) for x in list1]  # Convert all strings in the list to integers

# Rearrange the list
last_element = list1.pop()
middleplacing = len(list1) // 2
list1.insert(middleplacing, last_element)

# Separate into atomic elements
individualnos = []
for item in list1:
    individualnos.extend(int(x) for x in str(item))

def placenos(individualnos):
    list2 = int(individualnos[0]) + int(individualnos[1])  # Add the first 2 elements
    list2 = list(str(list2))  # Convert the result to a list
    list2.extend(individualnos[-2:])  # Add the last two elements
    numb = int("".join(map(str, list2)))  # Convert the list to an integer
    return numb

# Display result
if len(individualnos) <= 3:
    result = int("".join(map(str, individualnos)))
    st.success(f"Result: {result}")
else:
    st.success(f"Multiplying {ui} by 11 gives: {placenos(individualnos)}")












