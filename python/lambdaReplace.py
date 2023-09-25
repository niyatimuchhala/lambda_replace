import json
import re

REPLACE_PATH = "/replace"
REGEX_REPLACEMENTS = [
    (r"abn", "ABN AMRO"),
    (r"ing", "ING Bank"),
    (r"rabo", "Rabobank"),
    (r"triodos", "Triodos Bank"),
    (r"volksbank", "de Volksbank"),
]   

def lambda_handler(event, context):
    print(event)
    if event['resource'] == REPLACE_PATH:
        str = json.loads(event['body'])
        if "input" in str:
            a = str["input"]
            print(a)
            for old, new in REGEX_REPLACEMENTS:
                a = re.sub(old, new, a, flags=re.IGNORECASE)
            return{
                'statusCode' : 201,
                'body': json.dumps(a)
            }
        return{
            'statusCode' : 400,
            'body': json.dumps("Bad request")
        }