<template>  
    <div class="home">  
      <h1>保护动物，人人有责</h1>  
      <p>欢迎来到我们的保护动物网站，这里汇聚了关于如何保护野生动物的信息。</p>  
      <button @click="showMoreInfo">了解更多</button> 
      <component :is="tabComponent"></component> 
    </div>  
  </template>  
    
<script>
import AnimalsList from '../components/AnimalsList.vue';
export default{
    name: 'HomePage',  
    data(){
      return{
        tabComponent:"",
      }
    },
    methods: {  
      showMoreInfo() {  
        alert('请访问我们的博客和资源页面获取更多信息！'); 
        this.tabComponent = this.tabComponent==""?"AnimalsList":"" 
      }  
    } ,
    components:{
      AnimalsList,
    }
  }  
</script>  

<style scoped>  
  .home {  
    text-align: center;  
    padding: 20px;  
  }  
</style>