import { usePaginationFragment } from "react-relay";
import Todo from "./Todo";

import { useTransition } from "react";
import { graphql } from "relay-runtime";
import { Button } from "../ui/button";
import { ScrollArea } from "../ui/scroll-area";
import { TodoListFragment$key } from "./__generated__/TodoListFragment.graphql";

// TODO: pass this to mistral and ask if its okay to query for the same connection in two different components like
// this. we could probably get the connection ID from the query here and send the id directly to the todo controller
const TodoListFragment = graphql`
  fragment TodoListFragment on Query
  @refetchable(queryName: "TodoListPaginationQuery")
  @argumentDefinitions(
    cursor: { type: "String" }
    count: { type: "Int", defaultValue: 3 }
  ) {
    todos(after: $cursor, first: $count)
      @connection(key: "TodoListFragment_todos") {
      edges {
        node {
          id
          ...TodoFragment
        }
      }
      pageInfo {
        hasNextPage
      }
    }
  }
`;

type Props = {
  rootQuery: TodoListFragment$key;
};

export default function TodoList({ rootQuery }: Props) {
  const [isPending, startTransition] = useTransition();
  const { data, loadNext } = usePaginationFragment(TodoListFragment, rootQuery);

  function loadMore() {
    return startTransition(() => {
      loadNext(3);
    });
  }

  return (
    <ScrollArea className="flex grow w-full flex-col gap-4">
      {data.todos.edges.map((todoEdge) => {
        return <Todo todo={todoEdge.node} key={todoEdge.node.id} />;
      })}
      {data.todos.pageInfo.hasNextPage && (
        <Button
          className="w-full"
          variant={"secondary"}
          onClick={loadMore}
          disabled={isPending}
        >
          load more
        </Button>
      )}
      {isPending && <p>loading</p>}
    </ScrollArea>
  );
}
