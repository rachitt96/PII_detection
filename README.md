# PII_detection
According to wikipedia (https://en.wikipedia.org/wiki/Personally_identifiable_information), PII is any information (sensitive or insensitive) that can be used to reach to a particular person. So, it is important to predict whether any document (For ex, an email) has PII or not. If such a document is not detected at a particular time (before uploading to cloud), then it can become a very serious security issue and it can also result in permenant closer of an organization.

The main goal of this project is to detect if an email contains PII or not using Artificial Intelligence. The whole project is being done using Natural Language Processing (for converting the text to vector) and Machine Learning (for getting insights from vectors) techniques. I used Enron Corporation (https://en.wikipedia.org/wiki/Enron) email dataset (corpus) for building this project.

The training data (to train the model) was required to start the project as Supervised Machine Learning technique has been used. So, the first phase of the project was to develop the training set (containng emails with lables of each email) of a number of emails. I considered Full Name, Home Address, Email Id, Telephone Number, SSN, Passport Number attributes for labeling the email as PII (1) or Not PII (0). I considered around 100 emails for the tarining phase and considered all emails for the testing phase. I have uploaded the testing data in AWS S3 Bucket. Enron emails consist of a lot of information, but among all I just considerd "To" and "Message Body" for building both datasets.

Two Python programs: get_aws_data.py and pii_detection_test.py are developed. The first program (get_aws_data.py) takes the location of S3 as input and download the test dataset in the proper folder. The second program (pii_detection_test.py) takes the dowloaded test data and already present trainig data as input. Then, it will train the model (based on training data). Then, the same model is applied to predict the lables of all emails (of test data). Then, it will make the tab seprated file (containing document id with its lable), so that emails containing PII (lable 1) can be easily detected.

### Instructions ###
First step is to clone this project. Instructions (commands) to build and run docker image for this project after cloning it:
- [ ] docker build -t testing-docker .
- [ ] docker run -v ~/.aws/credentials:/root/.aws/credentials -i -t testing-docker /bin/bash
