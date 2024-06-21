import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: import.meta.env.VITE_API_URL,
    fetchOptions: {
      mode: "cors",
    },
    credentials: "include",
  }),
});

export default client;
