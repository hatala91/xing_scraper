
class Interest:
    title = None
    
    def __init__(self, title = None):
        self.title = title.decode('utf-8')
    
    def __repr__(self):
        return self.title

class Accomplishment:
    title = None
    
    def __init__(self, title = None):
        self.title = title.decode('utf-8')
    
    def __repr__(self):
        return self.title


class Organisation:
    title = None
    
    def __init__(self, title = None):
        self.title = title.decode('utf-8')
    
    def __repr__(self):
        return self.title

class Qualification:
    title = None
    
    def __init__(self, title = None):
        self.title = title.decode('utf-8')
    
    def __repr__(self):
        return self.title

class Scraper(object):
    driver = None

    def __find_element_by_class_name__(self, class_name):
        try:
            self.driver.find_element_by_class_name(class_name)
            return True
        except:
            pass
        return False


