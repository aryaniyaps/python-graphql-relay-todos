import { useClientQuery } from "react-relay";
import { ScrollArea } from "../ui/scroll-area";
import Todo from "./Todo";

import { graphql } from "relay-runtime";
import { TodoListQuery as TodoListQueryType } from "./__generated__/TodoListQuery.graphql";

const getTodosQuery = graphql`
  query TodoListQuery($first: Int!) {
    notes(first: $first) {
      edges {
        node {
          id
          content
          createdAt
          updatedAt
        }
      }
      pageInfo {
        hasNextPage
      }
    }
  }
`;

export default function TodoList() {
  const data = useClientQuery<TodoListQueryType>(getTodosQuery, { first: 10 });

  return (
    <ScrollArea className="flex grow w-full">
      {data.notes.edges.map((noteEdge) => {
        return <Todo todo={noteEdge.node} key={noteEdge.node.id} />;
      })}
    </ScrollArea>
  );
}
