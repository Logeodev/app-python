Great! Since your project is a Flask app, here are the steps to run it locally in Visual Studio Code:

1. **Clone Your Fork**:
   - Open a terminal in Visual Studio Code.
   - Clone your forked repository:
     ```bash
     git clone https://github.com/Logeodev/app-python.git
     cd app-python
     ```

2. **Set Up a Virtual Environment**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies**:
   - Install the required packages listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory of your project if it doesn't exist.
   - Add any necessary environment variables, such as your Neo4j connection details.

5. **Run the Flask App**:
   - Start your Flask application:
     ```bash
     flask run
     ```
   - By default, the app will be accessible at `http://127.0.0.1:5000/`.

6. **Access Your Routes**:
   - Open your web browser and navigate to the routes set up in your Flask app to ensure everything is working correctly.

If you encounter any issues or need further assistance, feel free to ask!