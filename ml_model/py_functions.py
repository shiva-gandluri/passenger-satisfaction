#importing required libraries
import pandas as p

# some useful functions to encode labels
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

# renaming functions for convienience
def rename_func(df2):
    df2 = df2.rename(columns={'Flight Distance': 'FDistance'})
    df2 = df2.rename(columns={'Type of Travel': 'Travel_type'})
    df2 = df2.rename(columns={'Customer Type': 'Cus_Type'})
    df2 = df2.rename(columns={'Inflight wifi service': 'Inflight_wifi_service'})
    df2 = df2.rename(columns={'Departure/Arrival time convenient' : 'DA_time_conv'})
    df2 = df2.rename(columns={'Ease of Online booking' : 'Ease'})
    df2 = df2.rename(columns={'Gate location' : 'Gate_location'})
    df2 = df2.rename(columns={'Food and drink' : 'Food_and_drink'})
    df2 = df2.rename(columns={'Online boarding' : 'Online_boarding'})
    df2 = df2.rename(columns={'Seat comfort' : 'Seat_comfort'})
    df2 = df2.rename(columns={'Inflight entertainment' : 'Inflight_entertainment'})
    df2 = df2.rename(columns={'On-board service' : 'Onboard_service'})
    df2 = df2.rename(columns={'Leg room service' : 'Leg_room_service'})
    df2 = df2.rename(columns={'Baggage handling' : 'Baggage_handling'})
    df2 = df2.rename(columns={'Checkin service' : 'Checkin_service'})
    df2 = df2.rename(columns={'Inflight service' : 'Inflight_service'})
    df2 = df2.rename(columns={'Departure Delay in Minutes' : 'Departure_Delay_in_Minutes'})
    df2 = df2.rename(columns={'Arrival Delay in Minutes' : 'Arrival_Delay_in_Minutes'})
    return df2


# to preprocess data as per observations from data analysis
def preprocessing(df2):
    bins = [0, 29,61, 100]
    labels = [0,1,2]
    df2['binned'] = p.cut(df2['Age'], bins=bins, labels=labels)
    df2['loy'] = list(map(loy,df2['Cus_Type'],df2['Class']))
    df2['tt'] = list(map(tt,df2['Cus_Type'],df2['Travel_type']))
    df2['Gender'] = df2['Gender'].map(gender)
    del df2['Travel_type']
    del df2['Age']
    del df2['Cus_Type']
    del df2['Class']
    del df2['Departure_Delay_in_Minutes']
    del df2['Arrival_Delay_in_Minutes']
    del df2['id']
    return df2

