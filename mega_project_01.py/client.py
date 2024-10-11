from openai import OpenAI
67
client=OpenAI(api_key="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")
completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a virtual assistant named jarvis skilled in general tasks"},
        {"role":"user","content":"what is coding"}
    ]
)
print(completion.choices[0].message)
'''
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion['choices'][0]['message']['content'])
'''