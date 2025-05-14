import request from '../utils/request/request'

export function addNotice(data){
    return request({
        url:'/sys/addNotice',
        method:'post',
        data
    })
}

export function getNotice(data){
    return request({
        url:'/sys/getNotice',
        method:'post',
        data
    })
}

export function deleteNotice(data){
    return request({
        url:'/sys/delNotice',
        method:'post',
        data
    })
}

export function addNoticeType(data){
    return request({
        url:'/sys/addNoticeType',
        method:'post',
        data
    })
}

export function getNoticeType(){
    return request({
        url:'/sys/getNoticeType',
        method:'post',
    })
}

export function deleteNoticeType(data){
    return request({
        url:'/sys/delNoticeType',
        method:'post',
        data
    })
}

export function addFeedBack(data){
    return request({
        url:'/sys/addFeedBack',
        method:'post',
        data
    })
}

export function getFeedBack(data){
    return request({
        url:'/sys/getFeedBack',
        method:'post',
        data
    })
}