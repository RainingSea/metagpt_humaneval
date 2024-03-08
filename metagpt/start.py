import sys
import os
import jsonlines

current_dir = os.getcwd()
sys.path.append(current_dir)

from software_company import generate_repo, ProjectRepo


def read_task_id_and_prompt(jsonl_file,k):
    task_ids_and_prompts = []
    index = 0
    with jsonlines.open(jsonl_file, "r") as reader:
        for obj in reader:
            task_id = obj.get("task_id", None)
            prompt = obj.get("prompt", None)
            if task_id is not None and prompt is not None:
                task_ids_and_prompts.append((task_id, prompt))
            index = index + 1
            if index == k:
                break
    return task_ids_and_prompts


if __name__ == "__main__":
    # info = '\ndef add_elements(arr, k):\n    """\n    Given a non-empty array of integers arr and an integer k, return\n    the sum of the elements with at most two digits from the first k elements of arr.\n\n    Example:\n\n        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4\n        Output: 24 # sum of 21 + 3\n\n    Constraints:\n        1. 1 <= len(arr) <= 100\n        2. 1 <= k <= len(arr)\n    """\n", "entry_point": "add_elements", "canonical_solution": "    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)\n", "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate([1,-2,-3,41,57,76,87,88,99], 3) == -4\n    assert candidate([111,121,3,4000,5,6], 2) == 0\n    assert candidate([11,21,3,90,5,6,7,8,9], 4) == 125\n    assert candidate([111,21,3,4000,5,6,7,8,9], 4) == 24, "This prints if this assert fails 1 (good for debugging!)"\n\n    # Check some edge cases that are easy to work out by hand.\n    assert candidate([1], 1) == 1, "This prints if this assert fails 2 (also good for debugging!)"\n\n'
    
    # 想要读多少条数据
    read_test_case_number = 15
    # 本次取的单个数据编号，0-163
    test_case_number = 10

    # 读取 prompt
    prompt = read_task_id_and_prompt("/home/molyer/project/metagpt/MetaGPT-0.7-humaneval/tests/humaneval/HumanEval.jsonl",
                                     read_test_case_number)[test_case_number]
    
    # 喂给 gpt，1 代表提取返回的 completion
    repo: ProjectRepo = generate_repo(prompt[1])  # or ProjectRepo("<path>")
    print(repo)  # it will print the repo structure with files
