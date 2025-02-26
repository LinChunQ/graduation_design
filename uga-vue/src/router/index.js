import { createRouter, createWebHistory } from 'vue-router'
// 布局文件
import HomePage from '@/views/Home/HomePage.vue'
import SmartCorrection from '../views//SmartCorrections/SmartCorrection.vue';
import History from '../views/DataCenter/History.vue';
import UserInfo from '../views/User/UserInfo.vue';


/**
 * 配置路由
 */
const routes = [
    {path: '/', name: 'HomePage', component: HomePage,},
    { path: '/smart-correction', component: SmartCorrection },
    { path: '/history', component: History },
    { path: '/user-info', component: UserInfo },
    {path: '/login', name: 'Login', component: () => import('@/views/Login.vue')},// 直接使用懒加载
    {path: '/:pathMatch(.*)*', redirect: '/404'},
];

const index = createRouter({
    history: createWebHistory(),
    routes
})
export default index