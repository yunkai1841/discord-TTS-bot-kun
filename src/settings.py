import json

import status

def get_token(debug=False):
    with open(file=r"settings/token.json") as f:
        tokens = json.load(f)
        
        if debug:
            print(tokens)

        return tokens
