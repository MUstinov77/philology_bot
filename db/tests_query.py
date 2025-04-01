import aiosqlite


async def get_all_tests():
    async with aiosqlite.connect('db.sqlite') as db:
        cursor = await db.execute("""
            SELECT *
            FROM test_type
        """)
        result = await cursor.fetchall()
        return result
