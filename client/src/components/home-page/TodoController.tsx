import { zodResolver } from "@hookform/resolvers/zod";
import { SubmitHandler, useForm } from "react-hook-form";
import { graphql, useMutation } from "react-relay";
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

const createTodoMutation = graphql`
  mutation TodoControllerCreateMutation($content: String!) {
    createTodo(content: $content) {
      id
      content
      createdAt
      updatedAt
    }
  }
`;

const createTodoSchema = z.object({
  content: z.string().max(250, {
    message: "content cannot be more than 250 characters.",
  }),
});

export default function TodoController() {
  // TODO: update todo list cache after mutation
  const [commitMutation, isMutationInFlight] = useMutation(createTodoMutation);

  const form = useForm<z.infer<typeof createTodoSchema>>({
    resolver: zodResolver(createTodoSchema),
  });

  const onSubmit: SubmitHandler<z.infer<typeof createTodoSchema>> = (data) => {
    commitMutation({ variables: { content: data.content } });
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="flex flex-col gap-8 w-full"
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
