import { defineStore } from "pinia"
import { reactive, ref, computed } from 'vue'
import request from '@/utils/request/request.js'
import {getUserInfoData,requestGrading} from '@/apis/user.js'

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
  async function getUserInfo(){
    const res=await getUserInfoData()
    Object.assign(userInfo,res.userInfo)
    localStorage.setItem('userInfo',JSON.stringify(res.userInfo))
    
  }
  const editUserInfo = async (newInfo) => {
    try {
      await request.put('/auth/updateUserInfo', newInfo)
      Object.assign(userInfo, newInfo)
    } catch (error) {
      console.error("Update user info failed:", error)
    }
  }

  async function smartGrading(data){
    const res= await requestGrading(data)
    debugger
  } 


  return {
    userInfo,
    getUserInfo,
    editUserInfo,
    smartGrading
  }
},{persist:true})

export default useUserStore