# Create a virtual environment
mkdir hotel_booking_chatbot
cd hotel_booking_chatbot
python3.9 -m venv venv
source venv/bin/activate

# RASA Setup
pip install rasa
rasa init

streamlit_extras-0.4.6



#Let's start with the RASA implementation:

# Set up RASA project:
rasa init --no-prompt


# ==== Update all necessrily Files # ====

# To run this setup:

#Train the RASA model:
rasa train

# Start the RASA server:
# rasa run --enable-api
# rasa run --enable-api --cors "*"
rasa run --enable-api --endpoints endpoints.yml

# In a new terminal, start the actions server:
rasa run actions

#Run the Streamlit app:
streamlit run app.py



st.set_page_config(page_title="Best Hotel Inn Booking", page_icon="🏨")


What Course do you want to learn? String
Mode of Training: String
No of Pertipant : int
Prefered_state date : date
full name : String
Email Address : Email
Note: string
