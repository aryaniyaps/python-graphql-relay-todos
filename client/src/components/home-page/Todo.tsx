import { dtf } from "@/lib/intl";
import clsx from "clsx";
import { useFragment, useMutation } from "react-relay";
import { graphql } from "relay-runtime";
import { Icons } from "../icons";
import { Button } from "../ui/button";
import { Card, CardFooter, CardHeader, CardTitle } from "../ui/card";
import { TodoFragment$key } from "./__generated__/TodoFragment.graphql";

export const TodoFragment = graphql`
  fragment TodoFragment on Todo {
    id
    content
    completed
    createdAt
    updatedAt
  }
`;

// TODO: handle TodoNotFoundErrors
const deleteTodoMutation = graphql`
  mutation TodoDeleteMutation($todoId: ID!, $connections: [ID!]!) {
    deleteTodo(todoId: $todoId) {
      __typename
      ... on Todo {
        id @deleteEdge(connections: $connections)
      }
      ... on TodoNotFoundError {
        message
      }
    }
  }
`;

const toggleTodoCompletedMutation = graphql`
  mutation TodoToggleCompleteMutation($todoId: ID!) {
    toggleTodoCompleted(todoId: $todoId) {
      ... on Todo {
        ...TodoFragment
      }
    }
  }
`;

type Props = {
  todo: TodoFragment$key;
  connectionId: string;
};

export default function Todo({ todo, connectionId }: Props) {
  const [commitDeleteMutation, isDeleteMutationInFlight] =
    useMutation(deleteTodoMutation);
  const [commitToggleCompletedMutation, isToggleCompletedMutationInFlight] =
    useMutation(toggleTodoCompletedMutation);
  const data = useFragment(TodoFragment, todo);

  return (
    <Card className="mb-4 group">
      <CardHeader>
        <CardTitle
          className={clsx({
            "line-through": data.completed,
          })}
        >
          <p className="break-words">{data.content}</p>
        </CardTitle>
      </CardHeader>
      <CardFooter className="flex">
        <p className="text-xs text-muted-foreground">
          created at {dtf.format(new Date(data.createdAt))}
        </p>
        <div className="flex gap-2 grow justify-end opacity-0 group-hover:opacity-100 transition-opacity">
          <Button
            title={data.completed ? "mark as incomplete" : "mark as complete"}
            size={"icon"}
            variant={"ghost"}
            disabled={isToggleCompletedMutationInFlight}
            onClick={() => {
              commitToggleCompletedMutation({
                variables: { todoId: data.id },
              });
            }}
          >
            {data.completed ? (
              <Icons.close className="h-4 w-4" />
            ) : (
              <Icons.check className="h-4 w-4" />
            )}
          </Button>
          <Button
            title="delete todo"
            size={"icon"}
            variant={"destructive"}
            disabled={isDeleteMutationInFlight}
            onClick={() => {
              commitDeleteMutation({
                variables: { todoId: data.id, connections: [connectionId] },
              });
            }}
          >
            <Icons.trash className="h-4 w-4" />
          </Button>
        </div>
      </CardFooter>
    </Card>
  );
}
