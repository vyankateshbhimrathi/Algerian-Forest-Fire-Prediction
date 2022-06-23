<div id="top"></div>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/vyankateshbhimrathi">
    <img src="https://img.icons8.com/external-flat-wichaiwi/64/undefined/external-bush-fire-climate-change-flat-wichaiwi.png" alt="Logo" width="80" height="80"/> 
  </a>

<h3 align="center">Algerian-Forest-Fire-Prediction</h3>

  <p align="center">
    Machine Learning Project
    <br />
    <a href="https://github.com/vyankateshbhimrathi/Algerian-Forest-Fire-Prediction"><strong>Explore the Repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/vyankateshbhimrathi/Algerian-Forest-Fire-Prediction/blob/main/app.py">View Flask app code</a>
    ·
    <a href="https://github.com/vyankateshbhimrathi/Algerian-Forest-Fire-Prediction/blob/main/Algerian.ipynb"> Model Building</a>
    ·
    <a href="https://github.com/vyankateshbhimrathi/Algerian-Forest-Fire-Prediction/blob/main/Algerian.ipynb">EDA on Forest Fires dataset</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
* Using Data Science and Machine learning, we can build a model that takes in the detected fires dataset learns and detects future fires based on certain Weather report.
* Storing the Sourced dataset to MongoDB.
* Building a **Flask App** hosted on **Heroku**.
* **Sklearn** for pre-processing and Model Building
* Pandas, Numpy, Matplotlib for csv reading, Data Processing, Data Cleaning, Visualization etc.

## Deployed app
[LINK TO HEROKU APP]

<!-- GETTING STARTED -->
## Introduction
*  The dataset for **Algerian Forest Fire Prediction** is taken from **UCI MACHINE LEARNING REPO**. The dataset contains a combination of forest fire observations and data in two regions of Algeria: the Bejaia region and the Sidi Bel-Abbes region. 
* The timeline of this dataset is from June 2012 to September 2012. In this project, we focused on whether certain weather features could predict forest fires in these regions using few Machine Learning algorithms. 

<!-- USAGE EXAMPLES -->
## Steps

* Installing Python, PyCharm, Monogodb, Git to Computer.
* Creating Flask app by importing `Flask` module.
* Download the source dataset from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++#).
* For Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.


### Exploratory Data Analysis
* In this step, we will apply Exploratory Data Analysis (EDA) i.e., univariate, bivariate and multivariate analysis to extract insights from the data set to know which features have contributed more in predicting Forest fire by performing Data Analysis using Pandas and Data visualization using Matplotlib & Seaborn. 
* It is always a good practice to understand the data first and try to gather as many insights from it.

### Model Building 
* Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.
* Models used : **Logistic Regression, Decision Tree, Random Forest, XGboost, K-Nearest Neighbour, Support Vector Machine, Naive Bayes.**

### Model Selection
* Based on the accuracy, precision and recall machine learning algorithm selected.
* HyperParameter Tuning is done best machine learning algorithm.


### Flask
* Importing the Flask module and creating a Flask web server from the Flask module.
* Create an object **app** in flask class with `__name__` which represents current app.py file.
* Create `/` route to render default page html.
* Create a route `/predict` to get user input for Classification. 
* Run the flask app with `app.run()` code.

### Heroku Deployment
* Create new repo in Github and push all the data using `Git`.
* Install Heroku CLI and login using `heroku login` and setup the app in Heroku Web.
* Connect with app `heroku git:remote -a appname`
* Push to Heroku using `git push heroku main`

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)


### **Tools used**
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)



<!-- CONTACT -->
## Contact
[![VYANKATESH BHIMRATHI | LinkedIn]][reach_linkedin_1]


<!-- CREDITS -->
## Credits
[![Aravind Selvam | LinkedIn](https://img.shields.io/badge/Aravind_Selvam-eeeeee?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0A66C2)][reach_linkedin]
[![Aravind Selvam | Github]][reach_github]



<!-- MARKDOWN LINKS  -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/linkedin_username

<!-- Tools Used -->
[PyCharm]: https://code.visualstudio.com/
[git]: https://git-scm.com/
[github]: https://github.com/
[heroku]: https://www.heroku.com/
[python]: https://www.python.org/
[flask]: https://flask.palletsprojects.com/en/2.1.x/
[sklearn]: https://scikit-learn.org/stable/

<!--contact-->
[reach_linkedin_1]: https://www.linkedin.com/in/vyankatesh-bhimrathi-1461a4140/

<!--CREDITS-->
[reach_linkedin]: https://www.linkedin.com/in/aravind-selvam/
[reach_github]: https://github.com/aravind9722
