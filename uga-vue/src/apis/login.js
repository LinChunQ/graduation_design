import request from '@/request';
import config from '@/request/config';

const baseURL = `${config.baseURL}/auth/oauth/token`

// 登录
export const login = (data) => {
    return request({
        headers: {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        },
        url: baseURL,
        method: 'post',
        data
    });
};

// 退出登录
export const logout = (data) => {
    return request({
        headers: {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        },
        url: `${config.baseURL}/auth/logout2`,
        method: 'post',
        data,
    });
};
