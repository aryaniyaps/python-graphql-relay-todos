import { usePaginationFragment } from "react-relay";
import Todo from "./Todo";

import { useTransition } from "react";
import { graphql } from "relay-runtime";
import { Button } from "../ui/button";
import { ScrollArea } from "../ui/scroll-area";
import { TodoListFragment$key } from "./__generated__/TodoListFragment.graphql";

const TodoListFragment = graphql`
  fragment TodoListFragment on Query
  @refetchable(queryName: "TodoListPaginationQuery")
  @argumentDefinitions(
    cursor: { type: "String" }
    count: { type: "Int", defaultValue: 3 }
  ) {
    todos(after: $cursor, first: $count)
      @connection(key: "TodoListFragment_todos") {
      __id
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

  if (data.todos.edges.length === 0 && !data.todos.pageInfo.hasNextPage) {
    return (
      <div className="flex grow flex-col gap-4 px-4 items-center h-full">
        <p className="font-medium text-muted-foreground">
          Hmm, there are no todos yet
        </p>
      </div>
    );
  }

  return (
    <ScrollArea className="flex grow w-full flex-col gap-4 px-4">
      {data.todos.edges.map((todoEdge) => {
        return (
          <Todo
            todo={todoEdge.node}
            connectionId={data.todos.__id}
            key={todoEdge.node.id}
          />
        );
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
