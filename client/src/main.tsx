import React, { Suspense } from "react";
import ReactDOM from "react-dom/client";
import { RelayEnvironmentProvider } from "react-relay/hooks";
import { RouterProvider } from "react-router-dom";
import LoadingScreen from "./components/LoadingScreen.tsx";
import "./index.css";
import environment from "./lib/relay-environment";
import router from "./router.tsx";

export default function App() {
  return (
    <React.StrictMode>
      <RelayEnvironmentProvider environment={environment}>
        <Suspense fallback={<LoadingScreen />}>
          <RouterProvider router={router} />
        </Suspense>
      </RelayEnvironmentProvider>
    </React.StrictMode>
  );
}

ReactDOM.createRoot(document.getElementById("root")!).render(<App />);
