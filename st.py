import streamlit as st

# Constant multiplier
constant = 11

st.title("Multiply a Two-Digit Number by 11")
st.write("Enter a two-digit number, and this app will multiply it by 11.")

# Input Section: Restricted to two-digit numbers
ui = st.number_input(
    "Enter a two-digit number:", 
    min_value=10, 
    max_value=99, 
    step=1, 
    format="%d"
)

# Button to trigger the computation
if st.button("Calculate"):
    # Convert the input into a list
    list1 = list(str(int(ui)))
    breakthroughnumber = int(list1[0]) + int(list1[1])  # Add the two digits
    list1.append(breakthroughnumber)  # Add the sum to the list

    # Convert all elements to integers
    list1 = [int(x) for x in list1]

    # Rearrange the list
    last_element = list1.pop()  # Extract the last element
    middleplacing = len(list1) // 2  # Find the middle position
    list1.insert(middleplacing, last_element)  # Insert the last element in the middle

    # Break down to atomic-level numbers
    individualnos = []
    for item in list1:
        individualnos.extend(int(x) for x in str(item))

    # Function to finalize the result
    def placenos(individualnos):
        list2 = int(individualnos[0]) + int(individualnos[1])  # Add first two elements
        list2 = list(str(list2))  # Convert the sum to a list of digits
        list2.extend(individualnos[-2:])  # Add the last two digits
        numb = int("".join(map(str, list2)))  # Join and convert to integer
        return numb

    # Perform multiplication
    result = placenos(individualnos)

    st.write(f"Multiplying {ui} with {constant}:")
    st.success(f"Result: {result}")
