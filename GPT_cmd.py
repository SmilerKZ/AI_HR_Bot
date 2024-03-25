from openai import OpenAI

def GPT_cmd_fcn(GPT_cmd):

    # Initializtion to ChatGPT API
    client = OpenAI(api_key='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')

    # Command ChatGPT to generate an individual invitation
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                # "content": cmd_GPT+CV_text,
                "content": GPT_cmd,
            },
        ],
    )

    return completion.choices[0].message.content