# %%

import json
# a Python object (dict):
Customer = {
    "cust1": {
        "name": "Derry",
        "member": 1
    },
    "cust2": {
        "name": "Angga",
        "member": 0
    },
    "cust3": {
        "name": "Lilis",
        "member": 1
    }
}

# convert into JSON:
y = json.dumps(Customer)

# the result is a JSON string:
print(y)

# %%
