import { defineStore } from "pinia"
import { login} from '../apis/auth'
import { reactive, ref, computed } from 'vue'

const useAuthStore = defineStore('useAuthStore', () => {
const isLogin=ref(false)
const token=ref('')

function getToken(){
    //token.value= localStorage.getItem('token');
}

async function handleLogin(data){
    const res= await login(data);
    debugger
    if(res.code==200){
        token.value=res.data.token
        localStorage.setItem('token',token.value)
        isLogin.value=true
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

return{
    isLogin,
    token,
    clearToken,
    logout,
    initAuth,
    handleLogin
}

})

export default useAuthStore