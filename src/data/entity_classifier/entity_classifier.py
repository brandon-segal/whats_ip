import spacy
from spacy.pipeline import EntityRuler
import re


class EntityClassifier:
    def __init__(self, lang='en_core_web_sm', regex=[]):
        self.model = spacy.load(lang)
        self.regex = regex

    @property
    def regex(self):
        return self._ruler

    @regex.setter
    def regex(self, value):
        if value is not None:
            if type(value) == list or type(value) == dict:
                self._ruler = EntityRuler(self.model)
                self._ruler.add_patterns(value)
            else:
                self._ruler = EntityRuler(self.model).from_disk(value)
            self.model.add_pipe(self._ruler, before='ner')

    def get_entities(self, doc):
        doc = self.model(doc)
        return doc


def main():
    tests = [
        'Bob found that 127.0.0.1 was bad and 123.4.5.6 was safe',
        'Brandon Segal found that 127.0.0.1.1.1 was bad and 123.4.5.6.2.3\
         was safe'
    ]
    ipv4_re = '^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$'
    ipv6_re = '^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){6}$'
    patterns = [
        {"label": "IP", "pattern": [{'TEXT': {"REGEX": ipv4_re}}]},
        {"label": "IP", "pattern": [{'TEXT': {"REGEX": ipv6_re}}]}
    ]
    create_rules_file(patterns, tests)


def create_rules_file(patterns, tests):
    entity_classifier = EntityClassifier(regex=patterns)
    for test in tests:
        entity_classifier.get_entities(test)
    entity_classifier._ruler.to_disk('../ip_address_rules.json')

if __name__ == "__main__":
    main()
