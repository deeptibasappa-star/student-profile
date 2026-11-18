import streamlit as st
st.set_page_config(
    page_title="Student Profile",
    page_icon="🎓",
    layout="centered"
)
st.title("🎓 Student Profile")
st.caption("My Profile")
st.header("Personal Information")

name = st.text_input("Enter Student Name", "xxxxxxxxx")
usn = st.text_input("Enter USN", "xxxxxxxxx")

department = st.selectbox(
    "Department",
    ["CSE", "ISE", "ECE", "EEE", "ME"]
)

year = st.radio(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

# Submit Button
if st.button("View My Profile"):

    st.success("Profile submitted successfully!")

    st.subheader("Profile Details")

    st.write("**Name:**", name)
    st.write("**USN:**", usn)
    st.write("**Department:**", department)
    st.write("**Year:**", year)
