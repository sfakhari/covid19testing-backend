# Backend for findcovidtesting.com

## Endpoints

### Health check
GET `/api/v1/health`

### List locations
GET `/api/v1/location`

### Create location
Requires basic auth
POST `/api/v1/location`

### Get location
GET `/api/v1/location{location_id}`

### Update location (not implemented yet)
Requires basic auth
POST `/api/v1/location{location_id}`

## Help Appreciated For These Items

* Unit tests

## Features

* Flask + blueprints
* SQLAlchemy
* Native AWS Parameter Support for grabbing env and secrets
* Docker
* Lots of automation

## Development

Start PG, pgadmin, and flask in docker:

```
make up
```

Create the schema:

```
make db_create
```

Stop docker environment:

```
make stop
```

## Deploying

Build and push to ECR
```
make push
```

```
make ENVIRONMENT=production push
```

## Database Tasks
The DB schema needs to get created in RDS before using an environment 

```
make ENVIRONMENT=xyz create_db_fargate
```

### Environments
* Staging
* Production

### Secrets
All secrets are stored in AWS Parameter Store with KMS encryption. The naming structure is:

`$ENVIRONMENT/backend/$VAR_IN_CAPS`

### Adding dependencies
```shell
scripts/pip_install.sh XYZ
```

## Structure
```text
├── application - the app code
├── config.py - Parameterized app config
├── create_db.py - Run this to create the DB schema
├── docker - Directory of docker specific scripts for use in dockerfile
├── docker-compose.py - Runs PG, PG admin, and the app
├── docker-compose.yml - local development
├── Dockerfile
├── scripts - Directory of automation scripts for use outside of dockerfile
└── wsgi.py - Hook for launching the app instance
```