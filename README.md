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
