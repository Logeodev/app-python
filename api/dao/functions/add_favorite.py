# Define a new transaction function to create a HAS_FAVORITE relationship
from api.exceptions.notfound import NotFoundException


def add_to_favorites(tx, user_id, movie_id):
    row = tx.run("""
        MATCH (u:User {userId: $userId})
        MATCH (m:Movie {tmdbId: $movieId})
        MERGE (u)-[r:HAS_FAVORITE]->(m)
        ON CREATE SET u.createdAt = datetime()
        RETURN m {
            .*,
            favorite: true
        } AS movie
    """, userId=user_id, movieId=movie_id).single()

    if row == None:
        raise NotFoundException()
    return row.get('movie')