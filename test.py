#pip install openai
#pip install zhconv
import openai
import zhconv


with open("test.mp3","rb") as audio_file:
    openai.api_key = ""
    model_id="whisper-1"
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    word=str(transcript['text'].replace(' ',"\n"))
    word1=zhconv.convert(word,"zh-tw")


with open('mp3_to_text.txt', 'w', encoding='utf-8') as f:
    f.write(word1)


word2='請將"'+word1+'"延伸成一篇500字的文章'
#word2='請將"'+word1+'"濃縮成一篇150字的大綱'

user_prompt = {}
user_prompt['role'] = 'user'
user_prompt['content'] = word2
messages = []
messages.append({"role": "assistant", "content": "你是一位助理"})
messages.append(user_prompt)
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages,
                                        n=2,
                                        temperature=0.2)
ai_answer1 = response["choices"][0]["message"]["content"]
ai_answer2 = response["choices"][1]["message"]["content"]
ai_answer = "回覆一:" + ai_answer1 + "\n\n回覆二:" + ai_answer2

with open('answer.txt', 'w', encoding='utf-8') as f:
    f.write(ai_answer)
