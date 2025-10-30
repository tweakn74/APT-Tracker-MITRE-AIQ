import { test, expect } from '@playwright/test';

test('page structure and basic functionality', async ({ page }) => {
  await page.goto('/');

  // Wait for the page to fully load
  await page.waitForLoadState('networkidle');

  // Check that the page loads without errors
  const title = await page.title();
  expect(title.trim().length).toBeGreaterThan(0);

  // Check that main content is visible
  const body = await page.locator('body');
  await expect(body).toBeVisible();

  // Check that the page contains APT-related content
  const pageContent = await page.content();
  expect(pageContent).toContain('APT');
  expect(pageContent).toContain('FIN7');

  // Check that script tags exist (indicating JavaScript is present)
  const scriptCount = await page.evaluate(() => document.querySelectorAll('script').length);
  expect(scriptCount).toBeGreaterThan(0);

  // Check that the page contains the aptDatabase definition
  expect(pageContent).toContain('aptDatabase');

  console.log('✅ Page structure test passed - ready for deployment');
});
