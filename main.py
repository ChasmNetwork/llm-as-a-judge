from prompt import juryPrompt

def run_jury(llm, model: str, question: str, answer_a: str, answer_b: str):
    """
    Runs the jury simulation using the given language model (llm) and model name.
    
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
        messages=juryPrompt(question, answer_a, answer_b)
    )
    content = result.choices[0].message.content
    print("--------")
    print("Model", model, ":", content)
    if("[[A]]" in content and "[[B]]" in content):
        return "Tie"
    if ("[[A]]" in content):
        return "A"
    elif ("[[B]]" in content):
        return "B"
    elif ("[[C]]" in content):
        return "Tie"
