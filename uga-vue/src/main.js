import { createApp } from 'vue'
import './style.css'
import i18n from './utils/i18n/index.js';
import App from './App.vue'
import { createPinia } from 'pinia';
import piniaPersist from 'pinia-plugin-persist'; // 导入pinia持久化插件
import index from './router/index.js';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import 'normalize.css';  // 使用normalize.css 重置样式
import DataVVue3 from '@kjgl77/datav-vue3'
const  app=createApp(App);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.use(i18n);
const pinia = createPinia();
pinia.use(piniaPersist);
app.use(pinia);
app.use(index);
app.use(ElementPlus);
app.use(DataVVue3);
app.mount('#app');