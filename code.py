Code Snippet:
python
Copy code
class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, text):
        words = text.lower().split()
        for word in words:
            if word not in self.index:
                self.index[word] = []
            if doc_id not in self.index[word]:
                self.index[word].append(doc_id)

    def search(self, query):
        query_words = query.lower().split()
        results = []
        for word in query_words:
            if word in self.index:
                results.append(self.index[word])
        return results if results else "No documents found"
