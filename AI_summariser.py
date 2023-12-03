from get_response import get_basic_response

def summariser(input_text):
    messages = [
        {
            "role" : "system" , "content" : "you are a very good summariser. your job is to accurately summarise the given input by the user. "
        },
        {
            "role" : "system","content" : input_text
        }

    ]

    summary = get_basic_response(messages)

    return summary