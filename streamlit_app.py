import streamlit as st

# Page Title
st.title('Healthcare Operational Starter Pack')

# Sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Analytics', 'Data Entry'])

# Home Page
if page == 'Home':
    st.write('Welcome to the Healthcare Operational Starter Pack!')

# Analytics Page
elif page == 'Analytics':
    st.subheader('Analytics Dashboard')
    # Add your analytics visualizations and insights here

# Data Entry Page
elif page == 'Data Entry':
    st.subheader('Data Entry')
    # Add your forms and data entry components here

# Footer
st.sidebar.write('Powered by Streamlit')
