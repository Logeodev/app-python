def get_user(tx, email):
    # Get the result
    result = tx.run("MATCH (u:User {email: $email}) RETURN u",
        email=email)

    # Expect a single row
    first = result.single()

    # No records? Return None
    if first is None:
        return None

    # Get the `u` value returned by the Cypher query
    user = first.get("u")

    return user