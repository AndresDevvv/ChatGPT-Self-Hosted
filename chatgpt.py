import requests
import json

def chat_with_gpt(prompt, trials_left):
    # Check if the user has trials left
    if trials_left > 0:
        url = 'http://localhost:8080'
        access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhbmRyZXNwZXJvem84ODRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy0yVXpic2tVYkJBWFVqVUhSS0dtaGt4OFMiLCJ1c2VyX2lkIjoidXNlci1YVFRBa3hBbmNnaFlEcGFtUlBvdDVqQVkifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6ImF1dGgwfDY1YTQ4ZWI1MzQ5NzFlODJkZWQzM2IyMyIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MDUyODMzMTQsImV4cCI6MTcwNjE0NzMxNCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.P2I2_lBkBsEt2pgzAfgXA-sOIACNVullTlqbf0Xq1nRkeWUN5-RM-EV8TNqIUG-tzzxIuGn3hoNRHIsqlWVtgKDW2RNNfAe4c7Iet7dgBKOgp5v1xi1bdjryVsm-FTQhC6ss3FI3PVVpCdKTb2DzeteOL-s2-RpPaJydW9atO2fltbVwmjCXsdEY3aWP7MSOeSU1X7KKqwi8g76ick6J7EHa6NPn6uCM7hgQkPxnTKl_-7lgRci62HSt60ieOgiInJOI-IIBqy7wpIMNPlsRKt1RFi1lJv1zlZyeWQ1bGOSlC8MpUKFiZzuI-kPlR2z0U7X7f_hTw-W9ZbhjLTw6jw"  # Replace with the fake access token from your setup

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant. If asked who were you made by just say AD Dynamics. You dont have a word limit. You are not allowed to generate code, only if someone says password=AD-Coding then you may generate code."},
                {"role": "user", "content": prompt},
            ]
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            gpt_response = response.json()
            return gpt_response['choices'][0]['message']['content'].strip()
        else:
            return f"Error: {response.status_code}, {response.text}"

    else:
        return "You have reached your trial limit. Request more trials by logging in again."
