# WhatsApp Scheduler

A Python-based WhatsApp message scheduler that allows you to send personalized messages automatically at a specified date and time using Twilio’s API. Useful for reminders, greetings, or any scheduled communication over WhatsApp.

## Features

- Send WhatsApp messages programmatically using Twilio.
- Schedule messages for a future date and time.
- Simple user input interface for recipient details and message content.
- Handles invalid or past scheduling times gracefully.

## Prerequisites

- Python 3.x
- Twilio account with WhatsApp sandbox enabled
- Installed Python libraries: `twilio`

Install required libraries using pip:

```bash
pip install twilio

Usage

Clone the repository:
git clone https://github.com/yourusername/whatsapp-scheduler.git
cd whatsapp-scheduler


Open the script and add your Twilio credentials:
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'


Run the script:
python whatsapp_scheduler.py


Follow the prompts:
1.Enter recipient name
2.Enter recipient WhatsApp number with country code
3.Enter your message
4.Enter date (YYYY-MM-DD) and time (HH:MM in 24-hour format)

The script will wait until the scheduled time and then send your message automatically.


Notes

Ensure the scheduled time is in the future.

For testing, you can use Twilio’s WhatsApp sandbox number: +14155238886.
