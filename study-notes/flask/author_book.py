# coding:utf-8
# LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@172.16.23.91:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "degw,dhuebdnulhdgywg3g7gbdbcjh,7dltg3bamdg7favfbufgdal2fvh,gfdilwgd3kyfv3b"


app.config.from_object(Config)
db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_authors.id'))


class AuthorBookFrom(FlaskForm):
    author_name = StringField(label=u"作者", validators=[DataRequired(u"作者必填")])
    book_name = StringField(label=u"书籍", validators=[DataRequired(u"书籍必填")])
    submit = SubmitField(label=u"保存")


@app.route("/", methods=['GET', 'POST'])
def index():
    form = AuthorBookFrom()
    if form.validate_on_submit():
        author_name = form.author_name.data
        book_name = form.book_name.data
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        # book = Book(name=book_name, author_id=author.id)
        book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)


@app.route("/delete_book", methods=["POST"])
def delete_book():
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(code=0, message="OK")


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒', author_id=au_xi.id)
    # bk_qian = Book(name='缥缈之旅', author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # db.session.commit()

    app.run(debug=True)