import streamlit as st

st.write("""
# Largest of 3 Given Numbers
""")

st.header('Enter 3 Numbers')

num_1 = st.number_input("1st Number",step=1)
num_2 = st.number_input("2nd Number",step=1)
num_3 = st.number_input("3rd Number",step=1)

st.subheader('Entered Numbers are -')
st.write([num_1, num_2, num_3])

max = None

if (num_1 > num_2) and (num_1 > num_3):
  max = num_1
elif (num_2 > num_1) and (num_2 > num_3):
  max = num_2
else:
  max = num_3

st.write("""
## Largest of the given 3 numbers is -
""")
st.write(max)
