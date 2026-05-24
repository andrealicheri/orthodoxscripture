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
    }),
    vite: {
        optimizeDeps: {
            exclude: ['astro'] // Prevents Bun from pre-bundling Astro's virtual internals
        }
    }
});
