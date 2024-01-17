# ChatGPT Integration for Python and Go 
Ensure you have a minimum Go version of 1.21.

This repository provides a simple integration of ChatGPT into both a Python-based web UI and a Go-based API. Follow the instructions below to set up and run the application.

## Python Web UI Setup:

1. Change the access token in `chatgpt.py` by logging in to ChatGPT and obtaining your token from [https://chat.openai.com/api/auth/session](https://chat.openai.com/api/auth/session).

2. Install the required dependencies by running the following commands:

   ```
   sudo apt install python3
   sudo apt install python3-pip
   pip install flask openai markupsafe jinja2
   ```

3. Start the web app by running the following command in the folder where `app.py` is located:

   ```
   python3 app.py
   ```

   The app will be accessible at [http://localhost:5000](http://localhost:5000).

## Go API Setup:

1. Navigate to the `api` folder.

2. Build the API by running the following commands, this might take a long time so sit tight.:

   ```
   go build
   ```

3. Run the built API:

   ```
   ./freechatgpt
   ```

4. Edit your `chatgpt.py`:

   ```python
   url = 'put this as http://localhost:8080 or http://127.0.0.1:8080'
   access_token = "Change this to your access token."
   ```

5. Enjoy!

# Thats it your done!

Special thanks to acheong08 for contributing to the API!

Feel free to explore and integrate ChatGPT into your projects using this simple setup.
