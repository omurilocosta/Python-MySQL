
def CREATE(parList, parTable, parID, parCursor):
    parCursor.execute(f"""CREATE TABLE IF NOT EXISTS {parTable}(
        {parList} PRIMARY KEY({parID}
        );
        """)