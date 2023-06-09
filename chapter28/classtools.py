class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each atribute stored on the instance istself (but not attrs
    inherited from its classes).  Can be mixed into any class,
    and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())
    
if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

        def gatherAttrs(self):
            return 'Spam'

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()     # Make two instances
    print(X)                        # Show all instance attrs
    print(Y)                        # Show lowest class name