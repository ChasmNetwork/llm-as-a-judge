default_score_rubric = "helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses"

def pairwise_prompt(model: str, question: str, answer_a: str, answer_b: str, score_rubric: str = default_score_rubric):
    # https://github.com/prometheus-eval/prometheus-eval/blob/main/eval/prompts.py
    if "prometheus2" in model:
        return [
            {
                "role": "system",
                "content": f"""###Task Description:
An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of two responses strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, choose a better response between Response A and Response B. You should refer to the score rubric.
3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (A or B)"
4. Please do not generate any other opening, closing, and explanations.

###Instruction:
{question}

###Response A:
{answer_a}

###Response B:
{answer_b}

###Score Rubric:
{score_rubric}

###Feedback: 
"""
            }
        ]

    return [
        {
            "role": "system",
            "content": """Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. 

After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie.""",
        },
        {
            "role": "user",
            "content": f"""[User Question]
{question}
[The Start of Assistant A’s Answer]
{answer_a}
[The End of Assistant A’s Answer]
[The Start of Assistant B’s Answer]
{answer_b}
[The End of Assistant B’s Answer]
""",
        },
    ]

def direct_assessment_prompt(model: str, question: str, answer: str, score_rubric = default_score_rubric):

    if "prometheus2" in model:
        return [
            {
                "role": "system",
                "content": f"""###Task Description:
An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)"
4. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate:
{question}

###Response to evaluate:
{answer}

###Score Rubrics:
{score_rubric}

###Feedback:"""
            }
        ]

    return [
        {
            "role": "system",
            "content": """You are a fair judge assistant tasked with providing clear, objective feedback based on specific criteria, ensuring each assessment reflects the absolute standards set for performance.
Task Description:
An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
3. The output format should look as follows:
"Feedback: (write a feedback for criteria)
[RESULT] (an integer number between 1 and 5)"
4. Please do not generate any other opening, closing, and explanations.
""",
        }, {
            "role": "system",
            "content": f"""###The instruction to evaluate:
{question}

###Response to evaluate:
{answer}

###Score Rubrics:
{score_rubric}

###Feedback:
"""

        }
    ]