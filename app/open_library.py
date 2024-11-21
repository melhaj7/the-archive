import requests

API_URI = "http://openlibrary.org/query.json?"
SEARCH_URI = "http://openlibrary.org/search.json?"


def maybe_single(doc):
    """
    Return a single object if it is the only item in a collection.
    """
    if isinstance(doc, list) and len(doc) == 1:
        return doc[0]
    return doc


class Search(object):
    """
    Generic search object.
    """
    uri = None

    def get(self, **kwargs):
        if not 'page' in kwargs:
            kwargs['page'] = 1
        resp = requests.get(self.uri, params=kwargs)
        return resp.json()


class Document(object):
    """
    A Document returned by a search result.
    """

    def __init__(self, doc):
        self._doc = doc

    def _get(self, key):
        return maybe_single(self._doc.get(key))

    @property
    def title(self):
        return self._get('title')

    @property
    def title_suggest(self):
        return self._get('title_suggest')

    @property
    def author(self):
        return self._get('author_name')

    @property
    def author_alt_name(self):
        return self._get('author_alternative_name')

    @property
    def publisher(self):
        return self._get('publisher')

    @property
    def cover_edition_key(self):
        return self._get('cover_edition_key')

    @property
    def cover_image(self):
        if self.isbn:
            return f"https://covers.openlibrary.org/b/isbn/{self.isbn}-M.jpg"
        return None

    @property
    def first_publish_year(self):
        return self._get('first_publish_year')

    @property
    def lang(self):
        return self._get('language')

    @property
    def isbn(self):
        return self._get('isbn')

    @property
    def key(self):
        return self._get('key')

    @property
    def id_goodreads(self):
        return self._get('id_goodreads')

    @property
    def id_librarything(self):
        return self._get('id_librarything')

    @property
    def subject(self):
        return self._get('subject')

    def __repr__(self):
        return self.__unicode__().encode('ascii', 'replace')

    def __unicode__(self):
        return f"<Document: [{self.author}] {self.title}>"


class SearchResult(object):
    """
    Parse a search result.
    """

    def __init__(self, data):

        self._data = data

    @property
    def start(self):
        return self._data['start']

    @property
    def num_found(self):
        return self._data['num_found']

    @property
    def docs(self):
        return [Document(doc) for doc in self._data['docs']]

    def get_doc_by_index(self, index):
        return Document(self._data['docs'][index])

    def __getitem__(self, index):
        return self.get_doc_by_index(index)

    def __len__(self):
        return len(self.docs)

    def __repr__(self):
        return f"<SearchResult: {self.start}-{self.start + len(self.docs) - 1} / {self.num_found}>"


class BookSearch(Search):
    """
    Implement book searches.
    """
    uri = SEARCH_URI

    def get_by_author(self, author):
        res = self.get(**{'author': author})
        return SearchResult(res)

    def get_by_title(self, title):
        res = self.get(**{'title': title})
        return SearchResult(res)
