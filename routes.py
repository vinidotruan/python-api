from bootstrap import app, request, db, jsonify
from DAO.book import Book
from DAO.client import Client
from DAO.reserve import Reserve

@app.route("/books", methods=["POST"])
def register_books():
    new_book = Book(
        title=request.json['title'],
        author=request.json['author']
        )
    db.session.add(new_book)
    db.session.commit()

    return jsonify({
      'id': new_book.id,
      'title': new_book.title,
      'author': new_book.author
    })

@app.route("/books", methods=["GET"])
def all_books():
    return jsonify([
        {'id': book.id, 'title': book.title, 'author': book.author}
        for book in Book.query.all()
    ])
    
@app.route("/books/<int:book_id>", methods=["GET"])
def book(book_id):
    book = Book.query.get(book_id)
    return jsonify([
        {'id': book.id, 'title': book.title, 'author': book.author,}
    ])

# @app.route("/books/<int:book_id>", methods=["PUT"])
# def update_book(book_id):
#     book = Book.query.get(book_id)

#     book.title = request.json['title'] if True else book.title
#     book.author = request.json['author'] if request.json['author'] else book.author

#     db.session.commit()

#     return book
#     # return jsonify([
#     #     {'id': book.id, 'title': book.title, 'author': book.author}
#     # ])

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify([{'message': "Data deleted"}])

@app.route("/books/<int:book_id>/reserve", methods=["POST"])
def register_reserves_by_book(book_id):
    reserve = Reserve(
        date_out = request.json['date_out'],
        date_back = request.json["date_back"] if request.json["date_back"] is not None else None,
        client_id = request.json['client_id'],
        book_id = book_id
    )

    db.session.add(reserve)
    db.session.commit()

    return Reserve.response(reserve)


# =============================================== #

@app.route("/clients", methods=["POST"])
def register_clients():
    new_client = Client(
        name=request.json['name'],
    )
    db.session.add(new_client)
    db.session.commit()

    return Client.response(new_client)

@app.route("/clients", methods=["GET"])
def all_clients():
    return jsonify([
        {'id': client.id, 'name': client.name}
        for client in Client.query.all()
    ])
    
@app.route("/clients/<int:client_id>", methods=["GET"])
def client(client_id):
    client = Client.query.get(client_id)
    return Client.response(client)

@app.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_clients(client_id):
    client = Client.query.get(client_id)
    db.session.delete(client)
    db.session.commit()

    return jsonify([{'message': "Data deleted"}])

@app.route("/clients/<int:client_id>/reserves", methods=["GET"])
def clients_reserves(client_id):
    client = Client.query.get(client_id)
    return jsonify([
        {'date_out': reserve.date_out,'date_back': reserve.date_back,'client_id': reserve.client_id,'book_id': reserve.book_id}
        for reserve in client.reserves
    ])

@app.route("/clients/<int:client_id>/books", methods=["GET"])
def clients_books(client_id):
    client = Client.query.get(client_id)
    
    return jsonify([
        { 'title':reserve.book.title, 'author':reserve.book.author, 'date_out': reserve.date_out, 'delay': Reserve.delayDay(reserve) }
        for reserve in client.reserves
    ])

# =============================================== #

@app.route("/reserves", methods=["POST"])
def register_reserves():
    reserve = Reserve(
        date_out = request.json['date_out'],
        date_back = request.json["date_back"] if request.json["date_back"] is not None else None,
        client_id = request.json['client_id'],
        book_id = request.json['book_id']
    )

    db.session.add(reserve)
    db.session.commit()

    return Reserve.response(reserve)


@app.route("/reserves", methods=["GET"])
def all_reserves():
    return jsonify([
        {
            'date_out': reserve.date_out,
            'date_back': reserve.date_back,
            'client_id': reserve.client_id,
            'book_id': reserve.book_id
        }
        for reserve in Reserve.query.all()
    ])

@app.route("/reserves/<int:reserve_id>", methods=["GET"])
def reserve(reserve_id):
    reserve = Reserve.query.get(reserve_id)
    return Reserve.response(reserve)


@app.route("/reserves/<int:reserve_id>", methods=["DELETE"])
def delete_reserves(reserve_id):
    reserve = Reserve.query.get(reserve_id)
    db.session.delete(reserve)
    db.session.commit()

    return jsonify([{'message': "Data deleted"}])

@app.route("/reserves/<int:reserve_id>/clients", methods=["GET"])
def reserve_clients(reserve_id):
    reserve = Reserve.query.get(reserve_id)

    return Client.response(reserve.client)


@app.route("/reserves/<int:reserve_id>/books", methods=["GET"])
def reserves_books(reserve_id):
    reserve = Reserve.query.get(reserve_id)
    return Book.response(reserve.book)