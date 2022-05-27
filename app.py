import streamlit as st
import requests
import pandas as pd

# global variable to map class values
binary_map = {
    '0': "Non-Disaster Tweet",
    '1': "Disaster Tweet"
}
multi_map = {
    '0': "automobile",
    '1': "entertainment",
    '2': "politics",
    '3': "science",
    '4': "sports",
    '5': "technology",
    '6': "world"
}

def send_request(text, type):
    files = {
        'text': (None, text),
        'type': (None, type),
    }
    response = requests.post('https://main-text-classification-server-cjw531.endpoint.ainize.ai/predict', files=files)
    status_code = response.status_code

    return status_code, response


st.title("Performance Comparison of Binary and Multi Class Text Classification Models With CNN & BERT + CNN Models")

st.header("Binary Classification") # binary classification section
st.markdown("The pre-trained binary classification CNN and BERT + CNN models will classify whether it is a disaster-related Tweets or not.")

# runtime comparison
with st.expander("Runtime Comparison (Seconds)"):
    code = '''Binary Models
+-------------+---------------+--------------------+
|    Model    | Train Runtime | Prediction Runtime |
+-------------+---------------+--------------------+
|     CNN     |       37.7845 |             0.1042 |
| BERT + CNN  |     2046.9980 |             6.4557 |
+-------------+---------------+--------------------+'''
    st.code(code)

# cpu & ram comparison
with st.expander("CPU & RAM Resources Comparison (%)"):
    dict_ = {
        'columns': ['Train CPU', 'Prediction CPU', 'Train RAM', 'Prediction RAM'],
        'CNN': [20.9, 17.5, 31.8, 32.0], 
        'BERT + CNN': [18.8, 24.7, 38.7, 41.4]
        }
    df = pd.DataFrame.from_dict(dict_)
    df = df.rename(columns={'columns':'index'}).set_index('index')
    st.bar_chart(df)
    
# accuracy
with st.expander("Accuracy (%)"):
    dict_ = {
        'columns': ['CNN', 'BERT + CNN'],
        'Accuracy (%)': [86.37, 88.08]
        }
    df = pd.DataFrame.from_dict(dict_)
    df = df.rename(columns={'columns':'index'}).set_index('index')
    st.bar_chart(df)

binary_base_text = st.text_input("Type Disaster or Non-Disaster Tweets", "Last week, around 21 people were assassinated in Texas due to mass shooting.")
if st.button("Predict Binary"):
    text = binary_base_text.title()
    status_code, response = send_request(text, "1")
    print(status_code)
    print(response)
    if status_code == 200:
        prediction = response.json()
        cnn_pred = binary_map[prediction["CNN prediction"]]
        bert_pred = binary_map[prediction['BERT prediction']]
        st.success('BERT + CNN Prediction: ' + bert_pred)
        st.success('CNN Prediction: ' + cnn_pred)
    else:
        st.error(str(status_code) + " Error")

st.markdown("""---""")

st.header("Multiclass Classification")
st.markdown("The pre-trained multiclass classification CNN and BERT + CNN models will classify the news article into 7 categories: \
    'automobile', 'entertainment', 'politics', 'science', 'sports', 'technology', 'world'")

# runtime comparison
with st.expander("Runtime Comparison (Seconds)"):
    code = '''Multiclass Models
+-------------+---------------+--------------------+
|    Model    | Train Runtime | Prediction Runtime |
+-------------+---------------+--------------------+
|     CNN     |       20.0207 |             0.0940 |
| BERT + CNN  |     1165.2892 |             3.8821 |
+-------------+---------------+--------------------+'''
    st.code(code)

# cpu & ram comparison
with st.expander("CPU & RAM Resources Comparison (%)"):
    dict_ = {
        'columns': ['Train CPU', 'Prediction CPU', 'Train RAM', 'Prediction RAM'],
        'CNN': [20.1, 16.4, 49.2, 49.2], 
        'BERT + CNN': [17.5, 24.1, 52.2, 54.8]
        }
    df = pd.DataFrame.from_dict(dict_)
    df = df.rename(columns={'columns':'index'}).set_index('index')
    st.bar_chart(df)

# accuracy
with st.expander("Accuracy (%)"):
    dict_ = {
        'columns': ['CNN', 'BERT + CNN'],
        'Accuracy (%)': [94.98, 95.30]
        }
    df = pd.DataFrame.from_dict(dict_)
    df = df.rename(columns={'columns':'index'}).set_index('index')
    st.bar_chart(df)

multi_base_text = st.text_input("Type News Article to Classify", "Joe Biden recently visited South Korea and then he headed to Japan.")
if st.button("Predict Multiclass"):
    text = multi_base_text.title()
    status_code, response = send_request(text, '2')
    if status_code == 200:
        prediction = response.json()
        cnn_pred = multi_map[prediction["CNN prediction"]]
        bert_pred = multi_map[prediction['BERT prediction']]
        st.success('BERT + CNN Prediction: ' + bert_pred)
        st.success('CNN Prediction: ' + cnn_pred)
    else:
        st.error(str(status_code) + " Error")