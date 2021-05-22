import json
    
def build_tree(input_json):
    categories = json.loads(input_json)
    tree = []
    parents = []
    level = "root"
    while level != "leaf":
        while level == "root":
            root = next((i for i, category in enumerate(categories) if category["parent_id"] == None), None)
            if root is not None:
                parents.append(categories[root]["id"])
                tree.append(categories[root])
                del categories[root]
            else:
                level = "children"
        while level == "children":
            child = next((i for i, category in enumerate(categories) if category["parent_id"] in parents), None)
            if child is not None:
                parents.append(categories[child]["id"])
                tree.append(categories[child])
                del categories[child]
            else:
                level = "leaf"
    return json.dumps(tree)

if __name__ == "__main__":
    input_json = json.dumps([
      {
        "name": "Accessories",
        "id": 1,
        "parent_id": 20,
      },
      {
        "name": "Watches",
        "id": 57,
        "parent_id": 1
      },
      {
        "name": "Men",
        "id": 20,
        "parent_id": None
      }
    ])
    
    print(build_tree(input_json)) 
