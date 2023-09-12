import { expect, Locator, Page } from '@playwright/test';

class LoginPage {
    readonly page: Page;
    readonly userName: Locator;
    readonly passWord: Locator;

    constructor(page: Page) {
        this.page = page;
        this.userName = page.getByLabel('username');
        this.passWord = page.getByLabel('password');
    }

    async to_login() {
        await this.userName.fill("hogwarts");
        await this.passWord.fill("test12345");
        await expect(this.page).toHaveTitle('首页');
    }

}

export default LoginPage;