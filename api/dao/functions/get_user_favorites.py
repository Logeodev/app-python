def get_user_favorites(tx, user_id):
    if user_id == None:
        return []
    result = tx.run("""
    MATCH (u:User {userId: $userId})-[r:HAS_FAVORITE]->(m)
    RETURN m.tmdbId as id
    """, userId=user_id)
    return [record.get('id') for record in result]