import { useClientQuery } from "react-relay";
import { ScrollArea } from "../ui/scroll-area";
import Todo from "./Todo";

import { graphql } from "relay-runtime";
import { TodoListQuery as TodoListQueryType } from "./__generated__/TodoListQuery.graphql";

const getTodosQuery = graphql`
  query TodoListQuery {
    allNotes {
      id
      content
      createdAt
      updatedAt
    }
  }
`;

export default function TodoList() {
  const data = useClientQuery<TodoListQueryType>(getTodosQuery, {});

  return (
    <ScrollArea className="flex grow w-full">
      {data.allNotes.map((todo) => {
        return <Todo todo={todo} key={todo.id} />;
      })}
    </ScrollArea>
  );
}
