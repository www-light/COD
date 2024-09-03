<template>
  <div id="all">
    <div id="nav-div">
      <div id="img-div">
          <img src="../assets/logo1.png" alt="logo" style="width: 90px;">
      </div>
  
      <div id="text-div">
        <nav>
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
    z-index: 100; 
  }
  
  #nav-div{
    /*  border: 1px solid black;   颜色调至black用于查看盒子位置 */
       background-color: #f7f6f4; 
      text-align: left;
      display: flex ; 
      align-items: center; 
  }
  
  #img-div{
    box-sizing: border-box;
    width: 40%;
    padding-left: 25%;
    border: 0px solid black;   /*颜色调至black用于查看盒子位置 */
  }
  
  #text-div{
    box-sizing:border-box;
    width: 20%;
    text-align: center;
    border: 0px solid black;   /*颜色调至black用于查看盒子位置 */
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