import openai
#API key
openai.api_key = ""

def writing_assistant(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

while True:
    user_input = input("Enter your writing prompt: ")
    response = writing_assistant(user_input)
    print("Writing Assistant: " + response)
