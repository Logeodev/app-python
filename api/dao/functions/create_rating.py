# Create function to save the rating in the database
def create_rating(tx, user_id, movie_id, rating):
    return tx.run("""
    MATCH (u:User {userId: $user_id})
    MATCH (m:Movie {tmdbId: $movie_id})
    MERGE (u)-[r:RATED]->(m)
    SET r.rating = $rating,
        r.timestamp = timestamp()
    RETURN m {
        .*,
        rating: r.rating
    } AS movie
    """, user_id=user_id, movie_id=movie_id, rating=rating).single()