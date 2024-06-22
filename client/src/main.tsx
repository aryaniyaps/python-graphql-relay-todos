import React, { Suspense } from "react";
import ReactDOM from "react-dom/client";
import { RelayEnvironmentProvider } from "react-relay/hooks";
import App from "./App.tsx";
import Loader from "./components/loader.tsx";
import "./index.css";
import environment from "./lib/relay-environment";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RelayEnvironmentProvider environment={environment}>
      <Suspense fallback={<Loader />}>
        <App />
      </Suspense>
    </RelayEnvironmentProvider>
  </React.StrictMode>
);
