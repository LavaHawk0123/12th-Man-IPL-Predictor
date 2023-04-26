import numpy as np
import joblib
import pickle
import random
import os
#from sklearn.preprocessing import fit
script_dir = os.path.dirname(__file__)

def pre_match_predict(season,team1,team2,city):
    rel_path = "pre_pred/pre_pred.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "pre_pred/pre_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[season,team1,team2,city]]
    #enc = enc.fit(X_test)
    #X_test = enc.transform(X_test).toarray()
    print(len(X_test[0]))
    #y_pred = regressor.predict(X_test)
    #print("our_prediction:",y_pred)
    result = random.uniform(0.4,0.6)
    return result



def predict_1st_inn(team_batting,team_bowling,run,ball,wicket,city):
    rel_path = "1st_inn/1st_inn_pred.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "1st_inn/1st_inn_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[team_batting,team_bowling,run,ball,wicket,city]]
    #enc = enc.fit(X_test)
    #X_test = enc.transform(X_test).toarray()
    print(len(X_test[0]))
    #y_pred = regressor.predict(X_test)
    #print("our_prediction:",y_pred)
    runs_per_ball = run/ball
    additional = int((10-wicket)*3*6*runs_per_ball)
    result = random.randint(additional,additional+50)
    return result

def predict_if_bat_win(team_batting,team_bowling,run,ball,wicket,target,city):
    rel_path = "2nd_inn/bat_win/2nd_inn_bat_win_wicket.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/bat_win/2nd_inn_bat_win_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))
    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    #enc.fit(X_test)
    #X_test = enc.transform(X_test).toarray()
    #y_pred = regressor.predict(X_test)
    #print("our_prediction:bat_win:wicket",y_pred)
    result = random.randint(run,run+50)
    return result

def predict_if_bowl_win(team_batting,team_bowling,run,ball,wicket,target,city):
    rel_path = "2nd_inn/bowl_win/2nd_inn_bowl_win_run.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/bowl_win/2nd_inn_bowl_win_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    #enc = enc.fit(X_test)
    #X_test = enc.transform(X_test).toarray()
    #y_pred = regressor.predict(X_test)
    result = random.randint(run,run+50)
    return result


def predict_2nd_end_ball(team_batting,team_bowling,run,ball,wicket,target,city):
    rel_path = "2nd_inn/end/2nd_inn_end.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/end/2nd_inn_end_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    #enc = enc.fit(X_test)
    #X_test = enc.transform(X_test).toarray()
    #y_pred = regressor.predict(X_test)
    result = [0,0]
    result[0] = random.randint(run,run+50)
    result[1] = random.randint(4,9)
    return result



def predict_2nd_inn(team_batting,team_bowling,run,ball,wicket,target,city):
    rel_path = "2nd_inn/who_win/2nd_inn_win_pred.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/who_win/2nd_inn_win_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))
    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    #enc = enc.fit(X_test)
    #X_test = enc.transform(X_test).toarray()
    #y_pred = regressor.predict(X_test)
    #end_ball = predict_2nd_end_ball(team_batting,team_bowling,run,ball,wicket,target,city)
    #if y_pred[0]>=0.5:
    #     info = predict_if_bat_win(team_batting,team_bowling,run,ball,wicket,target,city)
    #else:
    #    info = predict_if_bowl_win(team_batting,team_bowling,run,ball,wicket,target,city)
    result = [0,0,0,0]
    team = random.randint(1,3)
    result[0] = random.uniform(0.4,0.6)
    result[1] = random.randint(4,9)#random.randint(run,run+50)
    result[2] = random.randint(4,9)
    if(result[1]>0.5):
        result[3] = team_bowling
    else:
        result[3] = team_batting
    return result


def get_team(id):
    teams = {
            "1":'Sunrisers Hyderabad',
            "2":'Royal Challengers Bangalore',
            "3":'Chennai Super Kings',
            "4":'Kings XI Punjab',
            "5":'Rajasthan Royals',
            "6":'Delhi Daredevils',
            "7":'Mumbai Indians',
            "8":'Kolkata Knight Riders'
    }
    return teams[id]




#pred = predict_1st_inn(2,5,12,15,2,4)
#print("---------first-----------",pred)
#pred = predict_2nd_inn(1,6,12,15,2,174,11)
#print("-----------2nd---------------",pred)
