from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pandas as p 
from pandas import DataFrame
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import json

# Create your views here.
"""def index(request):
    return render(request,'feedback/index.html')"""

def rename_func(data_frame):
    data_frame = data_frame.rename(columns={'Flight Distance': 'FDistance'})
    data_frame = data_frame.rename(columns={'Type of Travel': 'Travel_type'})
    data_frame = data_frame.rename(columns={'Customer Type': 'Cus_Type'})
    data_frame = data_frame.rename(columns={'Inflight wifi service': 'Inflight_wifi_service'})
    data_frame = data_frame.rename(columns={'Departure/Arrival time convenient' : 'DA_time_conv'})
    data_frame = data_frame.rename(columns={'Ease of Online booking' : 'Ease'})
    data_frame = data_frame.rename(columns={'Gate location' : 'Gate_location'})
    data_frame = data_frame.rename(columns={'Food and drink' : 'Food_and_drink'})
    data_frame = data_frame.rename(columns={'Online boarding' : 'Online_boarding'})
    data_frame = data_frame.rename(columns={'Seat comfort' : 'Seat_comfort'})
    data_frame = data_frame.rename(columns={'Inflight entertainment' : 'Inflight_entertainment'})
    data_frame = data_frame.rename(columns={'On-board service' : 'Onboard_service'})
    data_frame = data_frame.rename(columns={'Leg room service' : 'Leg_room_service'})
    data_frame = data_frame.rename(columns={'Baggage handling' : 'Baggage_handling'})
    data_frame = data_frame.rename(columns={'Checkin service' : 'Checkin_service'})
    data_frame = data_frame.rename(columns={'Inflight service' : 'Inflight_service'})
    data_frame = data_frame.rename(columns={'Departure Delay in Minutes' : 'Departure_Delay_in_Minutes'})
    data_frame = data_frame.rename(columns={'Arrival Delay in Minutes' : 'Arrival_Delay_in_Minutes'})
    return data_frame

def preprocessing(data_frame):
    def loy(x,y):
        if (x=='Loyal Customer' and (y== 'Eco' or y== 'Business' or y== 'Eco Plus')) :
            return(1)
        else:
            return(0)

    def tt(x,y):
        if (x=='Loyal Customer' and (y== 'Business Travel' or y== 'Personal Travel')) :
            return(1)
        else:
            return(0)

    def gender(x):
        if x=='Male' :
            return 1 
        else :
            return 0
    bins = [0, 29,61, 100]
    labels = [0,1,2]
    #data_frame['Age'] = pd.to_numeric(data_frame['Age'])
    data_frame = data_frame.apply(p.to_numeric, downcast='integer', errors='ignore')
    data_frame['binned'] = p.cut(data_frame['Age'], bins=bins, labels=labels)
    data_frame['loy'] = list(map(loy,data_frame['Cus_Type'],data_frame['Class']))
    data_frame['tt'] = list(map(tt,data_frame['Cus_Type'],data_frame['Travel_type']))
    data_frame['Gender'] = data_frame['Gender'].map(gender)
    del data_frame['Travel_type']
    del data_frame['Age']
    del data_frame['Cus_Type']
    del data_frame['Class']
    del data_frame['Departure_Delay_in_Minutes']
    del data_frame['Arrival_Delay_in_Minutes']
    del data_frame['id']
    return data_frame

def index(request):
    #cls = joblib.load('ml_model/finalized_model_satisfaction.sav')
    user_info = []
    cols = ['id', 'Gender', 'Customer Type', 'Age', 
        'Type of Travel', 'Class', 'Flight Distance', 'Inflight wifi service',
       'Departure/Arrival time convenient', 'Ease of Online booking',
       'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
       'Inflight entertainment', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Inflight service',
       'Cleanliness', 'Departure Delay in Minutes',
       'Arrival Delay in Minutes']
    class_label = 0
    if request.method == 'GET':
        return render(request,'feedback/index.html')
    if request.method == 'POST':
        user_info.append(request.POST.get('id'))
        user_info.append(request.POST.get('gender'))
        user_info.append(request.POST.get('customer_type'))
        user_info.append(request.POST.get('age'))
        user_info.append(request.POST.get('type_of_travel'))
        user_info.append(request.POST.get('class'))
        user_info.append(request.POST.get('flight_distance'))
        user_info.append(request.POST.get('inflight_wifi_service'))
        user_info.append(request.POST.get('time_convenience'))
        user_info.append(request.POST.get('ease_of_booking'))
        user_info.append(request.POST.get('gate_location'))
        user_info.append(request.POST.get('food_and_drink'))
        user_info.append(request.POST.get('online_boarding'))
        user_info.append(request.POST.get('seat_comfort'))
        user_info.append(request.POST.get('inflight_entertainment'))
        user_info.append(request.POST.get('onboard_service'))
        user_info.append(request.POST.get('leg_room_service'))
        user_info.append(request.POST.get('baggage_handling'))
        user_info.append(request.POST.get('checkin_service'))
        user_info.append(request.POST.get('inflight_service'))
        user_info.append(request.POST.get('cleanliness'))
        user_info.append(request.POST.get('departure_delay'))
        user_info.append(request.POST.get('arrival_delay'))
        print(user_info)
        #converting data into dataframe for test data prediction
        data_frame = DataFrame(user_info).transpose()
        data_frame.columns = cols
        #preprocessing
        data_frame.rename(columns={'Flight Distance': 'FDistance', 'Type of Travel': 'Travel_type', 'Customer Type': 'Cus_Type', 
        'Inflight wifi service': 'Inflight_wifi_service', 'Departure/Arrival time convenient' : 'DA_time_conv', 
        'Ease of Online booking' : 'Ease', 'Gate location' : 'Gate_location', 'Food and drink' : 'Food_and_drink', 
        'Online boarding' : 'Online_boarding', 'Seat comfort' : 'Seat_comfort', 'Inflight entertainment' : 'Inflight_entertainment', 
        'On-board service' : 'Onboard_service', 'Leg room service' : 'Leg_room_service', 'Baggage handling' : 'Baggage_handling', 
        'Checkin service' : 'Checkin_service', 'Inflight service' : 'Inflight_service', 
        'Departure Delay in Minutes' : 'Departure_Delay_in_Minutes', 'Arrival Delay in Minutes' : 'Arrival_Delay_in_Minutes'}, inplace=True)
        data_frame = preprocessing(data_frame)
        #model prediction
        cls = joblib.load('ml_model/finalized_model_satisfaction.sav')
        class_label = cls.predict(data_frame)
        print("class label: "+str(class_label))
    # return render(request,'feedback/results.html', {'class_label' : True}) if (class_label == 1) else render(request,'feedback/failure.html',  {'class_label' : False})
    #return JsonResponse({'class_label':True}) if (class_label == 1) else JsonResponse({'class_label':False})
    return render(request, 'feedback/index.html', {'class_label': class_label, 'successful_submit': True})