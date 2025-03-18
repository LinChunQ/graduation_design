import axios from 'axios';
import { ElMessage } from 'element-plus';
import useAuthStore from '../../stores/useStoreAuth';
const axiosConfig ={
    baseURL: 'http://localhost:5000',
    // 请求头设置
    headers: {'Content-Type': 'application/json; charset=utf-8'},
    timeout: 5000,
}
export default function request(options) {
    const authStore = useAuthStore(); // 调用 useAuthStore 函数获取 store 实例
    const { isLogin, token, clearToken } = authStore;
    return new Promise((resolve, reject) => {
        // 创建请求实例
        const instance = axios.create(axiosConfig);
        // 增加请求拦截处理
        instance.interceptors.request.use(config => {
            if (token!=''&&isLogin.value){
                ElMessage.error("登陆状态出错!");
              return Promise.reject(new Error('not found token !'));
            }
            if(isLogin.value){
                config.headers.Token = token.value;
            }
            return config;
          });
          

        // 增加响应拦截处理
        instance.interceptors.response.use(response => {
            const { code,msg } = response.data;
            if (code !== 200) {
                console.log(msg)
              ElMessage.error(msg);
             return ;
            }
            return response.data;
            },
            (err) => {
                const codeMap = {
                    400: '请求错误',
                    401: '未授权，请登录',
                    403: '拒绝访问',
                    404: '请求地址出错',
                    408: '请求超时',
                    500: '服务器内部错误',
                    501: '服务未实现',
                    502: '网关错误',
                    503: '服务不可用',
                    504: '网关超时',
                    505: 'HTTP版本不受支持'
                };
                if (err && err.response) {
                    const status = err.response.status;
                    const errMsg = codeMap[status] || '';
                    ElMessage({ type: 'error', message: errMsg, showClose: true });
                    if (status === 401) {
                        clearToken();
                    }
                }
                return Promise.reject(err);
            }
        );

        // 处理正常返回的数据
        instance(options)
            .then((res) => {
                if (res || res.code === 200) {
                    resolve(res);
                } else {
                    ElMessage({ type: 'error', message: res.msg || '操作失败', showClose: true });
                    reject(res);
                }
            })
            .catch((error) => {
                reject(error);
            });
    });
}

