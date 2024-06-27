import HomePageLayout from "@/layouts/HomePageLayout";
import { graphql, useLazyLoadQuery } from "react-relay";
import TodoController from "../components/home-page/TodoController";
import TodoList from "../components/home-page/TodoList";
import { HomePageQuery as HomePageQueryType } from "./__generated__/HomePageQuery.graphql";

const HomePageQuery = graphql`
  query HomePageQuery {
    ...TodoListFragment
  }
`;
export default function HomePage() {
  const data = useLazyLoadQuery<HomePageQueryType>(HomePageQuery, {});
  return (
    <HomePageLayout>
      <div className="flex flex-col items-center w-full h-full justify-center gap-8 py-8">
        <TodoController />
        <TodoList root={data} />
      </div>
    </HomePageLayout>
  );
}
