from openai import OpenAI

from process import prompt_generator
from util import secrets_util


client = OpenAI(
    api_key=secrets_util.get_openai_api_key(),
)

messages = []


def chat(message):
    if "@@clear" in message:
        clear_message_thread()
        return "Model has been resetted"
    elif "@@" in message:
        company_info = message.split("@@")
        return get_initial_analysis(company_info[0], company_info[1])
    else:
        return follow_up_question(message)


def get_initial_analysis(company_name, symbol, live=True):
    clear_message_thread()
    messages.append({"role": "system", "content": "You are a Financial Analyst. You have to analyze financial data of "
                                                  "a company and suggest investment strategy for that company. You "
                                                  "only have to answer in context to the specified company."})
    messages.append({"role": "user", "content": prompt_generator.generate_prompt(company_name, symbol, live)})
    return execute_and_respond()


def follow_up_question(question):
    messages.append({"role": "user", "content": "(Only Consider Previous Data) " + question})
    return execute_and_respond()


def execute_and_respond():
    print(messages)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=False,
    )

    response_msg = response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_msg})
    return response_msg


def clear_message_thread():
    messages.clear()

