import { useFragment } from "react-relay";
import { ScrollArea } from "../ui/scroll-area";
import Todo from "./Todo";

import { graphql } from "relay-runtime";
import { TodoListFragment$key } from "./__generated__/TodoListFragment.graphql";

const TodoListFragment = graphql`
  fragment TodoListFragment on Viewer
  @argumentDefinitions(
    cursor: { type: "String" }
    count: { type: "Int", defaultValue: 3 }
  ) {
    todos(after: $cursor, first: $count) {
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
  viewer: TodoListFragment$key;
};

export default function TodoList({ viewer }: Props) {
  const data = useFragment(TodoListFragment, viewer);
  console.log(data);
  return (
    <ScrollArea className="flex grow w-full">
      {data.todos.edges.map((todoEdge) => {
        return <Todo todo={todoEdge.node} key={todoEdge.node.id} />;
      })}
    </ScrollArea>
  );
}
