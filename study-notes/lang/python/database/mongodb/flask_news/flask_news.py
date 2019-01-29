from flask import Flask, render_template, redirect, url_for, abort, request
from flask_mongoengine import MongoEngine
from datetime import datetime
from forms import NewsForm

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db' : 'mongo_news',
    'host' : '127.0.0.1',
    'port' : 27017
}
app.config['SECRET_KEY'] = 'a random string'
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
    content = db.StringField(required=True)
    news_type = db.StringField(required=True, choices=NEWS_TYPES)
    img_url = db.StringField()
    is_valid = db.BooleanField(default=True)
    create_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())

    def clean(self):
        if '黄' in self.title:
            raise db.ValidationError('不能有黄字')

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

@app.route('/admin/add', methods=['POST', 'GET'])
def add():
    '''新增新闻数据'''
    form = NewsForm()
    if form.validate_on_submit():
        new_obj = News(
            title = form.title.data,
            content = form.content.data,
            news_type = form.news_type.data,
            img_url = form.img_url.data
        )
        new_obj.save()
        # flash('新增新闻成功')
        return redirect(url_for('admin'))
    return render_template('admin/add.html', form=form)

@app.route('/admin/update/<pk>', methods=['POST', 'GET'])
def update(pk):
    '''修改新闻数据'''
    new_obj = News.objects.get_or_404(pk=pk)
    form = NewsForm()
    if form.validate_on_submit():
        new_obj.title = form.title.data
        new_obj.content = form.content.data
        new_obj.news_type = form.news_type.data
        new_obj.img_url = form.img_url.data
        new_obj.save()
        # flash('修改新闻成功')
        return redirect(url_for('admin'))
    return render_template('admin/update.html', form=form)

@app.route('/admin/delete/<pk>', methods=['POST'])
def delete(pk):
    new_obj = News.objects.filter(pk=pk).first()
    if new_obj:
        return 'no'
    #逻辑删除
    new_obj.is_valid = False
    new_obj.save()
    #物理删除
    new_obj.delete()
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
