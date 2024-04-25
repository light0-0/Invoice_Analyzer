# Invoice Reader with LLM Google API
This project demonstrates the basic use of the LLM (Large Language Model) Google API for reading invoices from images and answering user queries based on the content of the invoice.

# Project Overview
The project utilizes Google's Large Language Model (LLM) API to extract information from images of invoices. It then processes user queries based on the extracted data, providing relevant responses.

# Requirements
Python 3.10
Virtualenv
# Installation

1. Clone the repositor:
    * git clone https://github.com/yourusername/your-project.git
cd your-project
2. Create a virtual environment:
    * python3.10 -m venv env

3. Activate the virtual environment:
    * On Windows:
        * .\env\Scripts\activate
    * On macOS and Linux:
        * source env/bin/activate

4. Install the required packages:
    * pip install -r requirements.txt

# Usage
1.Once the environment is set up and the dependencies are installed, run the Streamlit app:
  streamlit run app.py
2.Access the Streamlit app via the provided URL in your browser.
3.Upload an image of an invoice to the app.
4.Ask questions related to the invoice content in the provided interface.
5.The LLM Google API will process the image and provide answers to your queries based on the content extracted from the invoice.