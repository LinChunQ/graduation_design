import { defineStore } from "pinia"
import { reactive, ref, computed } from 'vue'
import request from '@/utils/request/request.js'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('userInfo', () => {
  const router = useRouter()
  //用户基本信息
  const userInfo = reactive({
    username: '',
    sex: '',
    age: '',
    email: '',
    phone: '',
    address: '',
    school: '',
    profession: ''
  })
  //保存token
  const token = ref('')
  // 判断是否登录
  const isLoggedIn = false;//computed(() => !!token.value); 测试阶段

  // 方法定义
  const login = async (username, password) => {
    try {
      const response = await request({
        url: '/login',
        method: 'post',
        data: { username, password }
      })

      if (response.token) {
        token.value = response.token
        localStorage.setItem('token', response.token)
        router.push('/')
      }
    } catch (error) {
      console.error("Login failed:", error)
      throw error // 抛出错误以便组件处理
    }
  }

  const getUserInfo = async () => {
    try {
      const response = await request.get('/auth/getUserInfo')
      Object.assign(userInfo, response.data)
    } catch (error) {
      console.error("Get user info failed:", error)
    }
  }

  const editUserInfo = async (newInfo) => {
    try {
      await request.put('/auth/updateUserInfo', newInfo)
      Object.assign(userInfo, newInfo)
    } catch (error) {
      console.error("Update user info failed:", error)
    }
  }

  const clearToken = () => {
    token.value = ''
    localStorage.removeItem('token')
  }

  const logout = () => {
    clearToken()
    router.push('/login')
  }

  // 初始化方法
  const initAuth = () => {
    const storedToken = localStorage.getItem('token')
    if (storedToken) {
      token.value = storedToken
    }
  }

  return {
    userInfo,
    token,
    isLoggedIn,
    login,
    getUserInfo,
    editUserInfo,
    clearToken,
    logout,
    initAuth
  }
})