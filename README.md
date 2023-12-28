!!Face Mask Detection Model!!

Overview:

This repository contains a custom-coded model designed for face mask detection. The model is trained using a combination of our proprietary image dataset and the CIFAR-10 dataset.


Datasets

Initially, our in-house image collection was used for training, but later transitioned to the CIFAR-10 dataset for its accessibility and extensive size. The CIFAR-10 dataset comprises of over 60,000 images, with 50,000 allocated for training and 10,000 for testing.


Model Architecture

The Convolutional Neural Network (CNN) is implemented from scratch, featuring a custom base. The architecture incorporates various layers such as Conv2D, BatchNormalization, Activation, MaxPooling2D, Dropout, Flatten, and Dense layers. This combination allows the model to effectively process images and make accurate predictions.


Training and Test Results

The model is trained and tested using both our in-house image collection and the CIFAR-10 dataset. After 200 epochs, the validation accuracy reached approximately 80%, with a validation loss of around 0.56.


Model Performance

Upon completion of training and testing, the model achieved an accuracy of approximately 80% and a loss of 0.60. Continuous efforts are being made to enhance the model's performance.


Feel free to explore the code and contribute to the improvement of the face mask detection model!
