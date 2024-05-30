from dotenv import load_dotenv

from prompt import juryPrompt
load_dotenv()

from openai import OpenAI
import os

llm = OpenAI()
models = os.getenv("MODELS").split(",")

print("------------------")
print(f"Available models: {models}")
print("------------------")

def run_jury(model, question, answerA, answerB):
    result = llm.chat.completions.create(
        model=model,
        messages=juryPrompt(question, answerA, answerB)
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

def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("Question")
    question = input()
    print("--------")
    print("Model A:")
    input_model_a = get_multiline_input("Enter Model A input (end with an empty line):")
    print("--------")
    print("Model B:")
    input_model_b = get_multiline_input("Enter Model B input (end with an empty line):")
    print("--------")

    results = []
    for model in models:
        result = run_jury(model, question, input_model_a, input_model_b)
        print(f"Model {model} wins: {result}")
        results.append(result)

    counts = {
        "A": results.count("A"),
        "B": results.count("B"),
        "Tie": results.count("Tie")
    }

    overall_winner = max(counts, key=counts.get)
    if counts["A"] == counts["B"]:
        overall_winner = "Tie"

    print("--------")
    print(f"Overall result: {overall_winner}")
    print("--------")



if __name__ == '__main__':
    main()
