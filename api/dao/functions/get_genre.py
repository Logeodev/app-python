def get_genre(tx, name):
    return tx.run("""
    MATCH (g:Genre {name: $name})<-[:IN_GENRE]-(m:Movie)
    WHERE m.imdbRating IS NOT NULL AND m.poster IS NOT NULL AND g.name <> '(no genres listed)'
    WITH g, m
    ORDER BY m.imdbRating DESC

    WITH g, head(collect(m)) AS movie

    RETURN g {
        .name,
        movies: count { (g)<-[:IN_GENRE]-() },
        poster: movie.poster
    } AS genre
    """, name=name).single()