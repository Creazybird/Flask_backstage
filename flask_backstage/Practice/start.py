# 图书管理
# 1. 创建数据库连接信息，定义模型
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

CSRFProtect(app)

# 链接数据库，创建ORM
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:bird@127.0.0.1:3306/library"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 设置盐
app.config['SECRET_KEY'] = 'WOSHIGERENCAI'


# model 设计了两张表 作者 书籍  一对多

class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)

    # author 与 book是一对多关系
    # author 天添加关系属性和反向引用
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))  # 外键


# 写增删改查
@app.route('/add_book', methods=['POST'])
def add_book():
    author_name = request.form.get('author')
    book_name = request.form.get('book')

    if not all([author_name, book_name]):
        return '作者，书籍都不能为空'

    author = Author.query.filter(Author.name == author_name).first()
    if author:
        book = Book.query.filter(Book.name == book_name, Book.author_id == author.id).first()
        if book:
            flash('数据库中已有这条数据，不必重复添加')
        else:
            book = Book(name=book_name, author_id=author.id)
            db.session.add(book)
            db.session.commit()
    else:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        book = Book(name=book_name, author_id=author.id)
        db.session.add(book)
        db.session.commit()
    return redirect(url_for('show_page'))


@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id
                          )  # query.get(主键)  根据主键进行查询
    if book:
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('show_page'))
    else:
        return '不存在此编号书籍'


@app.route('/delete_author/<int:author_id>')
def delete_author(author_id):
    author = Author.query.get(author_id)
    # 因为author 中的id 做了 book表的外键
    for book in author.books:  # 卧槽，还有操作，有了外键，通过autor对象获取外键对应的model实例
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('show_page'))


@app.route('/')
def show_page():
    authors = Author.query.all()
    return render_template('library.html', authors=authors)


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()  # 定义了model 调用这句代码就ok了，创建了表

    # 创建测试数据
    # au1 = Author(name='刘备')
    # au2 = Author(name='曹操')
    # au3 = Author(name='孙权')
    # au4 = Author(name='关羽')
    # au5 = Author(name='张飞')
    # au6 = Author(name='典韦')
    # au7 = Author(name='许褚')
    # au8 = Author(name='周瑜')
    # au9 = Author(name='黄盖')
    #
    # db.session.add_all([au1, au2, au3, au4, au5, au6, au7, au8, au9])
    # db.session.commit()
    #
    # bk1 = Book(name='老刘家的人', author_id=au1.id)
    # bk2 = Book(name='曹家事迹', author_id=au2.id)
    # bk3 = Book(name='为父复仇', author_id=au3.id)
    # bk4 = Book(name='中意', author_id=au4.id)
    # bk5 = Book(name='二八长矛', author_id=au5.id)
    # bk6 = Book(name='早死', author_id=au6.id)
    # bk7 = Book(name='天下第一', author_id=au7.id)
    # bk8 = Book(name='被气死了', author_id=au8.id)
    # bk9 = Book(name='轻点打', author_id=au9.id)
    #
    # db.session.add_all([bk1,bk2,bk3,bk4,bk5,bk6,bk7,bk8,bk9])
    # db.session.commit()

    app.run(debug=True)
