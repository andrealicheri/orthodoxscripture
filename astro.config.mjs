import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
    output: 'server',
    adapter: vercel({
        isr: true,
        isr: {
            expiration: 60 * 60 * 24 * 30 * 6,
        }
    })
});
