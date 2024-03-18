
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Specialist Doctor Suggestion'],
                          icons=['activity','heart','person'],
                          default_index=0)


if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)



# Parkinson's Prediction Page
if (selected == 'Specialist Doctor Suggestion'):
    st.header("Heart Disease And Diabetes Speacialist Doctor Contacts")
# Create a button, that when clicked, shows a text
    
    if(st.button("Diabetes Dr.Navneet Agarwal")):
        st.text("Mobile number - : 0751 407 7724 \nAddress - Laltitpur Colony Gwalior\n 9:30 am–2 pm, 6–8 pm")
Skip to content
8982138233
/
public_ml_web_ap

Type / to search

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Editing mdps_public.py in public_ml_web_ap
Breadcrumbspublic_ml_web_ap
/
mdps_public.py
in
main

Edit

Preview
Indent mode

Spaces
Indent size

4
Line wrap mode

No wrap
Editing mdps_public.py file contents
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)



# Parkinson's Prediction Page
if (selected == 'Specialist Doctor Suggestion'):
    st.header("Heart Disease And Diabetes Speacialist Doctor Contacts")
# Create a button, that when clicked, shows a text
    
    if(st.button("Diabetes Dr.Navneet Agarwal")):
        st.text("Mobile number - 1860500106\nAddress - Laltitpur Colony Gwalior\n Mon-Sat Timings- 9:30 am–2 pm, 6–8 pm")
    
    if(st.button("Diabetes Dr.Pankaj Gupta")):
        st.text("Mobile Number - 9827869595\nAddress - Tulsi Vihar Colony Gwalior\ Mon- Sat Timings 10:00 am - 16:00 pm")

    if(st.button("Diabetes Dr.R.K Singhal")):       
        st.text(" Mobile Number - 6269841913\nAddress - Janakganj Gwalior\nMon- Sat Timings 10:00am - 17:00 pm")

    if(st.button("Heart Dr.Dalmia")):     
        st.text("Mobile Number - 9425752462\nAddress - Gole Ke Mandir Gwalior\nMon- Sat Timings 11:00am - 16:00 pm")

    if(st.button("Heart Dr.Ram Rawat")):  
        st.text("Mobile Number - 07512436093\nAddress - Kampoo Bus stand Gwalior\nMon- Sat Timings 10:00am - 18:00 pm")

    if(st.button("Heart Dr.Dushyant Deo")):     
        st.text("Mobile Number - 7700271131\nAddress jhinshi Road no.3 Gwalior\nMon- Sat Timings 10:00am - 15:00 pm")

