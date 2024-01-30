# AutoEvento

AutoEvento is a Python-based automation tool that allows for the creation of Google Calendar events from a text file. This application streamlines the process of adding multiple appointments to a calendar at once, saving time and avoiding manual data entry.

## Features

- Creates events in Google Calendar by reading information from a text file.
- Automatically sets the time zone to 'America/Sao_Paulo'.
- Allows setting the title, description, start time, and end time for each event.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- Python libraries: `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client`
- OAuth2 credentials for the Google Calendar API

## Installation

Clone the GitHub repository to your local machine:
git clone https://github.com/your-username/AutoEvento.git
cd AutoEvento

## Install the necessary dependencies:
pip install -r requirements.txt


## Configuration

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the Google Calendar API.
3. Create OAuth 2.0 credentials and download the `credentials.json` file.
4. Place the `credentials.json` file in the root directory of the project.


