class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author.articles.append(self)
        magazine.articles.append(self)

    @property
    def title(self):
        return self._title
    

    @title.setter
    def title(self, value):
        # Check if title has already been set (immutable after first set)
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Title cannot be changed after instantiation")
        
        # Validate title type and length
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self._title = value


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class.")
        self._author = value
        
class Author:
    def __init__(self, name):
        self.name = None
        self.name = name
        self.articles = []


    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass