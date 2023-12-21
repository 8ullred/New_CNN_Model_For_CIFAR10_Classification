This is my custom-coded model made for face mask detection.

Datasets:
To train this model, we originally used our own collection of images for training purposes, but we eventually switched over to the CIFAR-10 dataset due to it both being more easily accessible and many orders of magnitude larger.

Structure of the CNN:
This CNN model is coded by myself, and as such, utilizes a custom base for the model. It uses a varying combination of Conv2D, BatchNormalization, Activation, MaxPooling2D, Dropout, 

Training and Test Results:
We used the CIFAR-10 dataset to train and test the model - after running it and letting it go on for 200 epochs, we got roughly ~80% for the validation accuracy, and about ~57% for validation loss.

Accuracy of the model:
After all the above was done and tested, the model had roughly ~80% accuracy and 60% loss. The model is continuously being improved.
