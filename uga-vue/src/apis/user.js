import request from '../utils/request/request'

export  function getUserInfoData(){
    return request({
        url:'/auth/getUserInfo',
        method:'get'
    })
}

export function editUserInfo(data){
  return request({
    url:'/auth/updateUserInfo',
    method:'post',
    data
  })
}
export function requestGrading(data){
    return request({
      url: '/smart/grading',
      method: 'post',
      data,
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
}