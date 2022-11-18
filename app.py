# import numpy as np
from flask import Flask, request, jsonify, render_template

# # Transformer Imports
from transformers import AutoTokenizer
import pickle

model = pickle.load(open('mai_model.pkl', 'rb'))
# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")


app = Flask("__name__")



q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/predict", methods=['POST'])
def predict():
    
    # inputQuery1 = request.form['query1']
    # inputQuery2 = request.form['query2']
    # inputQuery3 = request.form['query3']
    # inputQuery4 = request.form['query4']
    # inputQuery5 = request.form['query5']

    # model = pickle.load(open("model.sav", "rb"))
    
    
    # data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5]]
    # new_df = pd.DataFrame(data, columns = ['texture_mean', 'perimeter_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean'])
    
    # single = model.predict(new_df)
    # probablity = model.predict_proba(new_df)[:,1]
    
    # if single==1:
    #     o1 = "The patient is diagnosed with Breast Cancer"
    #     o2 = "Confidence: {}".format(probablity*100)
    # else:
    #     o1 = "The patient is not diagnosed with Breast Cancer"
    #     o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1="I AM RUNNING")
    
if __name__ == "__main__":
    app.run()
# @app.route('/reply', methods=['GET'])
# @app.route('/reply', methods=['GET'])
# def reply():
    
#     data = request.get_json(force=True) 
#     new_user_input_ids = tokenizer.encode(data["data"] + tokenizer.eos_token, return_tensors='pt')

#     bot_input_ids = new_user_input_ids

#     chat_history_ids = model.generate(
#         bot_input_ids, max_length=200,
#         pad_token_id=tokenizer.eos_token_id,  
#         no_repeat_ngram_size=3,       
#         do_sample=True, 
#         top_k=100, 
#         top_p=0.7,
#         temperature = 0.8
#     )

#     x = "{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))
#     x = "I am Running"

#     return render_template("home.html", output=x)

# if __name__ == "__main__":
#     app.run()
