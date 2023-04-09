# document_proccesor

## Prerequisite
- Install docker and docker-compose<br>
---

## Access docker command
To build container first time, execute a secure build command with verbose verification.  
```
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose --verbose build --no-cache 
```

1) Deploy a dev environment into local machine, using docker-compose:
```
docker-compose up -d
```
2) Container must be showed into Docker app, or with list command:
```
docker ps
```

3) Access to container 
```
docker exec -it document_proccesor_web_1 bash
```

4) Down local container:
```
docker-compose down
```
---

## Development commands - outside docker container
To execute project
- Install python.  
- Load and join python virtual environment: `python3 -m venv venv && . venv/bin/activate`
- Install python requirements: `pip install -r requirements.txt`
- Leave python virtual environment: `deactivate`
---

## Testing
Project implement pytest and coverage, next command execute test and generate report, test information has been loaded into terminal.
```
coverage run -m pytest && coverage html
```
 - Notice new directory has been created (**htmlcov**). Load *index.html* into web browser to check measuring code report 
---

## Endpoints
Project include next endpoints to complete data process:

### Get document information 
`type=GET`
```
http://localhost:80/document
```
Return content from document_root

| PARAMS  | TYPE   | DATA                          | EXAMPLE                          |
|---------|--------|-------------------------------|----------------------------------|
| section | string | route of information required | section=root_document.subtitle_2 |


### Add document information 
`type=POST`
```
http://localhost:80/document
```
Add new data into system

| PARAMS | TYPE   | DATA                          | EXAMPLE                  |
|--------|--------|-------------------------------|--------------------------|
| path   | string | route of information required | root_document.subtitle_2 |
| name   | string | name of new section           | my_new_section           |
| text   | string | text of new section           | text for my new section  |

Response return `ok` if data inserted correctly
