import aiosqlite


async def initialize_db():
    async with aiosqlite.connect('db.sqlite') as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT
            )
        """)
        await db.commit()


async def add_user(
        telegram_id: int,
        username: str,
        first_name: str
):
    async with aiosqlite.connect('db.sqlite') as db:
        await db.execute("""
            INSERT INTO users (telegram_id, username, first_name)
            VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO NOTHING
        """, (telegram_id, username, first_name)
        )
        await db.commit()


async def get_all_users():
    async with aiosqlite.connect('db.sqlite') as db:
        cursor = await db.execute('SELECT * FROM users')
        rows = await cursor.fetchall()

        users = [
            {
                'telegram_id': row[0],
                'username': row[1],
                'first_name': row[2]
            }
            for row in rows
        ]
        return users


async def get_user(telegram_id: int):
    async with aiosqlite.connect('db.sqlite') as db:
        cursor = await db.execute(
            'SELECT * '
            'FROM users '
            'WHERE telegram_id = ?',
            (telegram_id,)
        )
        row = await cursor.fetchone()
        if row:
            user = {
                'telegram_id': row[0],
                'username': row[1],
                'first_name': row[2]
            }
            return user
        return None


async def get_question(test_type_id: int):
    async with aiosqlite.connect('db.sqlite') as db:
        cursor = await db.execute(f"""
            SELECT question, right_answer
            FROM questions
            LEFT JOIN test_type
            ON questions.test_type_id = {test_type_id}
            ORDER BY RANDOM()
            LIMIT 1
        """)
        row = await cursor.fetchone()
        question, right_answer = row[0], row[1]
        return question, right_answer
