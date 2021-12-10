class Tag:
    def __init__(self, tagname):
        self.tagname = tagname
        
    def __enter__(self):
        print('<{}').format(self.tagname)
    def __exit__(self):
        print('<{}').format(self.tagname)
        
        
html_tag = Tag('HTML')
body_tag = Tag('Body')

with html_tag:
    with body_tag:
        print("document contents")