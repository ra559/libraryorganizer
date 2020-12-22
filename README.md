# libraryorganiazer
library organaizer

## Description
The goal of this project is to write a web application that allows individuals to organize their books. The application uses the [Openlibrary API](https://openlibrary.org/dev/docs/api/books) to query key details about the books and arranges them in a table format.
The Application must include the following features:
1. A database where the books will be stored. - Assigned to [Ra559](https://github.com/ra559)
2. A connection to the OpenLibrary API - Assigned to [Ra55](https://github.com/ra559)
3. Google Sign on Flask implementation - Assigned to  [Lenthedev](https://github.com/LenTheDev)
4. A simple interface built with Bootstrap 5 - Assigned to [Lenthedev](https://github.com/LenTheDev)

## How to run the program:
1. Download the git repo with `git-clone https://github.com/ra559/gitcollab.git`
2. Install Docker and Docker-compose. Here is a [tutorial](https://docs.docker.com/compose/install/)
3. run the program from the directory where the docker-compose.yml file is located using this command: `docker-compose build && docker-compose up`

## Features currently working
1. Database connectes to the flask container and accepts/retrieves data
2. OpenLibrary API suceesfully retires a json object and it is sucessfully parsed and turned into SQL queries.
3. There is a bug with the google authenticator and it is currently not working.
4. The interface is a work in progress.
