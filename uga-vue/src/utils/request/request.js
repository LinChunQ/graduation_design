import axios from 'axios';
import { ElMessage } from 'element-plus';
import useAuthStore from '../../stores/useStoreAuth';

// 全局 Axios 配置
const axiosConfig = {
    baseURL: 'http://localhost:5000',  // API 基础地址
    headers: { 'Content-Type': 'application/json; charset=utf-8' }, // 默认 JSON
    timeout: 5000, // 超时时间
};

export default function request(options) {
    const authStore = useAuthStore();
    const { isLogin, token, clearToken } = authStore;

    return new Promise((resolve, reject) => {
        // 创建 Axios 实例
        const instance = axios.create(axiosConfig);

        // 请求拦截器
        instance.interceptors.request.use(
            (config) => {
                if (!isLogin.value || !token.value) {
                    console.warn('用户未登录或 token 为空');
                } else {
                    config.headers.Token = token.value;
                }
                return config;
            },
            (error) => {
                return Promise.reject(error);
            }
        );

        // 响应拦截器
        instance.interceptors.response.use(
            (response) => {
                const { code, msg, data } = response.data;
                if (code !== 200) {
                    ElMessage.error(msg || '操作失败');
                    return Promise.reject(new Error(msg || '操作失败')); // 让 `catch()` 处理错误
                }
                return data; // 直接返回 data，避免调用者访问 `res.data.data`
            },
            (error) => {
                if (!error.response) {
                    ElMessage.error('网络连接失败，请检查网络！');
                    return Promise.reject(new Error('网络连接失败'));
                }

                const status = error.response.status;
                const codeMap = {
                    400: '请求错误',
                    401: '未授权，请登录',
                    403: '拒绝访问',
                    404: '请求地址不存在',
                    408: '请求超时',
                    500: '服务器内部错误',
                    502: '网关错误',
                    503: '服务不可用',
                    504: '网关超时',
                };

                const errMsg = codeMap[status] || '请求失败';
                ElMessage.error(errMsg);

                if (status === 401) {
                    clearToken(); // 401 需要清除 Token 并重新登录
                }

                return Promise.reject(error);
            }
        );

        // 发送请求
        instance(options)
            .then(resolve) // 直接返回成功的数据
            .catch(reject); // 让调用者处理错误
    });
}
