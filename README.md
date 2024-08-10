# holidayz_inn_chatbot


This project implements a chatbot for hotel room booking using RASA for the backend and Streamlit for the frontend.

## Setup and Installation

### Prerequisites
- Python 3.9
- pip

### Create a virtual environment

```bash
mkdir hotel_booking_chatbot
cd hotel_booking_chatbot
python3.9 -m venv venv
source venv/bin/activate
```

###  Install dependencies
```bash
pip install -r requirements.txt
```
### Running the Application
#### 1. Start the RASA server

```bash
rasa run --enable-api --endpoints endpoints.yml
```
### 2. Start the actions server
#### In a new terminal:
```bash
rasa run actions
```

### 3. Run the Streamlit app
#### In another terminal:
```bash
streamlit run chatbot.py
```
### Usage
After starting all components, navigate to the URL provided by Streamlit in your web browser to interact with the chatbot.
