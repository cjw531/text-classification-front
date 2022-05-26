# text-classification-front

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/cjw531/text-classification-front)

This is the frontend implementation of the text classification project. To see the full implementation and the details, refer to: [Performance Comparison of Binary and Multi Class Text Classification Models With `scikit-learn` and `TensorFlow`](https://github.com/cjw531/text-classification).

For the server configuration, refer to: [`text_classification_front`](https://github.com/cjw531/text-classification-front).

## Introduction
The demo consists of two parts:
1. Predict binary text classification problem
2. Predict multiclass (7 classes here) text classification problem.

This demo runs with two types of pre-trained `TensorFlow` models:
1. CNN (Convolutional Neural Nets)
2. BERT (Bidirectional Encoder Representations from Transformers) + CNN 

For the binary classification model, the following text data may feed in to be classified:
- [0] Non-Disaster Tweet
- [1] Disaster Tweet (FYI, trained with following Tweets: COVID, Bushfires in Australia, Iran aircraft crash, and eruption of Taal Volcano in Batangas, Philippines)

For the multiclass classification model, the following text data may feed in to be classified:
- [0] automobile
- [1] entertainment
- [2] politics
- [3] science
- [4] sports
- [5] technology
- [6] world

## Demo Instruction
Input corresponding text for binary and multiclass text box and press `Predict` button below to get the predicted result.