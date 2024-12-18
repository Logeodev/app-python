from api.exceptions.notfound import NotFoundException


def remove_from_favorites(tx, user_id, movie_id):
        row = tx.run("""
            MATCH (u:User {userId: $userId})-[r:HAS_FAVORITE]->(m:Movie {tmdbId: $movieId})
            DELETE r
            RETURN m {
                .*,
                favorite: false
            } AS movie
        """, userId=user_id, movieId=movie_id).single()

        # If no rows are returnedm throw a NotFoundException
        if row == None:
            raise NotFoundException()

        return row.get("movie")