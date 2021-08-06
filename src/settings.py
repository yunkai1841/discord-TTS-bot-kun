import json

import status

def get_token(debug=False):
    with open(file=r"setting/token.json") as f:
        tokens = json.load(f)
        
        if debug:
            print(tokens)

        return tokens
