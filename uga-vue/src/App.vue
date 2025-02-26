<template>
    <div id="app">
      <Header />
      <router-view></router-view>
    </div>
  <RouterView></RouterView>
</template>

<script setup>
// 导入elementUI 的国际化内容
import { elementLocales } from './utils/i18n/index.js';
import Header  from "@/components/Header.vue";
const { locale } = useI18n();
locale.value = localStorage.getItem('locale') || 'zh-cn';
</script>

<style scoped>
#app {

}
</style>
