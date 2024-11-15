from openai import OpenAI
client = OpenAI()

# https://platform.openai.com/docs/guides/structured-outputs/examples


def score_article(content):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You will receive data from financial news source. Analyze the data and determine from the tone, the urgency and overall sentiment in raport to human speech of those news the impact it could potentially have on the market on a scale from -20 to 20, -20 being very damaging for the currency and 20 very good, while 0 is neutral. This should be done to the currecies mentioned and/or affected by those news. Write the scores for each currency in a json object. For each currency score, only output the number for the abbreviation of the currency. example: {'AUD' : -15}"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{content}"
                    }
                ]
            }
        ],
        temperature=0,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "json_object"
        }
    )
    return response.choices[0].message.content
    # print(response.choices[0].message)
