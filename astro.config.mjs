import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://kirogluciftligi.com',
  trailingSlash: 'ignore',
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/qr'),
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
    }),
    mdx(),
  ],
  build: {
    format: 'directory',
  },
});
