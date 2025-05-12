import { defineConfig } from 'vite';
import vueJsx from '@vitejs/plugin-vue-jsx';
import vue from '@vitejs/plugin-vue';

import AutoImport from 'unplugin-auto-import/vite';
import Components from 'unplugin-vue-components/vite';
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers';

import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [
    vueJsx(),   // 使vue项目支持jsx语法
    vue(),  // 使vite支持vue组件的编译和解析
    // vueDevTools(),  // vue开发者工具
    /**支持自动导入element-plus组件，vue-index, vue-i18n, pinia */
    AutoImport({
      imports: ['vue', 'vue-router', 'pinia', 'vue-i18n'],
      resolvers: [ElementPlusResolver()]
    }),
    Components({
      resolvers: [ElementPlusResolver()]
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
});
