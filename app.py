import streamlit as st
from PIL import Image
import pickle
import numpy as np
import base64

# Load the trained model
model = pickle.load(open("D:/Self Projects/bengaluru house price/BHP/venv/streamlit/bangalore_house_price_prediction.pickle", 'rb'))

# Define the Streamlit web app
def main():
    # Set the page title
    st.title('Bangalore House Price Prediction')

    # Load the background image
    def get_base64_of_bin_file(file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        return base64.b64encode(data).decode()

    # Load the background image
    background_image = get_base64_of_bin_file('D:/Self Projects/bengaluru house price/BHP/bhp.jpeg')

   # Write the HTML code to overlay the image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpg;base64,{background_image}');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create input fields for the features
    area_type = st.selectbox('Area Type', [0, 1, 2, 3], index=0)
    location = st.selectbox('Location', list(range(252)), index=0)
    total_sqft = st.number_input('Total Sqft', min_value=1.0)
    bath = st.number_input('Number of Bathrooms', min_value=1)
    BHK = st.number_input('Number of BHK', min_value=1)

    # Create a button to trigger the prediction
    if st.button('Predict Price'):
        # Prepare the input features as a dictionary
        input_data = {
            'area_type': area_type,
            'location': location,
            'total_sqft': total_sqft,
            'bath': bath,
            'BHK': BHK
        }

        # Reshape the input data
        input_array = np.array(list(input_data.values())).reshape(1,-1)

        # Perform the prediction using the loaded model
        price_prediction = model.predict(input_array)

        # Display the predicted price
        st.success(f'The predicted price is: {price_prediction}')

# Run the web app
if __name__ == '__main__':
    main()