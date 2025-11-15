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
            raise TypeError("Author must be of type Author")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value
        
class Author:
    def __init__(self, name):
        self._name = None  
        self.name = name  
        
        self._articles = [] 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Name cannot be changed after instantiation")
        
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        
        self._name = value
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list({article.magazine for article in self._articles})
    
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article
    
    def topic_areas(self):
        if not self._articles:
            return None
        
        return list({article.magazine.category for article in self._articles})

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