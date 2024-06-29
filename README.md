<h1>Python GraphQL Relay Todos</h1>
<p><i>Fully fledged todo application using Strawberry GraphQL, FastAPI, Relay and React</i></p>
<br />
<img src="https://skillicons.dev/icons?i=py,graphql,fastapi,postgres,ts,react,vite,tailwind,nodejs,docker,git,githubactions&perline=6" alt="Tech Stack" />

<p align="center">
  <video src="/assets/project-demo.mp4" width="500px"></video>
</p>

## Tech Stack:
<i>Backend stack</i>
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Strawberry GraphQL](https://strawberry.rocks/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [AsyncPG](https://magicstack.github.io/asyncpg/current/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Result](https://github.com/rustedpy/result)
- [AioInject](https://thirvondukr.github.io/aioinject/)
- [Structlog](https://www.structlog.org/en/stable/)
- [Pytest](https://docs.pytest.org/en/latest/)

<i>Frontend stack</i>
- [TypeScript](https://www.typescriptlang.org/)
- [React](https://react.dev/)
- [Vite](https://vitejs.dev/)
- [TailwindCSS](https://tailwindcss.com/)
- [Shadcn UI](https://ui.shadcn.com/)
- [Relay](https://relay.dev/)
- [React Router DOM](https://reactrouter.com/en/main)
- [React Hook Form](https://react-hook-form.com/)
- [Zod](https://zod.dev/)


## Features:
- Dependency Injection in resolvers
- Usage of dataloaders to resolve nodes
- Relay spec compliant GraphQL server
- Connection handling, including inserts, updates and deletions
- Usage of Relay Client and fragments
- Cursor paginated connections
- End to end GraphQL code generation
- Fully tested GraphQL server
- User facing errors modelling within the schema

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


## Running the Relay Compiler
```
cd client
npm run relay --watch
```
