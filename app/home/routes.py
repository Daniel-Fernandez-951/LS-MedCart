# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from app.home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
import app.home.predictor as pred
from app.home.remoteGet import get_studies, get_brands
import requests


@blueprint.route('/index')
@login_required
def index():
    html_resp = get_studies()
    return render_template('index.html', segment='index', studies_html=html_resp)


# MODEL PREDICTIONS
@blueprint.route('/api/model', methods=['POST', 'GET'])
@login_required
def model_results():
    if 'submit' in request.form:
        text = request.form['input_a']
        table = pred.pred_function(text)
        return render_template('results-table.html', table_html=table)


# # Studies GET Endpoint
# @blueprint.route('/api/studies', methods=['GET'])
# @login_required
# def html_studies():
#     html_resp = get_studies()
#     return render_template('index.html', studies_html=html_resp)


# Products GET Endpoint
@blueprint.route('/api/products', methods=['GET'])
def html_prod():
    html_resp = get_brands()
    return html_resp


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
