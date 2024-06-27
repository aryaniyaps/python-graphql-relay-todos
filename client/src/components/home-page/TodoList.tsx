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
  root: TodoListFragment$key;
};

export default function TodoList({ root }: Props) {
  const [isPending, startTransition] = useTransition();
  const { data, loadNext } = usePaginationFragment(TodoListFragment, root);

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
