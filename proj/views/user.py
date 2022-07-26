from flask import Blueprint, render_template, request, make_response,jsonify

from proj import app, model, db

bp_user = Blueprint('bp_user', __name__)


@bp_user.route('/list', methods=['GET'])
def list():
    return jsonify("OKEY")