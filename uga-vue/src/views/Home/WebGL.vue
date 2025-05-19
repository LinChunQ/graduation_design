<template>
    <div ref="container" class="threejs-container"></div>
</template>

<script setup>
import * as THREE from 'three'
import { ref, onMounted, onBeforeUnmount } from 'vue'
const container = ref(null)

// Three.js 相关变量
let scene, camera, renderer, cube
let animationId = null
  
  const initThreeJS = () => {
    // 场景
    scene = new THREE.Scene()
    scene.background = new THREE.Color('#262626')
  
    // 相机
    const width = container.value.clientWidth
    const height = container.value.clientHeight
    camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100)
    camera.position.set(0, 0, 10)
  
    // 立方体
    const geometry = new THREE.BoxGeometry(2, 2, 2)
    const material = new THREE.MeshBasicMaterial({
      color: 0xffffff,
      wireframe: true
    })

    cube = new THREE.Mesh(geometry, material)
    scene.add(cube)
  
    // 渲染器
    renderer = new THREE.WebGLRenderer({ antialias: true })
    renderer.setSize(width, height)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
    container.value.appendChild(renderer.domElement)
  
    // 动画循环
    const animate = () => {
      animationId = requestAnimationFrame(animate)
      cube.rotation.x += 0.01
      cube.rotation.y += 0.01
      renderer.render(scene, camera)
    }
    animate()
  }
  
  const handleResize = () => {
    if (camera && renderer) {
      const width = container.value.clientWidth
      const height = container.value.clientHeight
      camera.aspect = width / height
      camera.updateProjectionMatrix()
      renderer.setSize(width, height)
    }
  }
  
  onMounted(() => {
    initThreeJS()
    window.addEventListener('resize', handleResize)
  })
  
  onBeforeUnmount(() => {
    window.removeEventListener('resize', handleResize)
    if (animationId) cancelAnimationFrame(animationId)
    if (renderer) {
      renderer.dispose()
      // 清除渲染器 DOM 元素
      if (container.value && container.value.contains(renderer.domElement)) {
        container.value.removeChild(renderer.domElement)
      }
    }
  })
  </script>
  
  <style scoped>
  .threejs-container {
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  </style>