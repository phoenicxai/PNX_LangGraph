# Filename: KnowledgeRepository.py
from threading import Lock

class KnowledgeRepository:
    def __init__(self):
        self.repository = {}
        self.lock = Lock()  # Correctly importing and using Lock for concurrency control

    def store_knowledge(self, key, knowledge):
        with self.lock:
            # Assuming knowledge is structured as a dict containing various pieces of information
            self.repository[key] = knowledge

    def retrieve_knowledge(self, key):
        with self.lock:
            return self.repository.get(key, None)

    def search_knowledge(self, search_criteria):
        # search_criteria could be a lambda or function that filters knowledge based on certain conditions
        with self.lock:
            return [k for k, v in self.repository.items() if search_criteria(v)]