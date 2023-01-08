from flask import redirect, render_template, request, Blueprint, abort, flash, url_for
from app.models import *
from app import db
from app.models import Content, FormRequest
from app.main.forms import ContactForm


main = Blueprint('main', __name__)


@main.route('/home')
@main.route('/')
def home():
    url = url_for('static', filename="images/avatar.jpg")
    return render_template('main/home.html', title="home", url=url)


@main.route('/projects')
def projects():
    page = request.args.get('page', 1, type=int)
    projects = Content.query.filter_by(type='Project').order_by(Content.date_added.desc())\
        .paginate(page=page, per_page=30)
    return render_template('main/projects.html', projects=projects, title="projects")


@main.route('/articles')
def articles():
    flask = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Flask'})).count()
    javascript = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'JavaScript'})).count()
    css = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'CSS3'})).count()
    bootstrap = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Bootstrap'})).count()
    HTML = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'HTML5'})).count()
    python = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Python'})).count()
    regex = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Regular Expressions'})).count()
    categories = {'Flask': flask, 'JavaScript': javascript, 'CSS3': css, 'Bootstrap': bootstrap, 'HTML5': HTML, 'Python': python, 'Regular Expressions': regex}
    page = request.args.get('page', 1, type=int)
    articles = Content.query.filter_by(type='Article').order_by(Content.date_added.desc())\
        .paginate(page=page, per_page=30)
    total = Content.query.filter_by(type='Article').count()
    return render_template('main/articles.html', articles=articles, categories=categories, total=total, title="articles")


@main.route('/articles/<string:category>')
def show_by_category(category):
    flask = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Flask'})).count()
    javascript = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'JavaScript'})).count()
    css = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'CSS3'})).count()
    bootstrap = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Bootstrap'})).count()
    HTML = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'HTML5'})).count()
    python = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Python'})).count()
    regex = db.session.query(Content).filter_by(type='Article').filter(Content.subjects.contains({'Regular Expressions'})).count()
    categories = {'Flask': flask, 'JavaScript': javascript, 'CSS3': css, 'Bootstrap': bootstrap, 'HTML5': HTML, 'Python': python, 'Regular Expressions': regex}
    page = request.args.get('page', 1, type=int)
    articles = Content.query.filter_by(type='Article').filter(Content.subjects.contains({category})).order_by(Content.date_added.desc())\
        .paginate(page=page, per_page=30)
    total = Content.query.filter_by(type='Article').count()
    return render_template('main/articles.html', articles=articles, categories=categories, total=total, title="articles", category=category)


@main.route('/projects/<int:id>')
def project_detailed(id):
    project = Content.query.filter_by(type='Project', id=id).one_or_none()
    if project is None:
        abort(404)
    url = url_for('static', filename="images/"+project.image)
    return render_template('main/item-details.html', content=project, url=url, title="projects")


@main.route('/articles/<int:id>')
def article_detailed(id):
    article = Content.query.filter_by(type='Article', id=id).one_or_none()
    if article is None:
        abort(404)
    return render_template('main/item-details.html', content=article, title="articles")


@main.route('/contact', methods=['POST','GET'])
def contact():
    form = ContactForm()
    if request.method=='POST':
        if form.validate_on_submit():
            form_request = FormRequest(name=form.name.data, email=form.email.data,
                        subject=form.subject.data, message=form.message.data)
            db.session.add(form_request)
            db.session.commit()
            flash("Your message has been successfuly sent!", "success")
            return redirect(url_for('main.home'))
        else:
            flash("Please check your input", "danger")
    return render_template('main/contact.html', form=form, title="contact")