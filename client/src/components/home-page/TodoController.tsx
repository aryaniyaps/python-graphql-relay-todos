import { zodResolver } from "@hookform/resolvers/zod";
import { SubmitHandler, useForm } from "react-hook-form";
import { graphql, useFragment, useMutation } from "react-relay";
import { z } from "zod";
import { Button } from "../ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "../ui/form";
import { Textarea } from "../ui/textarea";
import { TodoControllerFragment$key } from "./__generated__/TodoControllerFragment.graphql";

const TodoControllerFragment = graphql`
  fragment TodoControllerFragment on Query
  @argumentDefinitions(
    cursor: { type: "String" }
    count: { type: "Int", defaultValue: 3 }
  ) {
    todos(after: $cursor, first: $count)
      @connection(key: "TodoListFragment_todos") {
      __id
      edges {
        # we have to select the edges field while
        # using the @connection directive
        __typename
      }
    }
  }
`;

const TodoControllerCreateMutation = graphql`
  mutation TodoControllerCreateMutation(
    $content: String!
    $connections: [ID!]!
  ) {
    createTodo(content: $content) {
      todoEdge @prependEdge(connections: $connections) {
        node {
          ...TodoFragment
        }
      }
    }
  }
`;

const createTodoSchema = z.object({
  content: z.string().max(250, {
    message: "content cannot be more than 250 characters.",
  }),
});

type Props = {
  rootQuery: TodoControllerFragment$key;
};

export default function TodoController({ rootQuery }: Props) {
  const data = useFragment(TodoControllerFragment, rootQuery);
  const [commitMutation, isMutationInFlight] = useMutation(
    TodoControllerCreateMutation
  );

  const form = useForm<z.infer<typeof createTodoSchema>>({
    resolver: zodResolver(createTodoSchema),
    values: { content: "" },
  });

  const onSubmit: SubmitHandler<z.infer<typeof createTodoSchema>> = async (
    input
  ) => {
    console.log(data.todos.__id);
    form.reset();
    commitMutation({
      variables: { content: input.content, connections: [data.todos.__id] },
    });
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="flex flex-col gap-8 w-full px-4"
      >
        <FormField
          control={form.control}
          name="content"
          render={({ field }) => (
            <FormItem>
              <FormControl>
                <Textarea
                  placeholder="write here..."
                  className="resize-none"
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" disabled={isMutationInFlight}>
          Create todo
        </Button>
      </form>
    </Form>
  );
}
