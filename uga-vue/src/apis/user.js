import request from '../utils/request/request'

export  function getUserInfoData(data){//获取个人信息
    return request({
        url:'/auth/getUserInfo',
        method:'post',
        data,
    })
}

export function editUserInfo(data){ //编辑个人信息
  return request({
    url:'/auth/updateUserInfo',
    method:'post',
    data
  })
}
export function requestGrading(data){//请求打分
    return request({
      url: '/smart/grading',
      method: 'post',
      data,
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
}

export function createCourse(data){ //增加课程
  return request({
    url:'/user/addCourse',
    method:'post',
    data
  })
}

export function getCourseById(){//通过用户id获取该用户下所有课程
  return request({
    url:'/user/getCourseById',
    method:'get'
  })
}

export function deleteCourseById(data){ //删除课程
  return request({
    url:'user/deleteCourse',
    method:'post',
    data
  })
}

export function updateCourse(data){ //编辑课程信息
  return request({
    url:'/user/updateCourse',
    method:'post',
    data
  })
}

export function getTestByCourseId(data){
  return request({
    url:'/user/getTestByCourseId',
    method:'post',
    data
  })
}