import { test, expect } from '@playwright/test';

//Todo refactor this function to clean code
test('test', async ({ page }) => {
    await page.goto('https://litemall.hogwarts.ceshiren.com/#/login');
    await page.getByPlaceholder('管理员账户').click();
    await page.getByPlaceholder('管理员账户').fill('Hogwarts');
    await page.getByPlaceholder('管理员密码').click();
    await page.getByPlaceholder('管理员密码').fill('test12345');
    await page.getByRole('button', { name: '登录' }).click();
});