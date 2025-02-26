import request from '@/request';
import config from '@/request/config';

const baseURL = `${config.baseURL}/admin/baseparam`

// 基础参数查询
export const listPage = (data) => {
    const url = `${baseURL}/queryList`;
    return request({ url, method: 'post', data });
};

// 添加
export const save = (data) => {
    const url = `${baseURL}/add`;
    return request({ url, method: 'post', data });
};

// 更新
export const update = (data) => {
    const url = `${baseURL}/update`;
    return request({ url, method: 'post', data });
}

// 删除
export const remove = (id) => {
    const url = `${baseURL}/delete/${id}`;
    return request({ url, method: 'post'});
}

