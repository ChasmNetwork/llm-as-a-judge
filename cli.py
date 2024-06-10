from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
import os
from main import run_jury

models = os.getenv("MODELS").split(",")
print("------------------")
print(f"Available models: {models}")
print("------------------")

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
    llm = OpenAI()
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
        result = run_jury(llm, model, question, input_model_a, input_model_b)
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
