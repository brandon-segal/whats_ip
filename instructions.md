# Instructions 

The assignment is rather simple, given a string of text i'd like to detect IP Addresses and Persons/Names in the string. For example: for input "Bob found that 127.0.0.1 was bad and 123.4.5.6 was safe." Should return that 127.0.0.1 and 123.4.5.6 are IPAddresses and that Bob is a person. 

```python 
def entity_recognition(string):
    """
    A function that can take in a string of data and returns a dictionary of entities labeled as either people or IP addresses 
    """
```

You may use any python packages you wish and any data structures/print statements etc to return or show your results. I'm most looking for general discussion for any kind of weaknesses with the approach that you use as well as general thoughts about the problem. I'd like to see discussion about how you would approach testing this problem or about any other possible solution paths you would be looking to test (again you only need to implement one).

# Constraints 

The only specific request is that you use python so that we can easily integrate it into our existing code base. 

# Organization

The organization is a cybersecurity firm that is trying to build machine learning models on the unlabeled data to better understand how certain documents holding information are related to each other and how they can be related to other data sets. 

## Technologies Used

In this project we utilize the Spacy Library to build statistically based and rules based tools to find Users and IP addresses 

## Use case 

The hypothetical use case for this feature is the organization has multiple sources of text data from data stored in S3 buckets, databases, streaming web applications, and email servers and they want to be able to mine text data regarding what IP addresses were associated with messages containing certain individuals. 

## Approach 

For this application we are going have a TDD methodology to develop a Entity Recognition tool that takes in a string and returns a map of IP addresses and names. 

## Entitiy Classifier API

The entity classifier API is a class that instantiates a Spacy language model and optional additional entity labels in either a dict or file format. If there is a file format it is expected in a jsonl format and is read into a Entity Ruler where it runs rules over each tokenized string before the named entity recognition step of the spacy object. 

To instantiate a 