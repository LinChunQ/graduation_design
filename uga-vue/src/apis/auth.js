import request from '../utils/request/request'

export async function login(data){
    return request({
        url: '/auth/login',
        method: 'post',
        data: data
    })
}

export async function register(data){
    return request({
        url:'/auth/register',
        method:'post',
        data:data
    })
}

export async function getUserInfoData(){
    return request({
        url:'/auth/getUserInfo',
        method:'get'
    })
}