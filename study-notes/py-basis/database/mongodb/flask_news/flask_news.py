from flask import Flask, render_template, redirect, url_for, abort, request
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db' : 'mongo_news',
    'host' : '127.0.0.1',
    'port' : 27017
}
db = MongoEngine(app)

NEWS_TYPES = (
    ('推荐', '推荐'),
    ('百家', '百家'),
    ('本地', '本地'),
    ('图片', '图片')
)

class News(db.Document):
    '''新闻模型'''
    title = db.StringField(required=True, max_length=200)
    content = db.StringField(required=True, choices=NEWS_TYPES)
    news_type = db.StringField(required=True)
    img_url = db.StringField()
    is_valid = db.BooleanField(default=True)
    create_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())

    meta = {
        'collection': 'news',
        'ordering': ['-created_at']
    }

@app.route('/')
def index():
    '''新闻首页'''
    news_list = News.objects.filter(is_valid=True)
    return render_template('index.html', news_list=news_list)

@app.route('/cat/<name>')
def cat(name):
    '''新闻类别页'''
    news_list = News.objects.filter(is_valid=True, news_type=name)
    return render_template('detail.html', news_list=news_list)

@app.route('/detail/<pk>')
def detail(pk):
    '''新闻详情页'''
    news_obj = News.objects.filter(pk=pk).first_or_404()
    # if not news_obj:
    #     abort(404)
    return render_template('cat.html', news_obj=news_obj)

@app.route('/admin')
@app.route('/admin/<int:page>')
def admin(page=None):
    '''后台首页'''
    if page is None:
        page = 1
    page_data = News.objects.paginate(page=page, per_page=5)
    return render_template('admin/index.html', page_data=page_data, page=page)

if __name__ == '__main__':
    app.run(debug=True)
