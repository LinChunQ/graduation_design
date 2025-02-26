
export default {
    // 默认请求方法
    method: 'get' ,
    // 请求url前缀
    baseURL: 'http://localhost:5000',
    // 请求头设置
    headers: {
        "Content-type": "application/json",
    },
    // 设置超时时间
    timeout: 1000,
    // 携带凭证
    withCredentials: true,
    // 返回数据类型
    responseType: 'json'
};
