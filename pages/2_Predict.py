import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn

st.markdown('<style>body{background-color: black;}</style>', unsafe_allow_html=True)

def load_model():
    with open('saved_steps_correct.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
s1 = data['model1']
log = data['model2']
s = data['s']
ord2 = data['ord2']
ord1 = data['ord1']
ohe = data['ohe']
le = data['le']

st.title(":blue[Check your Score]")
st.subheader("Kindly devote some of your precious time to fill in the details and check the status of your eyes.")

ages = ['15-18 yrs','18-20 yrs','20-25 yrs']
dryness = ['0 - never','1 - rarely','2 - sometimes','3 - very often','4 - always']
gender_options = ['Male','Female']

age_group = st.selectbox("Which age group do you belong to?", ages)
screen_time = st.slider("What is the average screen time you spend on digital devices? (in minutes)",0,420,60)
level_of_dryness = st.selectbox("How often do you experience dryness in eyes?(redness, itching and irritation)",dryness)
parents = st.slider("Do you have family history of myopia? (select 0 if no, 1 if yes)",0,1,0)
gender = st.selectbox("Enter your gender",gender_options)

predict = st.button("Predict")
if predict:
    x = np.array([[age_group,screen_time,level_of_dryness,parents,gender]])
    #x[0,1]=s.transform(x[[0,1]])
    #x[0,4]=ohe.transform(x[[0,4]])
    #x[0,0]=ord.transform(x[[0,0]])
    #x[0,2]=ord.transform(x[[0,2]])
    #x = x.astype('float')
    #x = x.reshape(-1,1)
    x0=x[:,0].reshape(1,-1)
    x1=x[:,1].reshape(1,-1)
    x2=x[:,2].reshape(1,-1)
    x3=x[:,3].reshape(1,-1)
    x4=x[:,4].reshape(1,-1)
    def age_category(z):
        if z == '15-18 yrs':
            x0 = np.array([[0]])
        elif z == '18-20 yrs':
            x0 = np.array([[1]])
        else:
            x0 = np.array([[2]])
        return x0
    def dryness(y):
        if y == '0 - never':
            x2 = np.array([[0]])
        elif y == '1 - rarely':
            x2 = np.array([[1]])
        elif y == '2 - sometimes':
            x2 = np.array([[2]])
        elif y == '3 - very often':
            x2 = np.array([[3]])
        else:
            x2 = np.array([[4]])
        return x2
    x0 = age_category(age_group)
    x1=s.transform(x1)
    x2 = dryness(level_of_dryness)
    #xl = ord1.transform(x2)
    #y = np.concatenate((x0,x2),axis=0).reshape(1,-1)
    #xal = ord.transform(y)
    if gender == 'Male':
        x4 = np.array([[1]])
    else:
        x4 = np.array([[0]])
    print(x0)
    y = np.hstack((x0,x1,x2,x3,x4))
    y = y.astype(float)

    Spectacles = log.predict(y)
    #print(s1.predict_proba(y))
    
    prob = log.predict_proba(y)
    answer = str((prob[0][1]*100))[0:4]
    
    if float(answer)>=0 and float(answer)<=25:
        st.balloons()
        st.subheader(":green[Congratulations! You are good to go ]:sunglasses: :thumbsup:")
        st.subheader("Your chances of acquiring myopia are "+answer+"%")
        st.subheader("Level of risk: Low")
        st.subheader("Need for consultation: Atleast once a year")

        st.write("-> Continue practicing healthy eye habits, such as taking breaks during screen time, maintaining proper lighting, and keeping screens at eye level.")
        st.write("-> Consume a balanced diet rich in vitamins and nutrients that support eye health, including foods with vitamin A, vitamin C, and omega-3 fatty acids.")
        
    elif float(answer)>25 and float(answer)<=50:
        st.subheader(":neutral_face:")
        st.subheader("Your chances of acquiring myopia are "+answer+"%")
        st.subheader("Level of risk: Medium")
        st.subheader("Need for consultation: Atleast once in every six months")

        st.write("-> Continue managing screen time effectively, ensuring that you follow the 20-20-20 rule (every 20 minutes, look at something 20 feet away for at least 20 seconds).")
        st.write("-> Ensure that your workspace and study area have proper lighting to reduce eye strain.")

    elif float(answer)>50 and float(answer)<=75:
        st.subheader(":confused:")
        st.subheader("Your chances of acquiring myopia are "+answer+"%")
        st.subheader("Level of risk: High")
        st.subheader("Need for consultation: Once every quarter")

        st.write("-> Limit prolonged periods of close-up work. Take longer breaks, and incorporate more outdoor time into your daily routine.")
        st.write("-> Ensure your screen is at eye level, and use an ergonomic chair and desk.")

    elif float(answer)>75 and float(answer)<=100:
        st.subheader(":red[Danger! ]:cry: :-1:")
        st.subheader("Your chances of acquiring myopia are "+answer+"%")
        st.subheader("Level of risk: Extreme")
        st.subheader("Need for consultation: Once in every two to three months")

        st.write("-> Implement strict screen time limitations and adhere to the 20-20-20 rule. Consider reducing screen time to the bare essentials.")
        st.write("-> Embrace an outdoor lifestyle and engage in outdoor activities as much as possible. Aim for a minimum of two hours of outdoor time daily.")
