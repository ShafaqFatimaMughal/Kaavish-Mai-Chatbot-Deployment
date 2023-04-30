# Kaavish-Mai-Chatbot-Deployment
This code is a sample that helps host the Mai model on Google Cloud Platform. The project can be found on the following GitHub: <br />
https://github.com/ShafaqFatimaMughal/Kaavish-Mai-Transformer-Based-Urdu-Chatbot

## How To Host The Model on GCP
### Step 0: Clone this Repository

### Step 1: Create your model and your Flask API
Once you have trained your model, you can save it as a pickle (.pkl) file in this code repository. So, open up the Deployment folder and paste your .pkl file. Once you've created your flask model you will need to create a main.py file that runs your model in the form of an API. You can learn more about this here: <br />
https://www.youtube.com/watch?v=UbCWoMf80PY

### Step 3: Setup Google Cloud
Create a free Google Cloud account and Create a new Project. Next, activate the two following APIs:
1) Cloud Run API
2) Cloud Build API

Once you've activated your APIs, you are good to go.

### Step 4: Install and initialize the Google Cloud SDK
You can install and initialize the Google Cloud SDK by following the instructions in the Google Cloud documentation:
https://cloud.google.com/sdk/docs/install

### Step 5: Initialize the Dockerfile, requirments.txt, and .dockerignore
The Dockerfile is used to initialize the enviroment. If you plan on running a simple model on GCP then you should be good to go. You will only need to tweak the requirements.txt file based on your need. <br />
Once you've configured the requirements.txt, you can make adjustments to the .dockerignore file. The .dockerignore fill will mention anyfile that you will not need to run the main application. Here we have only defined it as the text.py file which we were using to test out the model.

### Step 6: Cloud Build and Deploy
Once you have everything up and ready, you can host your model by running the following commands: <br />
```gcloud builds submit --tag gcr.io/<project-id>/get_prediction``` <br />
```gcloud run deploy --image gcr.io/<project-id>/get_prediction --platform managed```
