import streamlit as st
import openai

st.title("Thoại Soup Tích hợp chat gpt vào ứng dụng")

model = "text-davinci-003"

with open("apiKey.txt", "r") as f:
    openai.api_key = f.readline() # Lấy apiKey từ file txt

#Hàm gọi api gpt để xử lý
def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(
        engine = model,
        prompt = user_question,
        max_tokens = 1024,
        n = 1,
        temperature = 0.5
    )
    response_text = response.choices[0].text
    return response_text

# Khởi tạo giao diện
def main():
    user_question = st.text_input("Nhập câu hỏi vào đây...")
    if st.button("Hỏi"):
        response_text = get_response_from_chatgpt((user_question))
        return st.write(f"Soup trả lời: {response_text}")
main()