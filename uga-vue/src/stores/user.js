import { defineStore } from "pinia"
import request from '../utils/request/request.js'
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const useUserStore = defineStore('userInfo', {
    // defineStore('userInfo',{})  userInfo就是这个仓库的名称name
    state: () => ({
        username:'',// 姓名
            sex:'',//性别
            age:'', // 年龄
            email:'',//邮件
            phone:'',//手机号
            address:'',//地址
            school:'',//学校
            profession:'',//专业
            token:'',
    }),
    actions:{
            // 登录方法
            async login(username, password) {
                const router = useRouter();
                // 清空错误信息
                this.token = null;
                // 封装登录请求的参数
                const data = {
                    username,
                    password,
                };
                try {
                    // 发送登录请求
                    const response = await request({
                        url: '/login',  // 登录接口
                        method: 'post',
                        data,
                    });
                    // 假设登录成功后返回 token
                    if (response.token) {
                        this.token = response.token;  // 更新 token
                        localStorage.setItem('token', response.token);  // 将 token 存储到 localStorage
                        router.push('/home');  // 登录成功后跳转到首页
                    }
                } catch (error) {
                    // 登录失败时的处理
                    console.error("Login failed:", error);
                    // 可以根据需要处理错误信息，给用户反馈
                }
        },
        getUserInfo(){ //获取用户信息
           request().get('/auth/getUserInfo').then()
        },
        editUserInfo(){ //修改用户信息
            request().put()
        },
        clearToken(){
            this.token = null;
            localStorage.removeItem('token');  // 清除 token
        },
        // 清除 token（登出功能）
        logout() {
            this.clearToken()
        },
        // 通过 token 判断是否已经登录
        isLoggedIn() {
            return !!this.token;
        },
    }
})

export default useUserStore