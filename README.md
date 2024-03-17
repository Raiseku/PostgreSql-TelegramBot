# **Telegram Chatbot with PostgreSQL Integration**

Youtube explanation video: https://youtu.be/z5JT-bPdusY

This repository contains a Python script to create a Telegram chatbot capable of connecting to a PostgreSQL database and performing CRUD (Create, Read, Update, Delete) operations. The bot is built using the Aiogram library for Telegram bot development and psycopg2 for PostgreSQL database interaction.

## **Prerequisites**

- Python 3.7 or higher
- PostgreSQL installed and running
- Telegram bot token

## **Setup Instructions**

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:
    
    ```
    pip install -r requirements.txt
    ```
    
3. Create a PostgreSQL database and define the structure of the 'orders' table using the provided SQL query in the script.
4. Obtain a Telegram bot token from the BotFather.
5. Configure your PostgreSQL database URL and Telegram bot token in the **`config.py`** file.

## **Usage**

Run the script using Python:

```
Copy code
python postgresql.py
```

Once the bot is running, you can interact with it using the following commands in your Telegram chat:

- **`/start`**: Start the bot and display available commands.
- **`/select`**: Fetch all records from the 'orders' table.
- **`/insert <product> <price> <quantity>`**: Insert a new record into the 'orders' table.
- **`/edit <order_id> <new_product> <new_price> <new_quantity>`**: Update an existing record in the 'orders' table.
- **`/delete <order_id>`**: Delete a record from the 'orders' table.

## **Notes**

- Make sure your PostgreSQL database is accessible and properly configured.
- Ensure that your Telegram bot is active and has the necessary permissions to interact with users.
- Handle sensitive information (like database credentials and bot tokens) securely.
