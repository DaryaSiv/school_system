# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_lesson(topic):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "Ты помощник школьного учителя. Создавай краткие и понятные материалы по школьным темам."},
#             {"role": "user", "content": f"Составь краткий теоретический материал и 3 задания по теме: {topic}"}
#         ]
#     )
#     return response["choices"][0]["message"]["content"]