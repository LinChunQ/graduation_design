<template>
  <div id="app">
    <Header/>
    <main class="content-wrapper">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup>
// 导入elementUI 的国际化内容
import { elementLocales } from './utils/i18n/index.js';
import Header  from "@/components/Header.vue";
const { locale } = useI18n();
locale.value = localStorage.getItem('locale') || 'zh-cn';
</script>

<style lang="scss" scoped>
#app {
  /* 核心保护设置 */
  min-width: 400px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f0f0f0;
  .content-wrapper {
    flex: 1;
    min-height: calc(100vh - 80px); // 80px为header高度
    overflow: auto;
  }
}
</style>
