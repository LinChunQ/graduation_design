import { defineStore } from 'pinia';
import { getDict } from '@/apis/dict';
export const DICT = {
  vehicleType: '1819698002348158977',
  plateColor: '1819698002348158978',
}

export const useDictStore = defineStore('dict', {
  // 类似于data
  state: () => ({
    data: {}
  }),
  // 类似于computed计算属性
  getters: {
    dict(state, type) {
      return state.data[type] || [];
    }
  },
  // 类似于vue2中的methods
  actions: {
    setDict(type, data) {
      this.data[type] = data;
    },
    format(type, value) {
      const data = this.data[type];
      if (data) {
        const obj = data.find((item) => value == item.value);
        return obj?.label || '';
      }
    },
    async getDict(type, callback) {
      const id = DICT[type];
      if (!id) throw new Error('字典类型不存在');
      // 如果store中存在，则从store中直接获取
      if(this.data[type]) {
        // 执行回调
        callback && callback();
        return this.data[type];
      }
      // 获取该类型字典数据
      const res = await getDict(id);
      const resData = res?.data || [];
      // 提取关键数据转换为{label: '', value: ''}
      const data = resData.map((item) => ({ label: item.name, value: item.value }));
      // 存储数据
      this.setDict(type, data);
      // 执行回调
      callback && callback();
      // 返回数据
      return data;
    }
  }
});
