# Super OrgContact
![superOrgContact](https://user-images.githubusercontent.com/38052584/109373827-03d75700-7890-11eb-83fc-ae627d275427.png)

This repository is intended to store the files for client and server sides of the Super Org Contact application, proposed by Conecta Nuvem.

## Commits
For commit messages in this repository, the following prefix convention is used:
- FEAT: new feature added to a particular application
- FIX: bug fix
- STYLE: feature and updates related to styling
- REFACTOR: refactoring a specific section of the codebase
- TEST: everything related to testing
- DOCS: everything related to documentation
- CHORE: regular code maintenance

## Server
### OAuth2
To enable the use of OAuth2, it is required to acquire the credentials related to the project on Google Developers Console.

### Run Flask app
```bash
cd server/
source .venv/bin/activate
python3.7 ./server/main.py
```

### Deploy to Google App Engine
```bash
gcloud app deploy app.yaml --project super-org-flask
```

## Client

### Project setup
```bash
npm install
```

#### Compiles and hot-reloads for development
```bash
npm run serve
```

#### Compiles and minifies for production
```bash
npm run build
```

#### Lints and fixes files
```bash
npm run lint
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
