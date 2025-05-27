import puppeteer from 'puppeteer';
import fs from 'fs';
import path from 'path';

(async () => {
    const downloadPath = path.resolve('downloads'); // Ganti dengan path yang diinginkan

    if (!fs.existsSync(downloadPath)) {
        fs.mkdirSync(downloadPath, { recursive: true });
    }
    // Set opsi untuk mengatur direktori download

    const browser = await puppeteer.launch({
        headless: false, // bisa juga false untuk debugging
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();

    const client = await page.target().createCDPSession();
    await client.send('Page.setDownloadBehavior', {
        behavior: 'allow',
        downloadPath: downloadPath
    });

    // Buka halaman daftar saham IDX
    await page.goto('https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham/',
        {
            waitUntil: 'networkidle2',
            timeout: 60000 // Tunggu hingga halaman dimuat
        }
    );

    // Tunggu tombol "Unduh" muncul (sesuaikan selector)
    await page.waitForSelector('button');

    // Klik tombol "Unduh"
    const buttons = await page.$$('button');
    for (const button of buttons) {
        const buttonText = await page.evaluate(el => el.textContent, button);
        if (buttonText.includes('Unduh')) {
            await button.click();
            break; // Hentikan setelah menemukan tombol Unduh
        }
    }

    // Tunggu proses download (misal 5 detik)
    await new Promise(r => setTimeout(r, 5000));

    await browser.close();
})();
