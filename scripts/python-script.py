import json
import sys
from sklearn.pipeline import make_pipeline #you can import and use any of installed pip libs

def first_function():
    json_obj = open(sys.argv[2])
    data = json.load(json_obj)
    calculatedResults = [1,2,4,3] # it is just example of data to return, in fact you will calculate it bellow
    X = data["X"]
    y = data["y"]
    # do some your calculations based on X and y and put the result to the calculatedResults
    # print(make_pipeline)
    json_object_result = json.dumps(calculatedResults, indent=4)

    with open(sys.argv[3], "w") as outfile:
        outfile.write(json_object_result)
    print("OK")


if sys.argv[1] == 'first_function':
    first_function()

sys.stdout.flush()