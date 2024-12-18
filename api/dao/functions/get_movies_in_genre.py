from api.dao.functions.get_user_favorites import get_user_favorites


def get_movies_in_genre(tx, name, sort, order, limit, skip, user_id):
    favorites = get_user_favorites(tx, user_id)

    cypher = """
        MATCH (m:Movie)-[:IN_GENRE]->(:Genre {{name: $name}})
        WHERE m.`{0}` IS NOT NULL
        RETURN m {{
            .*,
            favorite: m.tmdbId in $favorites
        }} AS movie
        ORDER BY m.`{0}` {1}
        SKIP $skip
        LIMIT $limit
    """.format(sort, order)

    result = tx.run(cypher, name=name, limit=limit, skip=skip, user_id=user_id, favorites=favorites)

    return [ row.get("movie") for row in result ]