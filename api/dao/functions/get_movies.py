"""
This function will have one mandatory argument passed to it, a Transaction instance that you can use to execute a Cypher statement using the run() method. 
The function should also have the sort, order, skip, limit and userId parameters passed through as named parameters 
"""
# tag::get_movies[]
def get_movies(tx, sort, order, limit, skip, user_id):
    # Define the cypher statement
    cypher = """
        MATCH (m:Movie)
        WHERE m.`{0}` IS NOT NULL
        RETURN m {{ .* }} AS movie
        ORDER BY m.`{0}` {1}
        SKIP $skip
        LIMIT $limit
    """.format(sort, order)

    # Run the statement within the transaction passed as the first argument
    result = tx.run(cypher, limit=limit, skip=skip, user_id=user_id)
    # Extract a list of Movies from the Result
    return [row.value("movie") for row in result]
# end::get_movies[]