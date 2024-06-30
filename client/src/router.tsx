import { createBrowserRouter } from "react-router-dom";
import ErrorScreen from "./components/ErrorScreen";
import HomePage from "./pages/HomePage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
    errorElement: <ErrorScreen />,
  },
]);

export default router;
