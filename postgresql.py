import asyncio
import config
import psycopg2
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

# Define the structure of the 'orders' table
'''
CREATE TABLE orders (
  order_id     SERIAL PRIMARY KEY,
  product      VARCHAR(100),
  price        FLOAT,
  quantity     SMALLINT
);
'''

# Get the database URL from the configuration file
DATABASE_URL = config.URL

# Initialize the Aiogram Dispatcher
dp = Dispatcher()


# Handle the /start command
@dp.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
     await msg.answer(text="Hello! I'm a bot built with Aiogram. I'm able to use CRUD operations inside a PostgreSQL database.\n\nThese are my capabilities:\n\n/select\n/insert <product> <price> <quantity>\n/edit <order_id> <new_product> <new_price> <new_quantity>\n/delete <order_id>")


# Handle the /select command
@dp.message(Command("select"))
async def cmd_select(msg: types.Message) -> None:
    # Connect to the database and fetch all records from the 'orders' table
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()    
    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    await msg.answer(text="Data from database: \n{}".format(result))

# Handle the /insert command
@dp.message(Command("insert"))
async def cmd_insert(msg: types.Message) -> None:
    try:
        # Parse the input and extract product, price, and quantity
        splitted_msg = msg.text.split(" ")
        product = splitted_msg[1]
        price = float(splitted_msg[2])
        quantity = int(splitted_msg[3])
    except (ValueError, IndexError):
        await msg.answer("Invalid input. Please use /insert <product> <price> <quantity>")
        return

    # Connect to the database and insert the new record into the 'orders' table
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO orders (product, price, quantity)
        VALUES (%s, %s, %s)
    """, (product, price, quantity))

    conn.commit()
    cursor.close()
    conn.close()

    await msg.answer(text="Data inserted successfully!")

# Handle the /edit command
@dp.message(Command("edit"))
async def cmd_edit(msg: types.Message) -> None:
    try:
        # Parse the input and extract order_id, new_product, new_price, and new_quantity
        splitted_msg = msg.text.split(" ")
        order_id = int(splitted_msg[1])
        new_product = splitted_msg[2]
        new_price = float(msg.text.split(" ")[3])
        new_quantity = int(msg.text.split(" ")[4])

    except (ValueError, IndexError):
        await msg.answer("Invalid input. Please use /edit <order_id> <new_product> <new_price> <new_quantity>")
        return

    # Connect to the database and update the record in the 'orders' table
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Esegui l'aggiornamento nella tabella players
    cursor.execute("""
        UPDATE orders
        SET product = %s, price = %s, quantity = %s
        WHERE order_id = %s
    """, (new_product, new_price, new_quantity, order_id))

    conn.commit()
    cursor.close()
    conn.close()

    await msg.answer(text="Data updated successfully! Use /select to see the changes")


# Handle the /delete command
@dp.message(Command("delete"))
async def cmd_delete(msg: types.Message) -> None:

    try:
        # Parse the input and extract order_id
        order_id = int(msg.text.split(" ")[1])
    except (ValueError, IndexError):
        await msg.answer("Invalid input. Please use /delete <order_id>")
        return

    # Connect to the database and delete the record from the 'orders' table
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))

    conn.commit()
    cursor.close()
    conn.close()

    await msg.answer(text="Data deleted successfully!")

# Main function to start the bot
async def main() -> None:
    bot = Bot(config.BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("Bot started...")
    asyncio.run(main())
