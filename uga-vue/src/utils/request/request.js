import axios from 'axios';
import config from './config.js';
import { useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';
import {useUserStore} from '@/stores/user';
import i18n from '@/utils/i18n/index.js';
const { t } = i18n.global;
// 手动断言 config 的类型为 AxiosRequestConfig
const axiosConfig = /** @type {import('axios').AxiosRequestConfig} */ (config);
const router = useRouter();
export default function request(options) {

    return new Promise((resolve, reject) => {
        // 创建请求实例
        const instance = axios.create(axiosConfig);
        const userStore = useUserStore();

        // 增加请求拦截处理
        instance.interceptors.request.use(config => {
            const token = localStorage.getItem('token');
            if (!token) {
              router.push('/login');
              return Promise.reject(new Error(t('auth.tokenMissing')));
            }
            config.headers.Token = token;
            return config;
          });
          

        // 增加响应拦截处理
        instance.interceptors.response.use(response => {
            const { code } = response.data;
            if (code !== 200) {
              ElMessage.error(response.data.msg || t('error.operationFailed'));
              return Promise.reject(response.data);
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
                        userStore.clearToken();
                        router.push('/login');
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
                    if (res.code === -2) {
                        router.push('/login');
                    }
                    ElMessage({ type: 'error', message: res.msg || '操作失败', showClose: true });
                    reject(res);
                }
            })
            .catch((error) => {
                reject(error);
            });
    });
}

