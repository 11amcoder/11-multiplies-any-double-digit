import streamlit as st

# Constant multiplier
constant = 11

# Input widget for user to enter a number
st.title("Multiply a Two-Digit Number by 11")
st.write("Enter a two-digit number, and the app will calculate the result.")

ui = st.text_input("Please enter a two-digit number:", "")  # Text input as a string

if st.button("Submit"):
    try:
        ui = int(ui)
        if ui > 99 or ui < 10:
            st.error("Wrong! Please enter a valid two-digit number.")
        else:
            # Existing Code
            list1 = list(str(ui))
            breakthroughnumber = int(list1[0]) + int(list1[1])
            list1.append(breakthroughnumber)
            list1 = [int(x) for x in list1]

            last_element = list1.pop()
            middleplacing = len(list1) // 2
            list1.insert(middleplacing, last_element)

            individualnos = []
            for item in list1:
                individualnos.extend(int(x) for x in str(item))

            def placenos(individualnos):
                list2 = int(individualnos[0]) + int(individualnos[1])
                list2 = list(str(list2))
                list2.extend(individualnos[-2:])
                numb = int("".join(map(str, list2)))
                return numb

            result = placenos(individualnos)
            st.success(f"Multiplying {ui} with {constant}, the result is: {result}")
    except ValueError:
        st.error("Invalid input! Please enter a valid number.")
