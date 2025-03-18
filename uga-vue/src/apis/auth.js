import request from '../utils/request/request'

export async function login(data){
    return request({
        url: '/auth/login',
        method: 'post',
        data: data
    })
}