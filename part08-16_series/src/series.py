class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        result = f"{self.title} ({self.seasons} seasons)\n"
        result += f"genres: {', '.join(self.genres)}\n"

        num_of_ratings = len(self.ratings)
        if num_of_ratings != 0:
            avg_rating = sum(self.ratings) / num_of_ratings
            result += f"{num_of_ratings} ratings, average {avg_rating:.1f} points"
        else:
            result += f"no ratings"

        return result

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list[Series]):
    results = []

    for serie in series_list:
        if min(serie.ratings) > rating:
            results.append(serie)

    return results


def includes_genre(genre: str, series_list: list[Series]):
    results = []

    for serie in series_list:
        if genre in serie.genres:
            results.append(serie)

    return results


def main() -> None:
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)


if __name__ == "__main__":
    main()
