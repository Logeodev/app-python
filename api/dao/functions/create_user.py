def create_user(tx, email, encrypted, name):
    return tx.run(""" // (1)
        CREATE (u:User {
            userId: randomUuid(),
            email: $email,
            password: $encrypted,
            name: $name
        })
        RETURN u
    """,
    email=email, encrypted=encrypted, name=name # (2)
    ).single() # (3)