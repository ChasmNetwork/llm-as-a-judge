from prompt import direct_assessment_prompt, pairwise_prompt 

def run_direct_assessment(llm, model: str, question: str, answer: str):
    """
    Runs the direct assessment of an answer
    """

    result = llm.chat.completions.create(
        model=model,
        messages=direct_assessment_prompt(model, question, answer),
    )

    return result.choices[0].message.content

def run_pairwise(llm, model: str, question: str, answer_a: str, answer_b: str):
    """
    Runs the pairwise comparison of 2 answer
    
    Args:
        llm (LanguageModel): The language model used for generating responses.
        model (str): The name of the model to use for generating responses.
        question (str): The question to ask the jury.
        answer_a (str): The first answer option for the jury.
        answer_b (str): The second answer option for the jury.
    
    Returns:
        str: The result of the jury simulation. Possible values are 'A', 'B', or 'Tie'.
    """
    result = llm.chat.completions.create(
        model=model,
        messages=pairwise_prompt(model, question, answer_a, answer_b)
    )
    content = result.choices[0].message.content
    print(content)

    print("--------")
    print("Model", model, ":", content)

    if "prometheus2" in model:
        result = content.split("[RESULT]")
        return result[1].strip()

    if("[[A]]" in content and "[[B]]" in content):
        return "Tie"
    if ("[[A]]" in content):
        return "A"
    elif ("[[B]]" in content):
        return "B"
    elif ("[[C]]" in content):
        return "Tie"
