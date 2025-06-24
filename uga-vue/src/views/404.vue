<template>
  <div class="not-found">
    <h1>404</h1>
    <p>页面未找到</p>
    <router-link to="/" class="back-home">返回首页</router-link>
  </div>
</template>

<script>
export default {
  name: 'NotFound'
};
</script>

<style scoped>
.not-found {
  text-align: center;
  padding: 50px;
  font-size: 2rem;
  color: #333;
}

.not-found h1 {
  font-size: 5rem;
  margin-bottom: 20px;
}

.not-found p {
  font-size: 1.5rem;
  margin-bottom: 40px;
}

.back-home {
  display: inline-block;
  padding: 10px 20px;
  color: black;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.back-home:hover {
  background-color: #8ae28f;
}
</style>