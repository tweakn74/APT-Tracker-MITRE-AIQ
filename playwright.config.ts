import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  use: { 
    baseURL: 'http://127.0.0.1:5500', 
    headless: true, 
    trace: 'on-first-retry' 
  },
  webServer: {
    command: 'npx live-server --port=5500 --no-browser .',
    port: 5500,
    reuseExistingServer: true,
    timeout: 60_000
  },
});
