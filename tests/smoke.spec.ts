import { test, expect } from '@playwright/test';

test('page loads, no console errors, main content visible', async ({ page }) => {
  const errors: string[] = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });

  await page.goto('/');

  const title = await page.title();
  expect(title.trim().length).toBeGreaterThan(0);

  const h1Count = await page.locator('h1').count();
  if (h1Count > 0) {
    await expect(page.locator('h1').first()).toBeVisible();
  } else {
    await expect(page.locator('body')).toBeVisible();
  }

  expect(errors, `Console errors:\n${errors.join('\n')}`).toHaveLength(0);
});
