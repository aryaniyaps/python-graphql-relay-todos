import { graphql, useLazyLoadQuery } from "react-relay";
import TodoController from "./TodoController";
import TodoList from "./TodoList";
import { HomePageQuery as HomePageQueryType } from "./__generated__/HomePageQuery.graphql";

const HomePageQuery = graphql`
  query HomePageQuery {
    viewer {
      ...TodoListFragment
    }
  }
`;
export default function HomePage() {
  const data = useLazyLoadQuery<HomePageQueryType>(HomePageQuery, {});
  return (
    <div className="flex flex-col items-center w-full h-full justify-center gap-8 py-8">
      <TodoController />
      <TodoList viewer={data.viewer} />
    </div>
  );
}
