import streamlit as st
st.title("ejmplo para usar session_state")

if 'count' not in st.session_state:
  st.session_state['count'] = 0

if 'name' not in st.session_state:
  st.session_state.'name'. = ''
  
if st.button('click me'):
  st.session_state['count'] += 1

nombre = st.text_input("escribe tu nombre")
st.write(nombre)

st.write(st.session_state)
