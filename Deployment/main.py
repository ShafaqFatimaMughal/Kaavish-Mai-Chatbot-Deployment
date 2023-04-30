# import numpy as np
from flask import Flask, request, jsonify, render_template

# # Transformer Imports
from transformers import AutoTokenizer
import pickle
import time

model = pickle.load(open('mai_model.pkl', 'rb'))
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")

app = Flask(__name__)

@app.route("/reply", methods=['POST'])
def predict():

    data = request.get_json(force=True) 
    token_start = time.time()
    new_user_input_ids = tokenizer.encode(data["data"] + tokenizer.eos_token, return_tensors='pt')
    token_end = time.time()
    bot_input_ids = new_user_input_ids

    gen_start = time.time()
    chat_history_ids = model.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizer.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=100, 
        top_p=0.7,
        temperature = 0.8
    )
    gen_end = time.time()

    print("Tokenizer Time:", token_end - token_start, ", Generate_time:", gen_end - gen_start)
    x = "{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))

    return jsonify({"data":x})


@app.route("/greeting", methods=['GET'])
def greeting():
    return jsonify({"data": 'Hello! I am Mai. I have knowledge about the menstrual cycle, how to manage it properly, how to manage hygiene, as well as knowledge about menstrual products. Feel free to ask me questions about any of these topics. After sending a question, wait for the response before sending your next question. If you feel that my response to your query is incorrect, please fill out the feedback. I am still learning, so please be patient with me.'})
if __name__ == "__main__":
    app.run()