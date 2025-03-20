import { defineStore } from "pinia"
import { login,register,getUserInfoData} from '../apis/auth'
import { reactive, ref, computed } from 'vue'

const useAuthStore = defineStore('useAuthStore', () => {
    const token=computed(()=>{
        return localStorage.getItem('token')
    })
    const isLogin=ref(false)
    const userInfo=reactive({})

async function handleLogin(data){
    const res= await login(data);
    if(res){
        localStorage.setItem('token',res.token)
        isLogin.value=true;
    }
}

function clearToken() {
    localStorage.removeItem('token')
  }
  function logout() {
      clearToken()
    }
async function handleRegister(data){
        const res=await register(data)
        
}

async function getUserInfo(){
    const res=await getUserInfoData()
    userInfo.value=res.userInfo
    localStorage.setItem('userInfo',JSON.stringify(res.userInfo))
    
}

return {
    isLogin,
    token,
    userInfo,
    clearToken,
    logout,
    handleLogin,
    handleRegister,
    getUserInfo
};

})

export default useAuthStore