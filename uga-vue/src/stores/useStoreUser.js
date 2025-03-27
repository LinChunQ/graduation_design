import { defineStore } from "pinia"
import { reactive, ref, computed } from 'vue'
import request from '@/utils/request/request.js'
import {getUserInfoData,requestGrading,editUserInfo} from '@/apis/user.js'
import { ElMessage } from 'element-plus'

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

  //单个试卷分数
  const singleGrade=ref({})
  async function getUserInfo(){
    const res=await getUserInfoData()
    Object.assign(userInfo,res.userInfo)
    localStorage.setItem('userInfo',JSON.stringify(res.userInfo))
    
  }

  async function updateUserInfo(data){
     await editUserInfo(data)
  }
  async function smartGrading(data){
    const res= await requestGrading(data)
    singleGrade.value=res;
  } 


  return {
    userInfo,
    singleGrade,
    getUserInfo,
    editUserInfo,
    smartGrading,
    updateUserInfo
  }
},{persist:true})

export default useUserStore