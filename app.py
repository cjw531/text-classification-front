import streamlit as st
import requests

def send_request(text, type):
    files = {
        'text': (None, text),
        'type': (None, type),
    }
    response = requests.post('https://main-text-classification-server-cjw531.endpoint.ainize.ai/predict', files=files)
    status_code = response.status_code

    return status_code, response


st.title("Performance Comparison of Binary and Multi Class Text Classification Models With CNN & BERT + CNN Models")

# col1, col2 = st.columns(2) # set up 2 columns

st.header("Binary Classification") # binary classification section
st.markdown("The pre-trained binary classification CNN and BERT + CNN models will classify whether it is a disaster-related Tweets or not.")

binary_base_text = st.text_input("Type Disaster or Non-Disaster Tweets", "Last week, around 21 people were assasinated in Texas due to mass shooting.")
if st.button("Predict Binary"):
    text = binary_base_text.title()
    status_code, response = send_request(text, "1")
    print(status_code)
    print(response)
    if status_code == 200:
        prediction = response.json()
        st.success(prediction["CNN prediction"] + '\t' + prediction['BERT prediction'])
    else:
        st.error(str(status_code) + " Error")

st.markdown("""---""")

st.header("Multi Classification")
st.markdown("The pre-trained multiclass classification CNN and BERT + CNN models will classify the news article into 7 categories: \
    'automobile', 'entertainment', 'politics', 'science', 'sports', 'technology', 'world'")

multi_base_text = st.text_input("Type News Article to Classify", "Joe Biden recently visited South Korea and then he headed to Japan.")
if st.button("Predict Multi"):
    text = multi_base_text.title()
    status_code, response = send_request(text, '2')
    if status_code == 200:
        prediction = response.json()
        st.success(prediction["CNN prediction"] + '\t' + prediction['BERT prediction'])
    else:
        st.error(str(status_code) + " Error")