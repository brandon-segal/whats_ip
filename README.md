# Whats IP
==============================

Whats IP is a project to see how we can best work with text data to collect certain entities. We are going to first work with extracting names and IP addresses from a corpus. 
The detailed project description is to 

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   └── data           <- Scripts to download or generate data
    │       └── make_dataset.py
    │   
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


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

To instantiate a entity_classifier use an EntityClassifier and pass in the language and patterns that you are going to be searching for. 

ex: 
```python 
    # Create a set of regular expressions for IP addresses 
    ipv4_re = '^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$'
    ipv6_re = '^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){6}$'

    # Create the list of patterns to pass into 
    patterns = [
        {"label": "IP", "pattern": [{'TEXT': {"REGEX": ipv4_re}}]},
        {"label": "IP", "pattern": [{'TEXT': {"REGEX": ipv6_re}}]}
    ]

    # instantiate a entity_classifier object 
    entity_classifer = EntityClassifier(lang=en_core_web_sm, regex=patterns)

    # read a string from a file that has names and ip addresses
    doc = u'Bob found that 127.0.0.1 was bad and 123.4.5.6 was safe'

    # Get the entities from the document using the entity classifier 
    entities = [
        {ent.text: ent.label_}
        for ent in entity_classifier(doc).ents
    ]
```

## Tests 

There are tests written with unittests to check the functionality of the EntityClassifier class. These can be found within the entitiy classifier folder in the data folder. These tests can be run using 

## Solving environments

The environment for this project can be copied by creating an environment from the environment.yaml file using the command :
`conda env create --file environment.yaml` 

## Using the Entity Classifier

After solving for the environment it is time to use the EntityClassifier.
To see the entity classifier in action run the make_dataset.py file in ./src/data with the following arguments: 

`python ./src/data/make_dataset.py -p ./src/data/ip_address_rules.jsonl ./data/raw/ ./data/processed/entities.json` 

This will take all of the text files in the raw data folder and output the json file of all named entities that are either people or IP addresses