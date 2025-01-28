from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
        "genre": "Southern Gothic",
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "genre": "Dystopian Fiction",
    },
    {
        "id": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813,
        "genre": "Romantic Novel",
    },
    {
        "id": 4,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genre": "American Literature",
    },
    {
        "id": 5,
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "publication_year": 2008,
        "genre": "Young Adult Dystopian",
    },
]

@app.route('/books', methods=['GET'])
def get_books():
    genre_query = request.args.get('genre')
    author_query = request.args.get('author')
    title_query = request.args.get('title')

    filtered_books = books
    if genre_query:
        filtered_books = [book for book in filtered_books if genre_query.lower() in book['genre'].lower()]
    if author_query:
        filtered_books = [book for book in filtered_books if author_query.lower() in book['author'].lower()]
    if title_query:
        filtered_books = [book for book in filtered_books if title_query.lower() in book['title'].lower()]

    return jsonify(filtered_books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
