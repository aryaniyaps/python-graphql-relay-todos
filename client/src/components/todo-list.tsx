import { gql, useQuery } from "@apollo/client";
import Todo from "./todo";
import TodoListSkeleton from "./todo-list-skeleton";
import { ScrollArea } from "./ui/scroll-area";

const GET_TODOS = gql`
  query GetTodos {
    allNotes {
      id
      content
      createdAt
      updatedAt
    }
  }
`;

export default function TodoList() {
  const { loading, error, data } = useQuery(GET_TODOS);

  if (loading) return <TodoListSkeleton />;

  if (error) return `Error! ${error.message}`;

  return (
    <ScrollArea className="flex grow w-full">
      {data.allNotes.map((todo) => {
        return <Todo todo={todo} key={todo.id} />;
      })}
    </ScrollArea>
  );

  return (
    <div className="flex flex-col gap-2 w-full">
      {data.allNotes.map((todo) => {
        return <Todo todo={todo} key={todo.id} />;
      })}
    </div>
  );
}
