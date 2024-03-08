import json
import jsonlines
import os

def create_jsonl_from_py(task_id, py_file_path,jsonl_file_path):
    
    with open(py_file_path, 'r') as file:
        py_content = file.read()

    data = {'task_id':"HumanEval/"+str(task_id),'completion': py_content}
    json_str = json.dumps(data)

    with open(jsonl_file_path, "a") as file:
        file.write(json_str + "\n")

if __name__ == "__main__" :
    create_jsonl_from_py(1,"/home/molyer/project/metagpt/MetaGPT-0.7-humaneval/tests/humaneval/gpt_pyfile.py",
                         "/home/molyer/project/metagpt/MetaGPT-0.7-humaneval/tests/humaneval/one.jsonl")
    
from typing import List
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    
    if not numbers:  
        return []
    interspersed_list = [numbers[0]]
    for number in numbers[1:]:
        interspersed_list.append(delimiter)  
        interspersed_list.append(number)     

    return interspersed_list


