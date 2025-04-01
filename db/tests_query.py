import aiosqlite


async def get_all_tests():
    async with aiosqlite.connect('db.sqlite') as db:
        cursor = await db.execute("""
            SELECT *
            FROM test_type
        """)
        rows = await cursor.fetchall()
        tests = [
            {
                'test_id': row[0],
                'test_name': row[1],
            } for row in rows
        ]
        return tests
