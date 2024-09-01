<template>
<div id="all">

  <Header/>

  <div style=" border: 1px solid white">
    <!-- 路由出口 -->
    <router-view/>
  </div>

  <Footer/>
  
</div>
</template>

<script>
// Header组件
import Header from './components/Header.vue'
import Footer from './components/Footer.vue';
export default{
  components:{
    Header,
    Footer,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  text-align: center;

  color: #2c3e50;
  
}

#footer-div{
  width: 100%;
  z-index: -1;  
}

</style>

