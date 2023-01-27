import openai
import pandas as pd

# Set up your OpenAI API key
openai.api_key = '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'

# Define your data
data = pd.read_csv('P9.csv')


crust = "Year of Tetris"

def answer_question(data,crust):
    # Use the OpenAI API to generate answers based on the PDF and the question
    prompt = (f"{crust} according to {data}")
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )
    return completions["choices"][0]["text"]
# Use the fine-tuned model to generate text
ans = answer_question(data, crust)
print(ans)