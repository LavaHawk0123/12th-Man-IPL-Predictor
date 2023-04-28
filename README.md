# 12th-Man-IPL-Predictor
The main problem that this project aims to solve is the need for an accurate and user-friendly IPL score prediction tool. With the increasing popularity of the IPL and the rise of fantasy sports, there is a growing demand for accurate predictions of match outcomes and player performances. However, the majority of available prediction tools either lack accuracy or are not user-friendly. Additionally, many of these tools require users to have an extensive knowledge of cricket statistics, which can be a barrier for casual fans.

Our project aims to address these issues by providing a web application that utilizes machine learning to generate accurate predictions for the score of IPL matches. The web application is designed to be intuitive and user-friendly, allowing fans to easily input data and receive accurate predictions. Our objectives include:
<ol>
<li>Developing a web application that accurately predicts the score of IPL matches based on various input parameters such as team, venue, and number of overs.
<li>Designing a user-friendly interface that allows fans to easily input data and generate predictions without requiring extensive knowledge of cricket statistics.
<li>Incorporating machine learning algorithms to continuously improve the accuracy of predictions and provide reliable insights into player and team performance.
<li>Creating a platform that can be easily updated with the latest IPL data and statistics to ensure the accuracy of predictions.
</ol>
By achieving these objectives, we hope to provide IPL enthusiasts with a reliable and intuitive platform for making informed predictions and engaging with the tournament.
We used Python and Django Framework to create the website. HTML and CSS is used for styling. We ensured that the user’s data is stored in the database and admin can access it. 

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
cd 12th-Man-IPL-Predictor/web
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

## About the ML Implementation : 

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

