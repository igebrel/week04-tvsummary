def count_genres(records):
    """Count how many TV shows belong to each genre."""
    genre_counts = {}

    for show in records:
        genres = show.get("genres") or []

        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts

def average_rating_by_language(records):
    """Calculate the average TV show rating for each language."""
    rating_totals = {}
    rating_counts = {}

    for show in records:
        language = show.get("language") or "Unknown"
        rating = (show.get("rating") or {}).get("average")

        if isinstance(rating, (int, float)):
            rating_totals[language] = rating_totals.get(language, 0) + rating
            rating_counts[language] = rating_counts.get(language, 0) + 1

    averages = {
        language: round(rating_totals[language] / rating_counts[language], 2)
        for language in rating_totals
    }

    return averages



def count_by_decade(records):
    """Count TV shows by the decade in which they premiered."""
    decade_counts = {}

    for show in records:
        premiered = show.get("premiered")

        if isinstance(premiered, str) and len(premiered) >= 4:
            year_text = premiered[:4]

            if year_text.isdigit():
                year = int(year_text)
                decade = (year // 10) * 10
                label = f"{decade}s"
                decade_counts[label] = decade_counts.get(label, 0) + 1

    return decade_counts


def build_summary(records):
    """Build a summary of the downloaded TV show records."""
    languages = {
        show.get("language")
        for show in records
        if show.get("language")
    }

    return {
        "records_processed": len(records),
        "unique_languages": len(languages),
        "shows_by_genre": count_genres(records),
        "average_rating_by_language": average_rating_by_language(records),
        "shows_by_decade": count_by_decade(records),
    }
