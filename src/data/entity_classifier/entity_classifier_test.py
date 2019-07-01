import unittest
from entity_classifier import EntityClassifier
from spacy.pipeline import EntityRuler


class TestEntityClassifier(unittest.TestCase):

    def test_accept_file(self):
        # Check to make sure that entity_classifier accepts file for pattern
        # input
        pattern_file = 'src/data/ip_address_rules.jsonl'
        entity_classifier = EntityClassifier(regex=pattern_file)
        self.assertIsInstance(entity_classifier.regex, EntityRuler)

    def test_accept_list(self):
        # Check to make sure that entity_classifier accepts list for pattern
        # input
        patterns = [{
            "label": "GPE", "pattern": [
                {"lower": "san"},
                {"lower": "francisco"}
            ]
        }]
        entity_classifier = EntityClassifier(regex=patterns)
        self.assertIsInstance(entity_classifier.regex, EntityRuler)

    def test_person(self):
        entity_classifier = EntityClassifier()
        doc = u'Brandon Segal wrote this script'
        entities = entity_classifier.get_entities(doc).ents
        results = [{ent.text: ent.label_} for ent in entities]
        self.assertListEqual([{'Brandon Segal': 'PERSON'}], results)


if __name__ == '__main__':
    unittest.main()
