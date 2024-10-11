<template>  
  <div id="all">  
    <div id="nav-div">  
      <div id="img-div">  
        <img src="../assets/logo1.png" alt="logo" style="width: 90px;">  
      </div>  
  
      <div id="text-div">  
        <nav>  
          <router-link to='/' class="dropbtn">Home</router-link>&nbsp;&nbsp;|&nbsp;&nbsp;  
          <div class="dropdown">  
            <router-link to="/about" class="dropbtn">About</router-link>  
            <div class="dropdown-content"> 
              <router-link to="/about#protection" class="dropdown-link">生态智慧 & 保护实践</router-link> 
              <router-link to="/about#introduction" class="dropdown-link">小型野生动物科普</router-link>                  
            </div>  
          </div>  
          &nbsp;&nbsp;|&nbsp;&nbsp;  
          <router-link to="/detect" class="dropbtn">Detect</router-link>  
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
    z-index:100;
  }
  
  #nav-div{
       background-color: #f7f6f4; 
      text-align: left;
      display: flex ; 
      align-items: center; 
  }
  
  #img-div{
    box-sizing: border-box;
    width: 40%;
    padding-left: 25%;
    border: 0px solid black;   
  }
  
  #text-div{
    box-sizing:border-box;
    width: 20%;
    text-align: center;
    border: 0px solid black;  
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

  .dropdown {  
    position: relative;  
    display: inline-block;  
  }  
    
  .dropdown-content {  
    display: none;  
    position: absolute;  
    background-color: #f9f9f9;  
    min-width: 180px;  
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);  
    z-index: 1;  
    text-align: left;  
  }  
    
  .dropdown-content .dropdown-link {  
    color: #2c3e50;  
    padding: 12px 16px;  
    text-decoration: none;  
    display: block;  
    cursor: pointer;  
    font-size: 14px;  
    font-weight: bold; 
  }  
    
  .dropdown:hover .dropdown-content {  
    display: block;  
  }  
    
  .dropbtn {  
    font-size: 120%;  
    font-weight: bold;  
    color: #2c3e50;  
  }  
    
  .dropbtn:hover {  
    color: #42b983;  
  }  
    
  /* 悬停 */  
  .dropdown-content .dropdown-link:hover {  
    background-color: #f1f1f1;  
    color: #42b983; 
  }  
  </style>
  
