<template>
<div id="all">
  <div id="nav-div">
    <div id="img-div">
        <img src="../assets/logo1.png" alt="logo" style="max-width: 90px;">
    </div>

    <div id="nav-div">
      <nav style="border: 1px solid white;">
        <router-link to='/'>Home</router-link>&nbsp;&nbsp;|&nbsp;&nbsp; 
        <router-link to="/about">About</router-link>&nbsp;&nbsp;|&nbsp;&nbsp;  
        <router-link to="/detect">Detect</router-link>
      </nav>
    </div>

  </div>
    <hr> 

</div>
</template>

<style scoped>

#all{
  position: sticky; 
  top:0px; 
}

#nav-div{
    height: 100px;
    border: 1px solid white;  /* 颜色调至black用于查看盒子位置 */
     background-color: #f7f6f4; 
    text-align: start;
    display: flex ; 
    align-items: center; 
}

#img-div{
  padding-left: 25%;
  width: 17%;
  border: 1px solid white;  /* 颜色调至black用于查看盒子位置 */
}

#nav-div{
  border: 1px solid white;  /* 颜色调至black用于查看盒子位置 */
}

nav {
  padding: 0px;
}

nav a {
  font-size: 120%;
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

hr{
  height: 2px;
  margin: 0px;
  background-color: #42b983;

}

</style>