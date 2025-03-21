import { defineStore } from "pinia"
import { reactive, ref, computed } from 'vue'
import request from '@/utils/request/request.js'

const useUserStore = defineStore('useUserStore', () => {
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


  return {
    userInfo,
    getUserInfo,
    editUserInfo,
  }
},{persist:true})

export default useUserStore