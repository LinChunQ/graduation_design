import { createApp } from 'vue'
import './style.css'
import i18n from './utils/i18n/index.js';
import App from './App.vue'
import { createPinia } from 'pinia';
import index from './router/index.js';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import 'normalize.css';  // 使用normalize.css 重置样式
const  app=createApp(App);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.use(i18n);
const pinia = createPinia();
app.use(pinia);
app.use(index)
app.use(ElementPlus);
app.mount('#app');