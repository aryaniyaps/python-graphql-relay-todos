import react from "@vitejs/plugin-react";
import path from "path";
import { defineConfig } from "vite";
import relay from "vite-plugin-relay";

export default defineConfig({
  plugins: [react(), relay],
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
