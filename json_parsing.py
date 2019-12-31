import json
# %%
# a Python object (dict):
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# convert into JSON:
y = json.dumps(myfamily)

# the result is a JSON string:
print(y)


# %%
