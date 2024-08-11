# Movie Recommendation System

## Data
The data used in this project is from the MovieLens dataset. This dataset was collected by the GroupLens Research Project at the University of Minnesota. The dataset can be found [here](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset/).

## Methodology
The methodology used in this project is collaborative filtering. Collaborative filtering is a technique used by recommender systems to make predictions about the interests of a user by collecting preferences from many users. The underlying assumption is that if a user A has the same opinion as a user B on an issue, A is more likely to have B's opinion on a different issue than that of a randomly chosen user. 

## Running the Website

To run the website using Streamlit, follow these steps:

1. Start the Streamlit server:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to the url shown in your terminal.

## Conclusion
This project used a lot of python libraries that helped me along the way. I used pandas to manipulate the data, numpy to perform mathematical operations, and Surprise to build the model. I also used matplotlib to create visualizations. I also used streamlit to create a web app to interact with the data. I learned a lot about collaborative filtering and how it can be used to build a recommendation system. I also learned how to use the MovieLens dataset and how to manipulate it to get the data I needed.

## License

This project is licensed under the [MIT License](LICENSE).
