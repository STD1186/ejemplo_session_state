import streamlit as st
st.title("ejmplo para usar session_state")

if "count" not in st.session_state:
  st.session_state["key"] = 0

#count = 0

increment = st.button("increment")
if increment:
  count += 1

st.write("count = ", count)

st.write(st.session_state)
