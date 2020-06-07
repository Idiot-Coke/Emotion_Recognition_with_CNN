# Emotion_Recognition_with_CNN

This project uses the FER2013 data set to complete facial expression classification, has a visual interface, can replace the data set, replace the neural network for secondary training

## dataset

The database FER-2013 is used. This database contains a total of 35,887 face images, derived from data downloaded from the kaggle competition website([Data download address](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)).The original data stores the labels and pictures in a csv format. After a simple conversion, you can know that the picture size is 48*48 grayscale. The data set labels are 7 categories, respectively:*0:'angry',1:'disgust',2:'fear',3:'happy',4:'sad',5:'surprise',6:'neutral'.

## File Description

* `EmotionRecongnition.py`：Python UI interface generated by EmotionRecongnition_UI.ui
* `load_and_process.py`：Load data and preprocess
* `train_emotion_classifier.py`：Model training, you can set it according to your own situation
* `runMain.py`：Main program

## Model training

The network structure uses the Xception network structure, which is also a similar structure using depthwise convolution, (see the paper: [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357)).
You can also use tiny_XCEPTION, mini_XCEPTION, big_XCEPTION, simple_CNN, simpler_CNN to train your model by making changes in train_emotion_classifier.py.

In train_emotion_classifier.py you can select the neural network, select the data set, set the training parameters, set the model and log export location, and set the data enhancement method. Because the callback function is set, num_epochs can be set as large as possible.

## Usage
### Download this project
- `git clone https://github.com/Idiot-Coke/Emotion_Recognition_with_CNN.git`
### Environment configuration
- `cd Emotion_Recognition_with_CNN`
- `pip install -r requirements.txt`

## To train models for emotion classification
·Download the fer2013.tar.gz file from [here](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

·Move the downloaded file to the datasets directory inside this repository.

·Untar the file
- `tar -xzf fer2013.tar`

·Run the train_emotion_classifier.py file
- `python train_emotion_classifier.py`

## Result
 ![image]（https://github.com/Idiot-Coke/Emotion_Recognition_with_CNN/img_test/result.png）
