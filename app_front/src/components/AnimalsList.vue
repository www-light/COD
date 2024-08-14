<template>  
    <div>  
      <h2>受保护动物列表</h2>  
      <ul>  
        <li v-for="animal in animals" :key="animal.id">  
          <img :src="animal.image" alt="" style="width: 100px; height: 100px;">  
          {{ animal.name }} - {{ animal.description }}  
        </li>  
      </ul>  
    </div>  
  </template>  
    
  <script>  
  export default {  
    name: 'AnimalsList',  
    data() {  
      return {  
        animals: [  
          { id: 1, name: '大熊猫', description: '中国特有的珍稀动物', image: 'path/to/panda.jpg' },  
          { id: 2, name: '北极熊', description: '生活在北极的熊种', image: 'path/to/polarbear.jpg' },  
          // 更多动物...  
        ]  
      }  
    }  
  }  
  </script>  
    
  <style scoped>  
  ul {  
    list-style-type: none;  
    padding: 0;  
  }  
    
  li {  
    margin-bottom: 10px;  
    display: flex;  
    align-items: center;  
  }  
    
  img {  
    margin-right: 10px;  
  }  
  </style>