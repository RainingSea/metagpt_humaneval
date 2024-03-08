import sys
import jsonlines

sys.path.append("/home/molyer/project/metagpt/MetaGPT-0.7-humaneval/")

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
    repo: ProjectRepo = generate_repo("Design a centered music concert landing page within the entire page height. Include a rectangular image on the right with a height of 400px and a golden ratio aspect ratio sourced from Unsplash. The left side should have an area of the same size as the image, displaying the concert's theme and description, along with a button for ticket acquisition. Ensure the overall layout is centered both vertically and horizontally, making the entire webpage height equal to the page height. No need to implement backend logic, just design a static webpage. Please note that apart from the theme description, ticket acquisition button, and image, do not generate any other elements. try to use only simple javascript, do not use any typescript code")  # or ProjectRepo("<path>")
    # info = '\ndef add_elements(arr, k):\n    """\n    Given a non-empty array of integers arr and an integer k, return\n    the sum of the elements with at most two digits from the first k elements of arr.\n\n    Example:\n\n        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4\n        Output: 24 # sum of 21 + 3\n\n    Constraints:\n        1. 1 <= len(arr) <= 100\n        2. 1 <= k <= len(arr)\n    """\n", "entry_point": "add_elements", "canonical_solution": "    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)\n", "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate([1,-2,-3,41,57,76,87,88,99], 3) == -4\n    assert candidate([111,121,3,4000,5,6], 2) == 0\n    assert candidate([11,21,3,90,5,6,7,8,9], 4) == 125\n    assert candidate([111,21,3,4000,5,6,7,8,9], 4) == 24, "This prints if this assert fails 1 (good for debugging!)"\n\n    # Check some edge cases that are easy to work out by hand.\n    assert candidate([1], 1) == 1, "This prints if this assert fails 2 (also good for debugging!)"\n\n'
    
    # prompt = read_task_id_and_prompt("/home/molyer/project/metagpt/MetaGPT-0.7-humaneval/tests/humaneval/HumanEval.jsonl",15)[10]
    
    # repo: ProjectRepo = generate_repo(prompt[1])  # or ProjectRepo("<path>")
    print(repo)  # it will print the repo structure with files
