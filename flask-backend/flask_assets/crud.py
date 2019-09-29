from flask_assets import get_model
from flask import Blueprint, redirect, render_template, request, url_for
from flask import Response
import json

crud = Blueprint('crud', __name__)


# [START list]
@crud.route("/")
def list():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    locations, next_page_token = get_model().list(cursor=token)

    return render_template(
        "list.html",
        locations=locations,
        next_page_token=next_page_token)
# [END list]


@crud.route('/<id>')
def view(id):
    location = get_model().read(id)
    return render_template("view.html", location=location)


# [START add]
@crud.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        location = get_model().create(data)

        return redirect(url_for('.view', id=location['id']))

    return render_template("form.html", action="Add", location={})
# [END add]


@crud.route('/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    location = get_model().read(id)

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        location = get_model().update(data, id)

        return redirect(url_for('.view', id=location['id']))

    return render_template("form.html", action="Edit", location=location)


@crud.route('/<id>/delete')
def delete(id):
    get_model().delete(id)
    return redirect(url_for('.list'))


@crud.route('/rjson', methods=['GET'])
def api_hello():
    # parsed_json = (json.loads('collection.json'))
    # print(parsed_json)

    d = {}

    with open("collection.json") as f:
        for line in f:
            print(line)
            js = json.dumps(line)
            # (key, val) = line.split()
            # d[int(key)] = val
    # js = json.dumps(d)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = ''

    return resp
