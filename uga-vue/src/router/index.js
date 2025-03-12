import { createRouter, createWebHistory } from 'vue-router'
// 布局文件
import HomePage from '@/views/Home/HomePage.vue'

/**
 * 配置路由
 */
const routes = [
    {path: '/', name: 'HomePage', component: HomePage,},
    { path: '/smart-correction', component: () => import('@/views/SmartCorrections/SmartCorrection.vue') },
    { path: '/history', component: ()=>import('@/views/DataCenter/History.vue') },
    { path: '/user-info', component:()=>import('@/views/User/UserInfo.vue') },
    { path: '/statistics', component: ()=>import('@/views/Statistics/Statistics.vue') },
    { path: '/about', component: ()=>import('@/views/About/About.vue') },
    { path: '/help', component: ()=>import('@/views/Help/Help.vue') },
    {path: '/login', name: 'Login', component: () => import('@/views/Login.vue')},// 直接使用懒加载
    {path: '/:pathMatch(.*)*', redirect: '/404'},
];

const index = createRouter({
    history: createWebHistory(),
    routes
})
export default index