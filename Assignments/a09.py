## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(dict):
    type_of_doc = []

    if dict == {}:
        return []

    for doc in dict:
        type_of_doc += [doc]

    return type_of_doc
#### End OF MARKER

### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types_counts(dict):
    doc_type_count = {}

    for doc in dict:
        sum = len(dict[doc])
        doc_type_count[doc] = sum

    return doc_type_count
#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(dict, auth, doc_type=None):
    if dict == {}:
        return 0

    author_count = 0
    if doc_type:
        for type in doc_type:
            for detail in dict[type]:
                for deep in detail:
                    if deep == "author":
                        for auth_det in detail[deep].values():
                            if auth_det == auth:
                                author_count += 1


    else:
        for doc in dict:
            for detail in dict[doc]:
                for deep in detail:
                    if deep == "author":
                        for auth_det in detail[deep].values():
                            if auth_det == auth:
                                author_count += 1

    return author_count
#### End OF MARKER


if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print get_types(d)
    print get_types_counts(d)
    print get_author_count(d, 'cap')

    print get_author_count(d, 'jake', ['articles', 'tweets'])
