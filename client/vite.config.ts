import react from "@vitejs/plugin-react-swc";
import path from "path";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [
    react({
      plugins: [
        [
          "@swc/plugin-relay",
          {
            src: "./src",
            language: "typescript",
            schema: "../schema/schema.graphql",
            artifactDirectory: "./__generated__",
            eagerEsModules: true,
            excludes: [
              "**/node_modules/**",
              "**/__mocks__/**",
              "**/__tests__/**",
              "**/__generated__/**",
            ],
          },
        ],
      ],
    }),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    watch: {
      ignored: ["**/coverage/**", "**/__tests__/**"],
    },
  },
});
