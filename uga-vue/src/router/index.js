import { createRouter, createWebHistory } from 'vue-router'
import useAuthStore from '../stores/useStoreAuth';
// 布局文件
import HomePage from '@/views/Home/HomePage.vue'

/**
 * 配置路由
 */
const routes = [
    {path: '/', name: 'HomePage', component: HomePage,},
    { path: '/smart-correction', component: () => import('@/views/SmartCorrections/SmartCorrection.vue') },
    { path: '/history', component: ()=>import('@/views/DataCenter/History.vue') },
    { path: '/header', component: ()=>import('@/views/DataCenter/index.vue') },
    { path: '/user-info', component:()=>import('@/views/User/UserInfo.vue') },
    { path: '/statistics', component: ()=>import('@/views/Statistics/Statistics.vue') },
    { path: '/about', component: ()=>import('@/views/About/About.vue') },
    { path: '/help', component: ()=>import('@/views/Help/Help.vue') },
    { path: '/register', component: ()=>import('@/views/Register.vue') },
    { path: '/notice', component: ()=>import('@/views/Notice/Notice.vue') },
    { path: '/feedback', component: ()=>import('@/views/FeedBack/FeedBack.vue') },
    {path: '/login', name: 'Login', component: () => import('@/views/Login.vue')},// 直接使用懒加载
    {path: '/:pathMatch(.*)*', redirect: '/404'},
];

const index = createRouter({
    history: createWebHistory(),
    routes
})


index.beforeEach((to, from, next) => {
    const authStore = useAuthStore();
    const { isLogin, token} = authStore;
    if (to.path === '/login'||to.path === '/register'|| to.path === '/') {
        next();
    } else {
        if (token === null || token === '' && isLogin) {
            ElMessage({
                message: '请登录后进行相关操作！',
                type: 'warning',
                plain: true,
              })
            next('/login');
        } else{
            next();
        }
    }
})
export default index