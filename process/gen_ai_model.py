from openai import OpenAI

from process import prompt_generator

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="<api-key>",
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


def get_initial_analysis(company_name, symbol):
    clear_message_thread()
    messages.append({"role": "user", "content": prompt_generator.generate_prompt(company_name, symbol)})
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


def clear_message_thread():
    messages.clear()
