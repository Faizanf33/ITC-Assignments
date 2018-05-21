## IMPORTS GO HERE if required

## END OF IMPORTS


#### YOUR CODE FOR uniqueEntries GOES HERE ####
def uniqueEntries(n):
    """Function 'uniqueEntries' that takes a filled list/string and returns a list of its unique entries and
    duplicate entries
	"""
    uv, dI = [] , []

    for i in n:
        if (i in uv):
            dI.append(i)
        else:
            uv.append(i)
    return uv,dI

#### End OF MARKER ----uniqueEntries
