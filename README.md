This is my custom-coded model made for face mask detection.

Datasets:
To train this model, we originally used our own collection of images for training purposes, but we eventually switched over to the CIFAR-10 dataset due to it both being more easily accessible and many orders of magnitude larger. The CIFAR-10 dataset boasts 60,000 usable images for training - 50,000 images are dedicated to the actual training and 10,000 are for the tests.

Structure of the CNN:
This CNN model is coded by myself, and as such, utilizes a custom base for the model. It uses a varying combination of Conv2D, BatchNormalization, Activation, MaxPooling2D, Dropout, Flatten, and Dense layers for the model to properly process and pass correct decisions on images fed to it. 

Training and Test Results:
We used the CIFAR-10 dataset to train and test the model - after running it and letting it go on for 200 epochs, we got roughly ~80% for the validation accuracy, and about 0.56 for validation loss. 

Accuracy of the model:
After all the above was done and tested, the model had roughly ~80% accuracy and 0.60 loss. The model is continuously being improved.
