from openai import OpenAI
import os

OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


def checkMessage(text):
    try:
        client = OpenAI()
        chat_completion = client.chat.completions.create(
            model='gpt-3.5-turbo',  # or 'gpt-3.5-turbo' depending on your preference
            messages=[
                {"role": "system", "content": "The following is a message that needs to be classified as either appropriate or inappropriate (violent, harassing, sexually explicit):"},
                {"role": "user", "content": text}
            ]
        )
        result = chat_completion.choices[0].message.content
        if "inappropriate" in result.lower():
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
text_to_check = "i love your dick"
result = checkMessage(text_to_check)
print(result)
