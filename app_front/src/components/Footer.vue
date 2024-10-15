<script setup lang="ts">
import router from '@/router';
</script>

<template>
  <div id="footer-div" style="border: 0px solid black;">
  <hr id="hr2"> 
    <footer> 
        <!-- <p style="color:grey;">&copy; 2024 小型动物检测网站. 版权所有.</p>   -->
        <div style="display: flex;">
          <div class="logo"><img src="../assets/logo1.png" alt="logo" style="height: 100px;"></div>
          <div>
            <div style="display: flex;">
              <div class="content">
                <router-link to="/" class="link"><div class="item">网站首页</div></router-link>
                <router-link to="/about#protection" class="link"><div class="item">生态智慧 & 保护实践</div></router-link>
                <router-link to="/about#introduction" class="link"><div class="item">小型野生动物科普</div></router-link>
                <router-link to="/detect" class="link"><div class="item">小型动物检测</div></router-link>
              </div>
              <div class="content">              
                <div class="item">联系我们：</div>
                <div class="item">邮箱：2842776238@qq.com</div>
                <div class="item">电话：19396005525</div>
              </div>
            </div>
            <div>
              <div style="padding-top: 20px;">cpyright© 小动物的神奇世界 All Right Reserved.</div>
            </div>
          </div>         
        </div>
    </footer> 
  </div>
</template>



<style scoped>

footer {    
padding: 10px 0;  
font-size:x-small;
text-align: center; 
height: 150px;
background-color: #f7f6f4;
color: dimgrey;
}

.logo {
  box-sizing: border-box;
  max-height: 200px;
  width: 280px;
  margin-left: 250px;
  border: 0px solid black;
}

.content {
  display: block;
  text-align: left;
  width: 200px;
  padding: 0px 10px;
}

.item {
  margin: 10px 10px;
  color:dimgray;
}

.link {
  text-decoration: none;
}

.link :hover{
  color: #42b983;
}

#hr2{
  height: 0px;
  background: rgb(255, 255, 255);
}

</style>