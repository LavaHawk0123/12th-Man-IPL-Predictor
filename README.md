# 12th-Man-IPL-Predictor

This Django and Machine Learning powered Web app predicts and analyse IPL matches. It currently has three working model i.e 
prediction of a match winner before toss, prediction of expected score of 1st inning at any point of time during the match 
and prediction of winner, match concluding over during the 2nd inning of the match.


## Webpage
Live project is available [here](https://fourth-umpire.herokuapp.com).


## Local Setup
Create and activate a virtualenv:

```bash
virtualenv cfd_apriori
cd cfd_apriori
source bin/activate
```
Clone the repository on your local environment <br>

```bash
git clone https://github.com/LavaHawk0123/12th-Man-IPL-Predictor.git `
```

Navigate to the folder <br>
```bash 
cd 4th_umpire/web
```

Install the required dependencies <br>
```bash
pip3 install -r requirements.txt 
```

Run the localhost-server <br>
```bash 
python3 manage.py runserver
```

The web-app will be available at `127.0.0.1:8000` on your browser. 

## About
This web-app is created for Microsoft Code Fun Do competition.

- In this project we have tried various algorithms like Naive Bayes, SVM, Random Forest  for training our various machine learning models. And finally,we have used random forest algorithm. 

- We have used dataset from Kaggle and then modified the csv files and make various csv files in order to train and for working of our different models.In addition, We have use varoius python libraries such as scikit learn, numpy, pandas,etc in order to code our models. 

# Screenshots: 
#### Landing Page
![Landing_Page](https://user-images.githubusercontent.com/75236655/234510115-40e9d8ef-f723-47fb-ad3d-dd389d977e81.png)

##### Predictions Pane
![Predictions_Pane](https://user-images.githubusercontent.com/75236655/234510148-dcf8c5dd-f79c-47d5-a3d9-c3f41f4ee8f0.png)

##### Predict Page
![Predict_Page](https://user-images.githubusercontent.com/75236655/234510181-b85a13c0-4ac5-48fb-98d1-44c0a71f8b87.png)

##### Statistics Pane
![STat+Contact](https://user-images.githubusercontent.com/75236655/234510205-c6f7c11f-0566-4f6f-bfa1-2f458b513d96.png)

##### About Us Page
![About_Page](https://user-images.githubusercontent.com/75236655/234510225-63351882-c593-4e35-b526-91cf906d2df9.png)

##### Gallery Page
![Gallery](https://user-images.githubusercontent.com/75236655/234756601-faabc333-565b-4dd4-9b13-6634173f4f28.png)

