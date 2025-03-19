import { defineStore } from "pinia"
import { login,register} from '../apis/auth'
import { reactive, ref, computed } from 'vue'

const useAuthStore = defineStore('useAuthStore', () => {
    const token=computed(()=>{
        return localStorage.getItem('token')
    })
    const isLogin=ref(false)

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
        return res
}

return {
    isLogin,
    token,
    clearToken,
    logout,
    handleLogin,
    handleRegister
}

})

export default useAuthStore