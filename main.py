import textwrap
import pathlib
import google.generativeai as genai
from IPython.display import display

def model_gemini(name):
    # setup api model
    genai.configure(api_key=API KEY)

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro')

    while True:
        input_user = input("masukkan prompt:")
        response = model.generate_content(input_user)
        print(response.text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    model_gemini('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
