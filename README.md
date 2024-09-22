# Currency_Converter 💱

A Python-based Currency Converter application that provides real-time exchange rates using a modern graphical user interface (GUI) built with Tkinter. This project fetches live currency exchange rates from an external API and allows users to convert currencies efficiently and interactively.

Features 🚀

Real-time Exchange Rates: Fetches the latest exchange rates from a free API.

Interactive GUI: User-friendly interface built using Tkinter.

Multiple Currencies: Supports conversion between popular currencies such as USD, EUR, INR, JPY, GBP, and CAD.

Conversion Result: Displays the converted amount in a pop-up dialog.

Status Bar: Provides user feedback and displays success or error messages.

Input Validation: Ensures users enter valid amounts for conversion.


Tech Stack 🛠️

Python: The main programming language used.

Tkinter: Python’s standard GUI library used for creating the interface.

Requests: Python library to fetch data from the currency exchange API.


API Information 🌐

The project utilizes the https://api.exchangerate-api.com to retrieve the latest exchange rates. It uses USD as the base currency and converts to/from other supported currencies.

Prerequisites 📋

Before you run the project, ensure you have Python installed on your system. You can install the necessary dependencies by running:

pip install requests

How to Run the Project 🚀

1. Clone the repository:

git clone https://github.com/Diksha026_lab/currency-converter.git


2. Navigate to the project directory:

cd currency-converter


3. Run the Python script:

python currency_converter.py



Once the application starts, you will see a graphical window where you can input the amount, select the source currency, and the target currency. Click the "Convert" button to see the conversion result.


License 📜

This project is licensed under the MIT License. See the LICENSE file for more details.
