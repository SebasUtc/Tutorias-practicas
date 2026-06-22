import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
   base: './',
   root: resolve(__dirname, 'src'),   // Mantiene la raíz en src para buscar tus recursos
   server: {
    host: true,
    port: 3000,
    hot: true,
    open: true,
  },
  css: {
    preprocessorOptions: {
        scss: {},
      }
  },
  build: {
    // 1. Cambiamos 'dist' para que envíe los archivos directo a los estáticos de Django
    outDir: resolve(__dirname, '../static/private'), 
    emptyOutDir: false, // Evita que borre otras cosas de tus estáticos
    rollupOptions: {
      // 2. En lugar de buscar HTMLs, le decimos que compile directamente tu CSS/JS principal
      input: {
        main: resolve(__dirname, 'static/private/assets/js/main.js'), // O 'src/assets/css/main.css' según donde esté tu archivo base
      },
      output: {
        chunkFileNames: 'assets/js/[name].js',
        entryFileNames: 'assets/js/[name].js',
        assetFileNames: ({name}) => {
          if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')){
              return 'assets/images/[name][extname]';
          }
          if (/\.css$/.test(name ?? '')) {
              return 'assets/css/[name][extname]'; // <-- Aquí nacerá tu main.css
          }
          return 'assets/[name][extname]';
        },
      },
    },
  },
});