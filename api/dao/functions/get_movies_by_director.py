from api.dao.functions.get_user_favorites import get_user_favorites

def get_movies_by_director(tx, id, sort, order, limit, skip, user_id):
    favorites = get_user_favorites(tx, user_id)

    cypher = """
        MATCH (m:Movie)<-[:DIRECTED]-(:Person {{tmdbId: $id}})
        WHERE m.`{0}` IS NOT NULL
        RETURN m {{
            .*,
            favorite: m.tmdbId in $favorites
        }} AS movie
        ORDER BY m.`{0}` {1}
        SKIP $skip
        LIMIT $limit
    """.format(sort, order)

    result = tx.run(cypher, id=id, limit=limit, skip=skip, user_id=user_id, favorites=favorites)

    return [ row.get("movie") for row in result ]