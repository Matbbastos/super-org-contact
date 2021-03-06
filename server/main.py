# -*- coding: utf-8 -*-

import os
import requests

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

from flask import Flask, url_for, redirect, session, request, jsonify, Response
from flask_cors import CORS
from auth_decorator import login_required


CLIENT_SECRETS_FILE = "credentials.json"
SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/contacts.readonly', 'https://www.googleapis.com/auth/contacts.other.readonly']
API_SERVICE_NAME = 'people'
API_VERSION = 'v1'

CLIENT_BASE_URL = "https://superorgcontact-1614087097383.firebaseapp.com"
SERVER_BASE_URL = "https://super-org-flask.rj.r.appspot.com"

app = Flask(__name__)
app.secret_key = b'\x19j\xa9\x07MR8<I\x9c\x94\xc6* \xb5\xb6'
app.config.from_object(__name__)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

CORS(app, resources={'/*': {'origins': '*'}}, headers=['Content-Type', 'Cookie'], supports_credentials=True)


@app.route('/')
def index():
    return redirect(f"{SERVER_BASE_URL}/login")


@app.route('/login')
def login():
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    session['state'] = state
    return redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    state = session['state']

    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('oauth2callback', _external=True)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)
    return redirect(f"{CLIENT_BASE_URL}/home")


@app.route('/home', methods=['GET'])
@login_required
def home():
    session_credentials = session.get('credentials', 'Não há credenciais')
    credentials = Credentials(**session_credentials)
    service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    call = service.people().connections().list(
        resourceName='people/me',
        pageSize=1000,
        personFields='names,emailAddresses')
    results = call.execute()

    connections = filter_connections(results)
    return jsonify(combine_by_domain(connections))


@app.route('/logout')
def logout():
    if 'credentials' not in session:
        return "Não há credenciais para revogar."

    credentials = Credentials(**session['credentials'])
    revoke = requests.post('https://oauth2.googleapis.com/revoke',
                           params={'token': credentials.token},
                           headers={'content-type': 'application/x-www-form-urlencoded'})

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        if 'credentials' in session:
            del session['credentials']
        return redirect(url_for('index'))
    else:
        return 'Ocorreu um erro.'


def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}


def filter_connections(results):
    connections = results.get('connections', [])
    return [[contact.get('names', None)[0].get('displayName', None), contact.get('emailAddresses', None)[0].get('value', None)] for contact in connections if contact.get('emailAddresses', None)]


def combine_by_domain(connections):
    filtered_connections = {}
    for connection in connections:
        domain = connection[1].split("@")[1]
        if not filtered_connections.get(domain, False):
            filtered_connections.update({domain: []})
        filtered_connections.get(domain).append(connection)
    return filtered_connections


if __name__ == '__main__':
    app.run()
