import streamlit as st
st.set_page_config(
    page_title="Student Profile",
    page_icon="🎓",
    layout="centered"
)
st.title("🎓 Student Profile")
st.caption("My Profile")
st.header("Personal Information")

name = st.text_input("Enter Student Name", "DEEPTI B D")
usn = st.text_input("Enter USN", "1SV24CS038")

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

    st.write("**Name:**", DEEPTI B D)
    st.write("**USN:**", 1SV24CS038)
    st.write("**Department:**", CSE)
    st.write("**Year:**", 3rd)
