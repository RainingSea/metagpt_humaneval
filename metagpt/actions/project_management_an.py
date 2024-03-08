#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/12/14 15:28
@Author  : alexanderwu
@File    : project_management_an.py
"""
from typing import List

from metagpt.actions.action_node import ActionNode
from metagpt.logs import logger

REQUIRED_PYTHON_PACKAGES = ActionNode(
    key="Required Python packages, only suggest",
    expected_type=List[str],
    instruction="Only packages from the Python standard library are allowed to be suggested.",
    example=["typing, sys"],
)

REQUIRED_OTHER_LANGUAGE_PACKAGES = ActionNode(
    key="do not suggest third-party packages",
    expected_type=List[str],
    instruction="do not suggest third-party packages",
    example=["do not suggest third-party packages"],
)

LOGIC_ANALYSIS = ActionNode(
    key="Logic Analysis",
    expected_type=List[List[str]],
    instruction="Provide only one file with the function to be implemented"
    "including dependency analysis and imports.",
    example=[
        ["function.py", "implement the disired function based on the description"],
    ],
)

REFINED_LOGIC_ANALYSIS = ActionNode(
    key="Refined Logic Analysis",
    expected_type=List[List[str]],
    instruction="Review and refine the logic analysis by merging the Legacy Content and Incremental Content. "
    "Include dependency analysis, consider potential impacts on existing code, and document necessary imports.",
    example=[
        ["function.py", "implement the disired function based on the description"],
    ],
)

TASK_LIST = ActionNode(
    key="task list",
    expected_type=List[str],
    instruction="generate only one file with the function to be implemented",
    example=["function.py"],
)

REFINED_TASK_LIST = ActionNode(
    key="task list",
    expected_type=List[str],
    instruction="generate only one file with the function to be implemented",
    example=["funcion.py"],
)

FULL_API_SPEC = ActionNode(
    key="Full API spec",
    expected_type=str,
    instruction="Describe all APIs using OpenAPI 3.0 spec that may be used by both frontend and backend. If front-end "
    "and back-end communication is not required, leave it blank.",
    example="openapi: 3.0.0 ...",
)

SHARED_KNOWLEDGE = ActionNode(
    key="Shared Knowledge",
    expected_type=str,
    instruction="Detail any shared knowledge, like common utility functions or configuration variables.",
    example="`game.py` contains functions shared across the project.",
)

REFINED_SHARED_KNOWLEDGE = ActionNode(
    key="Refined Shared Knowledge",
    expected_type=str,
    instruction="Update and expand shared knowledge to reflect any new elements introduced. This includes common "
    "utility functions, configuration variables for team collaboration. Retain content that is not related to "
    "incremental development but important for consistency and clarity.",
    example="`new_module.py` enhances shared utility functions for improved code reusability and collaboration.",
)


ANYTHING_UNCLEAR_PM = ActionNode(
    key="Anything UNCLEAR",
    expected_type=str,
    instruction="Mention any unclear aspects in the project management context and try to clarify them.",
    example="Clarification needed on how to start and initialize third-party libraries.",
)

NODES = [
    REQUIRED_PYTHON_PACKAGES,
    REQUIRED_OTHER_LANGUAGE_PACKAGES,
    LOGIC_ANALYSIS,
    TASK_LIST,
    FULL_API_SPEC,
    SHARED_KNOWLEDGE,
    ANYTHING_UNCLEAR_PM,
]

REFINED_NODES = [
    REQUIRED_PYTHON_PACKAGES,
    REQUIRED_OTHER_LANGUAGE_PACKAGES,
    REFINED_LOGIC_ANALYSIS,
    REFINED_TASK_LIST,
    FULL_API_SPEC,
    REFINED_SHARED_KNOWLEDGE,
    ANYTHING_UNCLEAR_PM,
]

PM_NODE = ActionNode.from_children("PM_NODE", NODES)
REFINED_PM_NODE = ActionNode.from_children("REFINED_PM_NODE", REFINED_NODES)


def main():
    prompt = PM_NODE.compile(context="")
    logger.info(prompt)
    prompt = REFINED_PM_NODE.compile(context="")
    logger.info(prompt)


if __name__ == "__main__":
    main()
