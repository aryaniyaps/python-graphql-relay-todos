import { useClientQuery } from "react-relay";
import { ScrollArea } from "../ui/scroll-area";
import Todo from "./Todo";

import { graphql } from "relay-runtime";
import { TodoListQuery as TodoListQueryType } from "./__generated__/TodoListQuery.graphql";

const getTodosQuery = graphql`
  query TodoListQuery {
    todos {
      edges {
        node {
          ...TodoFragment
        }
      }
      pageInfo {
        hasNextPage
      }
    }
  }
`;

export default function TodoList() {
  const data = useClientQuery<TodoListQueryType>(getTodosQuery, {});
  console.log(data);
  return (
    <ScrollArea className="flex grow w-full">
      {data.todos?.edges?.map((todoEdge) => {
        return <Todo todo={todoEdge.node} key={todoEdge.node.id} />;
      })}
    </ScrollArea>
  );
}
