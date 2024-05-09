# Movie Recommendation System

## Introduction
This 

## Data
The data used in this project is from the MovieLens dataset. This dataset was collected by the GroupLens Research Project at the University of Minnesota. The dataset contains 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users. The dataset can be found [here](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset/).


## Methodology
The methodology used in this project is collaborative filtering. Collaborative filtering is a technique used by recommender systems to make predictions about the interests of a user by collecting preferences from many users. The underlying assumption is that if a user A has the same opinion as a user B on an issue, A is more likely to have B's opinion on a different issue than that of a randomly chosen user.

## Installation
To run this project, you will need to install movie_lens dataset, specifically movies.csv and ratings.csv. You can download the dataset [here](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset/). You will also need to install the libraries from requirements.txt. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

**Note**: You will need to have Python installed on your machine to run the above command. An alternative is to use Anaconda. You can download Anaconda [here](https://www.anaconda.com/products/individual). Also, is recommended to start a virtual environment before installing the libraries. You can do this by running the following command in your terminal:

```bash
python -m venv venv
```
or 
    
```bash
conda create -n venv
```

## Usage
To run this project, you can see the code in the notebook, where I have explained the code and the results. While giving visualizations and widgets to interact with the data. You can also run the code in the python file. You can do this by running the following command in your terminal:

```bash
python app.py
```

## Conclusion
This project used a lot of python libraries that helped me along the way. I used pandas to manipulate the data, numpy to perform mathematical operations, and scikit-learn to build the model. I also used matplotlib and seaborn to create visualizations. I also used streamlit to create a web app to interact with the data. I learned a lot about collaborative filtering and how it can be used to build a recommendation system. I also learned how to use the MovieLens dataset and how to manipulate it to get the data I needed.