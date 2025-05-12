import request from '../utils/request/request'

export  function login(data){
    return request({
        url: '/auth/login',
        method: 'post',
        data: data
    })
}

export  function register(data){
    return request({
        url:'/auth/register',
        method:'post',
        data:data
    })
}

export function getCaptcha(data){
    return request({
        url:'/auth/getCaptcha',
        method:'post',
        data:data
    })
}

