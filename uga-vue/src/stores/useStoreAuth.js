import { defineStore } from "pinia"
import { login,register} from '../apis/auth'
import { reactive, ref, computed } from 'vue'
import useUserStore from '../stores/useStoreUser'


const useAuthStore = defineStore('useAuthStore', () => {
    const token=computed(()=>{
        return localStorage.getItem('token')
    })
    const isLogin=ref(false)
    const userStore=useUserStore()
    const role=ref('1')
    const {userInfo} =userStore

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
      userInfo.value={};
      localStorage.removeItem('userInfo')
}
async function handleRegister(data){
        const res=await register(data)
        
}



return {
    isLogin,
    token,
    userInfo,
    role,
    clearToken,
    logout,
    handleLogin,
    handleRegister,
};


})

export default useAuthStore