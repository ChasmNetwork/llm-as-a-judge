# LLM as a judge

A quick CLI tool to test whether an LLM outperform another LLM based on the paper [LLM-as-a-judge method](https://arxiv.org/abs/2306.05685v4).

## Installation

1. Install all the libraries
```
pip install -r requirements.txt
```

2. Setup .env
```
cp .env.sample .env
```

by default it's using OLLAMA to run the judge work.

3. Run the code
```
python main.py
```

The CLI will ask the question and response of LLM A and LLM B, and then will run the benchmark using MODELS as jury.