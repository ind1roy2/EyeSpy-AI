import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.markdown('<style>body{background-color: black;}</style>', unsafe_allow_html=True)


st.title(":blue[Welcome to EYE SPY AI]")

st.subheader(":orange[About our Web App]")
st.write("This is an initiative to prevent the rapid acceleration of near-sightedness or myopia among today's generation. Especially during the pandemic, due to increased exposure to Visual Display Terminals (VDT), several students have started using spectacles.")
st.image("https://smith-magenis.org/wp-content/uploads/myopia-featured-image.jpg", width=600)

st.subheader(":orange[The Problem]")



# Create columns for layout
col1, col2, col3, col4, col5 = st.columns(5)

# Add text and shapes to columns
with col1:
    st.write("1")
    st.markdown('<div style="width: 50px; height: 50px; background-color: blue;"></div>', unsafe_allow_html=True)
    st.write("Excessive screen time")
with col2:
    st.write("2")
    st.markdown('<div style="width: 50px; height: 50px; background-color: blue;"></div>', unsafe_allow_html=True)
    st.write("Less tear production leads to dry tear film")
with col3:
    st.write("3")
    st.markdown('<div style="width: 50px; height: 50px; background-color: blue;"></div>', unsafe_allow_html=True)
    st.write("This results in dry eyes")
with col4:
    st.write("4")
    st.markdown('<div style="width: 50px; height: 50px; background-color: blue;"></div>', unsafe_allow_html=True)
    st.write("Gives rise to visual problems")
with col5:
    st.write("5")
    st.markdown('<div style="width: 50px; height: 50px; background-color: blue;"></div>', unsafe_allow_html=True)
    st.write("Most common problem among students - myopia")




st.subheader(":orange[What is Myopia]")
st.write("Myopia, commonly known as nearsightedness, is a refractive error of the eye that causes distant objects to appear blurry, while close objects can be seen clearly. It is a prevalent vision condition that has been on the rise globally, particularly among younger populations.")
st.write("It occurs when the light rays meet before the retina. A concave lens can diverge these rays so that they meet exactly on the retina.")

st.image("https://foresee-eyecare.com/wp-content/uploads/2021/12/myopia-eye-vision-problem-1024x672.jpg",width=600)
st.subheader(":orange[Proposed Solution]")
st.write("Our app focuses on the prevention of myopia from an early stage. All you have to do is provide input in through questions asked by our form. In response, you get to know your chances of acquiring myopia in the near future, based on your current visual lifestyle.")
st.write("You can stay updated regarding the status of your eyes by just entering a few details. You need not be aware of complex medical science terms in order to provide input to our model. If one does not start taking adequate precautionary measures from an early stage, it is possible that he/she may have to use spectacles for the rest of his/her life.")
st.subheader(":orange[20-20-20 Rule]")
st.image("https://evershineoptical.com.sg/wp-content/uploads/20-20-20-rule.png",width=600)
st.subheader(":orange[Note]")
st.write("-> Please note that our app is not the replacement for any doctor. We strongly prefer taking advice from a doctor depending upon the response received by you through our app.")
st.write("-> The target audience for this app includes high school and college going students.")
st.write("-> The suggestions provided by the app would be relevant if the user is currently not using spectacles.")

#st.markdown("<p style='text-align: center;'>Center-Aligned Text</p>", unsafe_allow_html=True)

st.subheader(":orange[Contact us:]")
st.markdown('[Indraneel Roy](https://linkedin.com/in/indraneel--roy)', unsafe_allow_html=True)
st.markdown('[Aryan Rakheja](https://www.linkedin.com/in/aryan-rakheja-3429091b6)',unsafe_allow_html=True)

