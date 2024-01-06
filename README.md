# python-ai-restful-server

## Getting started

This is an archetype project for python restful server, depends on `flask`

## Features
1.  Auto-detect the api endpoint from /api folder
2.  Base on Dockerfile, it can package to a container
3.  In Dockerfile, use gunicorn as container enterpoint

## Deployment
### docker-compose
```yaml
version: '3.7'

services:
  system:
    image: ${docker_repository}/${docker_namespace}/${application_artifact}
    container_name: ${application_artifact}
    restart: always
    volumes:
      - ./api:/app/api
    networks:
      devops-network:
        ipv4_address: 172.18.0.22

networks:
    devops-network:
        external: true
```

## Todos
- [ ] Add auto install mechanism, when a new api endpoint added, whose dependencies are installed automatically or during the container reboot.   
- [ ] Create a new project archetype for the api implements