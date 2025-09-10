import json

class IQP:
    def __init__(self, summary, lexical_terms, bug_category, semantic_vector=None):
        self.summary = summary
        self.lexical_terms = lexical_terms
        self.bug_category = bug_category
        self.semantic_vector = semantic_vector

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)
