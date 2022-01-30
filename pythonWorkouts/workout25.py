def myxml(tagname, content='bar', **kwargs):
    """Takes one required parameter as the tag type, 
    one optional parameter as the content, and as 
    many as required keyword paramters as attributes.
    Returns a string in xml form."""

    attr_list = [f' {key}="{value}"' for key, value in kwargs.items()]
    attr_str = ''.join(attr_list)
    return f'<{tagname}{attr_str}>{content}</{tagname}>'

print(myxml('tagname', a="v", b=2, c=3))