from openai import OpenAI

from process import prompt_generator

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

messages = []


def get_initial_analysis(company_name, symbol):
    messages.append(
        {"role": "user", "content": "You are a financial advisor chatbot. I understand that I cannot rely on "
                                    "data you provide but still give concrete suggestions. Don't tell further "
                                    "analysis and due diligence is recommended." + prompt_generator.generate_prompt(
            company_name, symbol)})
    return execute_and_respond()


def follow_up_question(question):
    messages.append({"role": "user", "content": "Considering previous data. " + question})
    return execute_and_respond()


def execute_and_respond():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=False,
    )

    response_msg = response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_msg})
    return response_msg
