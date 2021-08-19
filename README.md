# PASSENGER SATISFACTION
Passenger Satisfaction is <i>my first full-stack data science project</i> where I built a web application 
over the machine learning model for this problem. I learned how to deploy a machine learning model into production in this project.
<h3> Problem: </h3>
<p>
 The objective or goal of this project is to guide an airlines company to determine the important 
 factors that influences the customer or passenger satisfaction. I built a binary classifier model to determine whether a customer
 is satisfied or not.
 In this project, the <a href="https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining">CRISP-DM methodology</a>
 has been implemented to derive an appropriate solution for a business problem. It is carried out in six phases - 
 Business understanding, Data understanding, Data preparation, Data Modelling, Evaluation and Deployment.
 </p>

* **Technologies Used:** Machine Learning, Python
* **Framework:** Django
* **Frontend:** Html, CSS, JavaScript and JQuery 



### Project Demo

 > *Click on the image below to go to the project demo.*

 > [![PASSENGER SATISFACTION - PROJECT DEMO](static/images/Passenger_Satisfaction_Thumbnail.PNG)](https://www.youtube.com/watch?v=4v2mJSBRhnY)



### Data
<p>
  The Passenger Satisfaction is distributed across 2 categories with over 0.13 million records of passenger's information.
  Each record in the dataset contains 24 attributes like age, gender, type of travel etc.
</p>

 <h3> Highlights about the data: </h3>
 <ul>
   <li>
     In this data set, the ‘Arrival Delay in Minutes’ column has 310 missing values in it. 
     These missing values are imputed with the mean values of the non-missing values of the same column.
   </li>
   <li>
     99.2% of 'Loyal' customers who go for 'Personal' travel type are satisfied. (Customer type, Travel type are attributes and 
     Satisfied is the class variable.)
   </li>
 </ul>

 <h3> Models used: </h3>
 <ul>
   <li>Naive Bayes</li>
   <li>Logistic Regression</li>
   <li>Random Forest</li>
   <li>XGBoost</li>
   <li>Ensemble Vote Classifier</li>
 </ul>
 
 <h6> Conclusions: </h6>
<ul>
<li>Although Random Forest Classifier took lesser time, XGBoost model gave the best performance of 96.04% accuracy.</li>
<li>Feature Engineering was one of the most important steps while solving this problem, on performing which the accuracy increased from 94% to 96%.</li>
</ul>

Detailed explanation of Machine Learning aspects of this project: [Medium blog](https://shiva1gandluri.medium.com/passenger-satisfaction-f213ec5cc9f7)

### Table of Contents

* [Versions](#versions)
* [Terminal Commands](#terminal-commands)
* [File Structure](#file-structure)
* [Find me](#find-me)


### Versions

* Python : 3.6.5
* Django : 3.2
* Scikit-learn : 0.19.1
* Bootstrap : 4.0



### Terminal Commands

1. Open Terminal
2. Install Python and necessary libraries (joblib, pandas, scikit learn and bootstrap modal forms)
3. Install Django as mentioned in [Django Official Page](https://www.djangoproject.com/download/).
4. Go to your virtual environment project by running the command in terminal: ```workon your_virtualenv_name```
5. Run in terminal: ```python ./manage.py runserver```
6. Navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### File Structure

Within the download you'll find the following directories and files:

```
passenger-satisfaction
├── .vscode
│   └── settings.json
├── feedback
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── migrations
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-36.pyc
│   │   └── __init__.py 
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── ml_model
│   ├── __pycache__
│   │   └── py_functions.cpython-36.pyc
│   ├── finalized_model_satisfaction.sav
│   ├── model.py
│   ├── py_functions.py
│   └──  satisfaction_2015.csv
├── passenger_satisfaction
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── fonts
│   │   └── Mallanna.css
│   ├── gifs
│   │   ├── sorry_milk.gif
│   │   └── thankyou_milk.gif
│   ├── images
│   │   ├── Passenger_Satisfaction_Thumbnail.PNG
│   │   ├── aeroplane_1.jpg
│   │   └── aeroplane_8.jpg
│   ├── bootstrap_4.css
│   ├── bootstrap_edited.css
│   └── styles.css
├── templates
│   ├── feedback
│   │   └── index.html
│   └── fonts.css
├── README.md
├── finalized_model_satisfaction.sav
├── manage.py
└── passenger_satisfaction-checkpoint.ipynb
```

### Find me

- LinkedIn : https://www.linkedin.com/in/shiva-gandluri-63016416b/
- Youtube : https://www.youtube.com/channel/UC_vlvekR9zdzK0nG2bXvkKQ
