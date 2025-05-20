<template>
  <div id="app">
    <header>
      <Header v-show="true"/>
    </header>
    <main class="content-wrapper">
      <router-view></router-view>
    </main>
    <footer>
      <Footer v-show="true"/>
    </footer>
  </div>
</template>

<script setup>
import Header  from "@/components/Header.vue";
import Footer  from "@/components/Footer.vue";
</script>

<style lang="scss" scoped>
#app {
  /* 核心保护设置 */
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  min-height: 100vh;
  min-width: 40vw;
}

header {
  flex: 0 0 auto;
  z-index: 999;
}

main {
  flex: 1 1 auto;
}

footer {
  flex: 0 0 auto;
  z-index: 999;
}
</style>
