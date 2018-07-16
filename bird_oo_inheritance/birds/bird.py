class Bird(object):
    kind = ''
    call = ''
    
    def __init__(self, the_kind, the_call):
        self.kind = the_kind
        self.call = the_call
        
    def get_description(self):
        return "the {0} goes {1}".format(self.kind, self.call)
        
class Seabird(Bird):
    diving_depth = 0
    
    def __init__(self, the_kind, the_call, the_diving_depth):
        super(Seabird,self).__init__(the_kind, the_call)
        self.diving_depth = the_diving_depth
    
    def get_description(self):
        return super(Seabird, self).get_description() + " and dives to a depth of {0}m".format(self.diving_depth)
    