<h1 align="center">My todos</h1>
<p align="center"><i>Fully fledged application using Strawberry GraphQL, FastAPI, Relay and React</i></p>
<br />
<p align="center">
  <a href="https://skillicons.dev">
<img src="https://skillicons.dev/icons?i=py,graphql,fastapi,postgres,ts,react,vite&perline=8" alt="Tech Stack" />
  </a>
</p>


## Starting the project

1. setup docker compose
```
docker compose up
```
2. install server dependencies
```
cd server
pdm install
```

3. setup database migrations
```
pdm run migrate
```

4. start the server
```
pdm run dev
```

5. install client dependencies
```
cd client
npm install
```
6. start the client
```
npm run dev
```


## Generating the GraphQL schema

```
cd server
pdm run generate-schema
```
