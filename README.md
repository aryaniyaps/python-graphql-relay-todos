# graphql-notes


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
