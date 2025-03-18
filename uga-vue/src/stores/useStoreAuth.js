import { defineStore } from "pinia"
import { login,register} from '../apis/auth'
import { reactive, ref, computed } from 'vue'

const useAuthStore = defineStore('useAuthStore', () => {
    const token=computed(()=>{
        return localStorage.getItem('token')
    })
    const isLogin=computed(()=>{
        return token.value!==null
    })

async function handleLogin(data){
    const res= await login(data);
    if(res.data){
        isLogin.value=true;
        localStorage.setItem('token',res.data.token)
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
        debugger
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