<template>  
 
  <div class="about">  
    <!-- 纵向导航栏 -->  
    <nav class="sidebar-nav">  
      <ul>  
        <li @click="setActiveSection('introduction')"><router-link to="/about#introduction" class="nav-link">小体型野生动物<br>概览</router-link></li>  
        <li @click="setActiveSection('importance')"><router-link to="/about#importance" class="nav-link">生态与人类<br>价值</router-link></li>  
        <li @click="setActiveSection('protection')"><router-link to="/about#protection" class="nav-link">保护<br>行动与方法</router-link></li>  
      </ul>  
    </nav>  
  
    <!-- 内容区域 -->  
    <div class="content" id="contentBox">  
      <!-- 小体型野生动物概览 -->  
      <section v-show="activeSection === 'introduction'" id="introduction" class="section">  
        <h1>Overview of small wild animals</h1>  
        <p class="indented-text">在生物学界，小体型野生动物指的是那些体型相对较小，通常具有独特生态适应性和生存策略的物种。这些动物广泛分布于各种生态系统中，从热带雨林到高山草甸，从淡水湖泊到海洋深处，均可见其踪迹。它们虽然体型不大，但在生物多样性和生态平衡中，乃至人类生活生产中扮演着至关重要的角色。</p>  
        <h3 class="h3-custom">小型哺乳动物</h3>  
        <ul>  
          <li>  
            <img src="/about.jpg" alt="伶鼬" style="width: 200px; height: auto;margin-left:45px;">  
            <p>  
              <span class="highlighted-text">伶鼬</span>：是地球上体型最小的食肉目哺乳动物之一<br>  
              体重范围在30-250克之间<br>  
              其主要栖息在北半球的森林和草原。<br>  
              它们拥有敏锐的视觉、听觉、嗅觉以及锐利的爪子和牙齿，能捕捉比自身大数倍的猎物<br>  
              此外，伶鼬的毛色随季节变化，冬季雪白，夏季为褐色或啡色，这种保护色有助于其在不同季节的隐蔽和捕猎  
            </p>
             </li>  
          <li>  
            <img src="/about0.jpg" alt="三趾跳鼠" style="width: 200px; height: 200px;margin-left:45px;">  
            <p>  
              <span class="highlighted-text">三趾跳鼠</span>：是跳鼠科中的一种小型哺乳动物<br>体型中等偏小，体长约101-155毫米，尾长超过体长1/3<br>其头大、眼大，后肢特别发达，以其卓越的跳跃能力和杂食性饮食习惯著称<br>它们主要生活在亚洲的沙漠和半沙漠地区，夜间活动，白天则藏身于沙质洞穴中。</p>  
          </li>  
          <li>  
            <img src="/about1.jpg" alt="指猴" style="width: 200px; height: auto;margin-left:45px;">  
            <p>
              <span class="highlighted-text">指猴</span>：又称绒猴或指灵长，是世界上最小的灵长类动物之一<br>成年指猴身高仅10-12厘米，体重80-100克，体型小巧而独特<br>它们分布于马达加斯加岛,以其独特的中指和夜间捕食树木中蛀虫的习性而知名<br>但由于人类活动和栖息地破坏，目前数量极为稀少，残存不足80只，目前处于极度濒危状态。</p>  
          </li>  
        </ul>  
  
        <!-- 其他类别... -->  
  
        <h3 class="h3-custom">小型节肢动物</h3>    
        <ul> 
           <li>    
       <img src="/about2.jpg" alt="蜘蛛" style="width: 270px; height: 210px;margin-right:-20px;" >    
       <p><span class="highlighted-text">蜘蛛</span>: 是蛛形纲蜘蛛目（Araneae）的通称<br>体长差异极大，从不足1毫米到超过90毫米不等，广泛分布于全球<br>身体分为头胸部和腹部，腹部柔软，通常具有多种图案和颜色，用于伪装或警告天敌<br>依靠结网或直接追捕等方式捕食，部分种类具有复杂的求偶和交配行为<br>部分蜘蛛能分泌毒液注入猎物体内使其麻痹或死亡，有的则利用刺毛或强力的螯肢进行防御 </p>    
          </li>    
          <li>    
       <img src="/about3.jpg" alt="蝎子" style="width: 270px; height: 200px;margin-right:-20px;">    
       <p><span class="highlighted-text">蝎子</span>:属于蛛形纲蝎目（Scorpionida）<br>形态独特，头胸部前端有强大的螯肢和螯足，尾部末端藏有毒腺和尾刺<br>以昆虫等小型生物为食，常在夜间利用敏锐的嗅觉和触觉寻找猎物，具有高度的防御和攻击能力<br>蝎子是胎生的，幼蝎在母蝎背上孵化并受到保护直至能够独立生活</p>    
          </li>    
          </ul> 
  
        <!-- 青蛙、蜥蜴、鸟类等部分... -->  
  
        <h3 class="h3-custom">青蛙</h3>  
        <ul class="reversed-layout"> 
          <li> 
        <img src="/about4.jpg" alt="青蛙" style="width: 250px; height: 250px;margin-right:70px;">
        <p> <span class="highlighted-text">青蛙</span>：两栖无尾目小型种，生态适应性强<br>拥湿润且富含血管的皮肤，调节体温和水分平衡，且赋予独特的辅助呼吸能力<br>后肢强健，擅长跳跃。主要以昆虫、蜘蛛等小型无脊椎动物为食<br>对控制这些害虫的数量、维护水生与陆生生态系统的平衡起着至关重要的作用<br>此外，其繁殖行为如产卵于水中、变态发育等生物学特性。使其成为进化生物生态学研究的重要对象</p>  
      </li> </ul> 

        <h3 class="h3-custom">蜥蜴</h3>  
        <ul class="reversed-layout">  <li>
        <img src="/about5.jpg" alt="蜥蜴" style="width: 320px; height: 220px;margin-right:70px;"> 
        <p><span class="highlighted-text">蜥蜴</span>：是小型种类<br>体表覆盖角质鳞片，减少水分蒸发并提供保护<br>四肢灵活，食性多样，包括肉食、杂食及少数草食<br>具备变色、断尾等生存策略，展现高度生态适应性，是生物多样性研究的典范。</p>  
      </li> </ul> 

        <h3 class="h3-custom">鸟类</h3>  
        <ul class="reversed-layout">  <li>
        <img src="/about6.jpg" alt="鸟类" style="width: 320px; height: 220px;margin-right:70px;">
        <p> <span class="highlighted-text">鸟类</span>：其中的小型鸟类<br>具有高效双重呼吸系统和四腔心脏支持高能耗飞行<br>骨骼轻薄中空，胸肌发达，提供飞行动力<br>既是捕食者也是被捕食者，食物多样，对生态平衡和生物多样性至关重要<br>复杂社群行为和繁殖策略，是生态学和环境保护研究的重要指示物种</p>  
      </li> </ul> 
    </section>  
  
    <!-- 生态与人类价值 -->
   
    <section v-show="activeSection === 'importance'" id="importance" class="section">
      <div class="section1">
      <h2>小体型野生动物：生态平衡的微动力<br>Small wild animals: The micro driving force for ecological balance.</h2>
      <div class="box">
        <div class="box1">
          <div class="image">
            <img class="image__img" src="/about26.png" alt="Bricks">
            <div class="image__overlay">
              <div class="image__title">Biodiversity</div>
              <p class="image__description">
                Ecosystem Stability
              </p>
            </div>
            <div class="image__description-box">
              <h3>生物多样性与生态系统稳定性</h3>
              <p>小体型野生动物对维持生物多样性至关重要。它们通过生态关系构建复杂食物网和生态链，数量稳定直接影响生态系统平衡。</p>
            </div>
          </div>
        </div>
    
        <div class="box2">
          <div class="image">
            <img class="image__img" src="/about29.png" alt="Bricks">
            <div class="image__overlay">
              <div class="image__title">Material Cycling</div>
              <p class="image__description">
                Energy Flow
              </p>
            </div>
            <div class="image__description-box">
              <h3>环境指示作用</h3>
              <p>小体型野生动物对生存环境敏感，常被用作环境质量的指示物种。其种群数量及分布范围的变迁等可反映出生态系统健康状况和环境质量的变化。</p>
            </div>
          </div>
        </div>
    
        <div class="box3">
          <div class="image">
            <img class="image__img" src="/about28.png" alt="Bricks">
            <div class="image__overlay">
              <div class="image__title">Environmental Indicator </div>
              <p class="image__description">
                Role
              </p>
            </div>
            <div class="image__description-box">
              <h3>物质循环与能量流动</h3>
              <p>小体型野生动物采食植物、排泄粪便，推动生态系统物质循环。同时，它们也是分解者的重要食物来源，加速有机物质分解和营养元素再循环。</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section2">
      <h2>小体型野生动物：人类福祉的灵动贡献<br>Small wild animals: The lively contribution to human well-being.</h2>
      <div class="box">
        <div class="box1">
          <div class="image">
            <img class="image__img" src="/about27.png" alt="Bricks">
            <div class="image__overlay">
              <div class="image__title">Cultural & symbolic</div>
              <p class="image__description">
                value
              </p>
            </div>
            <div class="image__description-box">
              <h3>文化与象征价值</h3>
              <p>小型野生动物如虎斑蝶，象征美丽与自由，连接多元文化，激发人类对自然的尊重与情感共鸣。</p>
            </div>
          </div>
        </div>
    
        <div class="box2">
          <div class="image">
            <img class="image__img" src="/about30.png" alt="Bricks">
            <div class="image__overlay">
              <div class="image__title">scientific research</div>
              <p class="image__description">
                value
              </p>
            </div>
            <div class="image__description-box">
              <h3>科学研究价值</h3>
              <p>小体型野生动物独特的生理结构和行为习性为生命科学研究提供重要材料。例如，在生物医学中，可作为实验动物模拟人类疾病，为治疗和药物研发提供依据。</p>
            </div>
          </div>
        </div>
    
        <div class="box3">
          <div class="image">
            <img class="image__img" src="/about31.jpg" alt="Bricks">
            <div class="image__overlay">
              <div class="image__title">ecological service </div>
              <p class="image__description">
                function
              </p>
            </div>
            <div class="image__description-box">
              <h3>生态服务功能</h3>
              <p>小体型野生动物提供重要生态服务功能。如蝙蝠授粉；猫头鹰控制害虫；松鼠促进种子扩散和植物繁殖。这些对人类生产生活有直接促进作用。</p>
            </div>
          </div>
        </div>
      </div>

      <div class="section3">
        <h2>小体型野生动物：研究领域的奇妙宝藏<br>Small wild animals: A wonderful treasure in the field of research.</h2>
        <div class="box">
          <div class="box1">
            <div class="image">
              <img class="image__img" src="/about32.png" alt="Bricks">
              <div class="image__overlay">
                <div class="image__title">Protect biodiversity</div>
                <p class="image__description">
        
                </p>
              </div>
              <div class="image__description-box">
                <h3>保护生物多样性</h3>
                <p>研究与保护小体型野生动物，是有效维护生物多样性的关键。生物多样性作为地球生命系统的核心，对生态平衡与人类福祉至关重要。</p>
              </div>
            </div>
          </div>
      
          <div class="box2">
            <div class="image">
              <img class="image__img" src="/about33.png" alt="Bricks">
              <div class="image__overlay">
                <div class="image__title">Promote ecological </div>
                <p class="image__description">
                  research
                </p>
              </div>
              <div class="image__description-box">
                <h3>促进生态学研究</h3>
                <p>小体型野生动物作为生态系统重要组成，通过研究可深入了解生态系统结构与功能、物种间相互作用等科学问题，为生态保护与管理提供科学依据。</p>
              </div>
            </div>
          </div>
      
          <div class="box3">
            <div class="image">
              <img class="image__img" src="/about34.png" alt="Bricks">
              <div class="image__overlay">
                <div class="image__title">Improve human quality  </div>
                <p class="image__description">
                  of life
                </p>
              </div>
              <div class="image__description-box">
                <h3>提升人类生活质量</h3>
                <p>保护小体型野生动物可维护生态平衡与生物多样性，提升人类生活质量，如促进农业生产、激活地方经济、保障人类健康。</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </section>

   
  

      
      <!-- 保护行动与方法--> 
      <section v-show="activeSection === 'protection'" id="protection" class="section">
       
        <!-- 轮播图部分 -->
        <div class="carousel-container" v-if="activeSection === 'protection'">
          <div class="carousel-slide" :style="{ backgroundImage: 'url(' + currentImage + ')' }">
            <div class="carousel-text">
              <h2>Protect Tiny Lives, <br>Build a Shared Ecological Home</h2>
              <p>Small-bodied wildlife, the starting point of great love. Demonstrating respect and <br>care for nature from the tiniest details, let us join hands to shelter a sky of survival for them, making love boundless and the ecology more harmonious.</p>
              </div>
          </div>
        </div>

        <div class="carousel-indicators">
          <div class="carousel-indicator" v-for="(image, index) in images" :class="{ active: index === currentIndex }"></div>
        </div>

        <!-- 内容部分 -->
        <div class="protection-content">
          <!-- 第一部分 -->
          <div class="section-group">
            <div class="image-group">
              <img src="/about11.jpg" alt="Image 1" style="width: 150px; height: 150px;position: relative; left: 10px; top: 70px;">
              <div class="right-images">
                <img src="/about12.jpg" alt="Image 2" style="width: 180px; height: 95px;position: relative; left: 20px; top: 85px;">
                <img src="/about13.jpg" alt="Image 3" style="width: 180px; height: 95px;position: relative; left: 20px; top: -115px;">
              </div>
            </div>
            <div class="text-group">
              <h2>保护栖息地</h2>
              <p>Habitat Conservation</p>
              <p>在保护小体型野生动物的栖息地方面，我们需构建全方位的保护网络。通过精准划定并严格管理自然保护区，为这些生物提供免受人类活动侵扰的净土。同时，实施生态修复工程，针对受损栖息地实施定制化恢复计划，如植被恢复与生态廊道建设，以恢复其自然生态功能与生物多样性。此外，制定并执行科学的管理规划，包括持续监测、效果评估及动态调整保护策略，确保栖息地得到有效而可持续的保护。</p>
              <ul class="keyword-list">
                <li><span class="green-dot">&#8226;</span>建立自然保护区</li>
                <li><span class="green-dot">&#8226;</span>恢复受损栖息地</li>
                <li><span class="green-dot">&#8226;</span>科学管理</li>
              </ul>
            </div>
          </div>
      
          <!-- 第二部分 -->
          <div class="section-group">
            <div class="image-group new-image-group">
              <img src="/about14.jpg" alt="New Image 1" style="width: 150px; height: 150px;position: relative; left: 10px; top: 70px;">
              <div class="right-images new-right-images">
                <img src="/about15.jpg" alt="New Image 2" style="width: 180px; height: 95px;position: relative; left: 20px; top: 50px;">
                <img src="/about16.jpg" alt="New Image 3" style="width: 180px; height: 95px;position: relative; left: 20px; top: -153px;">
              </div>
            </div>
            <div class="text-group new-text-group">
              <h2>控制人为威胁</h2>
              <p>Control Human Threats</p>
              <p>针对人为威胁的控制，我们需采取综合手段以减轻对小体型野生动物的负面影响。减少环境污染是首要任务，通过严格的环境监管，限制有害物质的排放，保护它们免受污染之害。同时，强化法律法规建设，严厉打击非法捕猎与贸易活动，从源头上切断非法链条。此外，在自然保护区等敏感区域实施合理的游客管理政策，平衡旅游发展与生态保护，确保野生动物免受不必要的干扰。</p>
              <ul class="keyword-list new-keyword-list">
                <li><span class="green-dot">&#8226;</span>减少污染</li>
                <li><span class="green-dot">&#8226;</span>禁止非法贸易</li>
                <li><span class="green-dot">&#8226;</span>限制游客活动</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 第三部分 -->
<div class="section-group">
  <div class="image-group new-image-group-2">
    <img src="/about17.png" alt="New Image 1" style="width: 150px; height: 150px;position: relative; left: 10px; top: 70px;">
    <div class="right-images new-right-images-2">
      <img src="/about18.png" alt="New Image 2" style="width: 180px; height: 95px;position: relative; left: 20px; top: 80px;">
      <img src="/about19.png" alt="New Image 3" style="width: 180px; height: 95px;position: relative; left: 20px; top: -123px;">
    </div>
  </div>
  <div class="text-group new-text-group-2">
    <h2>加强监测与研究</h2>
    <p>Strengthen Monitoring and Research</p>
    <p>监测与研究是科学保护的基础。我们需建立健全小体型野生动物的监测体系，利用现代科技手段如遥感、GIS及大数据分析，精准掌握其种群动态与生态习性。同时，深入开展遗传学研究，揭示其遗传多样性与进化历程，为制定保护策略提供遗传学层面的支持。此外，生态系统研究也不可或缺，通过解析它们在生态系统中的功能与角色，为整体生态保护提供科学依据。</p>
    <ul class="keyword-list new-keyword-list-2">
      <li><span class="green-dot">&#8226;</span>种群监测</li>
      <li><span class="green-dot">&#8226;</span>遗传学研究</li>
      <li><span class="green-dot">&#8226;</span>生态系统研究</li>
    </ul>
  </div>
</div>

<!-- 第四部分 -->
<div class="section-group">
  <div class="image-group new-image-group-3">
    <img src="/about20.jpg" alt="New Image 1" style="width: 150px; height: 150px;position: relative; left: 10px; top: 70px;">
    <div class="right-images new-right-images-3">
      <img src="/about21.jpg" alt="New Image 2" style="width: 180px; height: 95px;position: relative; left: 20px; top: 100px;">
      <img src="/about22.jpg" alt="New Image 3" style="width: 180px; height: 95px;position: relative; left: 20px; top: -103px;">
    </div>
  </div>
  <div class="text-group new-text-group-3">
    <h2>促进公众参与与教育</h2>
    <p>Promote Public Participation and Education</p>
    <p>公众参与与教育是推动保护工作的关键力量。我们需广泛传播保护理念，利用多种渠道提升公众对小体型野生动物保护的认识与重视。通过举办教育活动、开展科普宣传及建立互动平台，激发公众的保护热情与参与度。同时，鼓励社会各界积极参与保护行动，形成政府主导、社会参与的良好氛围。</p>
    <ul class="keyword-list new-keyword-list-3">
      <li><span class="green-dot">&#8226;</span>提高公众意识</li>
      <li><span class="green-dot">&#8226;</span>开展教育活动</li>
      <li><span class="green-dot">&#8226;</span>鼓励公众参与</li>
    </ul>
  </div>
</div>

<!-- 第五部分 -->
<div class="section-group">
  <div class="image-group new-image-group-4">
    <img src="/about23.jpg" alt="New Image 1" style="width: 150px; height: 150px;position: relative; left: 10px; top: 70px;">
    <div class="right-images new-right-images-4">
      <img src="/about24.png" alt="New Image 2" style="width: 180px; height: 95px;position: relative; left: 20px; top: 100px;">
      <img src="/about25.png" alt="New Image 3" style="width: 180px; height: 95px;position: relative; left: 20px; top: -103px;">
    </div>
  </div>
  <div class="text-group new-text-group-4">
    <h2>加强国际合作</h2>
    <p>Strengthen International Cooperation</p>
    <p>科技创新可以为小体型野生动物的保护提供新的手段和方法。利用先进的监测技术，实时掌握小体型野生动物的分布和数量变化。开发新型的保护设备和工具，提高保护效率。同时，运用大数据和人工智能技术，分析小体型野生动物的生存环境和行为模式，为制定科学的保护策略提供依据。此外，鼓励科研机构和企业加大在小体型野生动物保护方面的研发投入，推动科技创新与保护实践的结合。</p>
    <ul class="keyword-list new-keyword-list-4">
      <li><span class="green-dot">&#8226;</span>信息共享</li>
      <li><span class="green-dot">&#8226;</span>技术支持</li>
      <li><span class="green-dot">&#8226;</span>联合执法</li>
    </ul>
  </div>
</div>
    
    
      </section>
    </div>  
  </div>
</template>  



  
<script>
export default {
  name: 'AboutPage',
  data() {
    return {
      activeSection: 'protection',
      images: ['./about7.jpg', './about8.jpg', './about9.jpg', './about10.jpg'],
      currentImage: '',
      currentIndex: 0,
      intervalId: null
    };
  },
  created() {
    this.currentImage = this.images[this.currentIndex];
  },
  beforeDestroy() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    setActiveSection(section) {
    this.activeSection = section;
    window.scrollTo({ top: 0, behavior: 'smooth' });
    if (section === 'protection' &&!this.intervalId) {
        this.startCarousel();
    }
},
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.currentImage = this.images[this.currentIndex];
      console.log('切换到下一张图片：', this.currentImage);
    },
    startCarousel() {
      this.intervalId = setInterval(this.nextImage, 3000);
      console.log('启动轮播图定时器');
    },
    handleScroll() {
      const topNavHeight = 50;
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      const contentElement = document.getElementById('contentBox');
      if (scrollTop > topNavHeight) {
        contentElement.style.marginTop = `${topNavHeight}px`;
      } else {
        contentElement.style.marginTop = '0';
      }
      const footerTop = document.querySelector('footer').getBoundingClientRect().top;
      const sidebarNav = document.querySelector('.sidebar-nav');
      if (sidebarNav.getBoundingClientRect().bottom > footerTop) {
        sidebarNav.classList.add('limit-to-footer');
      } else {
        sidebarNav.classList.remove('limit-to-footer');
      }
    }
  },
  mounted() {
    console.log('添加滚动事件监听器');
    window.addEventListener('scroll', this.handleScroll);
  }
};
</script>
  




<style scoped>  

.about {  
  padding: 20px;  
  display: flex;  
  
} 
  
.sidebar-nav {  
  width: 150px;  
  background-color: #34463a; 
  padding: 10px;  
  color: white; 
  min-width: 150px;
  position: fixed; 
  top: 135px; 
  left: 20px;
  height:570px;
  transition: top 0.3s ease;
  
}  

.sidebar-nav.limit-to-footer {
  top: calc(100vh - 570px);
}

.sidebar-nav ul {  
  list-style-type: none;  
  padding: 0;  
}  
  
.sidebar-nav li {  
  margin-bottom: 10px; 
}  


  
.nav-link {  
  display: block;  
  text-decoration: none;  
  color: white; 
  padding: 5px; 
  font-size: 15px; 
  letter-spacing: 1.5px; 
  line-height: 1.5; 
}  
  
.nav-link.router-link-exact-active,  
.nav-link:hover {  
  background-color: rgb(120, 164, 120); 
  color: rgb(249, 248, 248); 
}  


  
.content {  
  flex-grow: 1;  
  padding-left: 200px;  
 
}  


  
.section:target {  
  border-left: 5px solid green;  
  padding-left: 15px; 
}  



 /* 1 */
.indented-text {  
  text-indent: 2em; 
  text-align: justify; 
  letter-spacing: 0.3em; 
  line-height: 1.8; 
  padding: 40px; 
  padding-top: 25px;
  padding-bottom: 40px;  
  padding-left: 110px; 
  padding-right: 110px;
  font-size: 15px;
 
}

  h1 {  
    display: block;  
    font-size: 2em; 
    margin-block-start: 0.67em;  
    margin-block-end: 0.67em;  
    margin-inline-start: 0;  
    margin-inline-end: 0;  
    font-weight: bold;  
    unicode-bidi: isolate;  
  }  


    
  .section ul li {  
    display: flex;  
    align-items: center;  
    padding-bottom: 40px;  
}  
  

  
.section ul li img {  
    height: auto;  
    padding-left: 90px; 
    padding-right: 80px;
    flex-shrink: 0;  
}  
  

  
.section ul li p {  
    text-align: justify;  
    letter-spacing: 0.2em;  
    line-height: 2.5;  
    font-size: 13px;  
    padding-left: 10px; 
    padding-right: 0; 
}  

.reversed-layout li {  
  flex-direction: row-reverse;  
  justify-content: flex-end; 
  
  padding-bottom: 40px; 
   
} 

.reversed-layout li img {  
  margin-left: auto;
}  

.reversed-layout li p {  
  margin-left: 85px;  
}  
  
 
.highlighted-text {  
  font-size: 25px;  
  display: inline-block; 
  position: relative; 
  padding-left: 20px; 
  z-index: -1;
}  
  
.highlighted-text::before {  
  content: ""; 
  display: block; 
  width: 0;  
  height: 0;  
  border-top: 10px solid transparent; 
  border-bottom: 10px solid transparent; 
  border-left: 10px solid green; 
    
  
  position: absolute;  
  left: 0; 
  top: 50%; 
  transform: translateY(-50%); 
  z-index: -1;
}


  .h3-custom {  
  display: inline-block;  
  border: 2px solid green;  
  background-color: transparent;  
  padding: 5px 10px;  
  color: rgb(40, 39, 39);  
  font-weight: bold;  
  letter-spacing: 0.1em;  
  margin: 0; 
  margin-top: 40px; 
  margin-bottom: 20px; 
  
  }  
  


   /* 2 */
   #importance h2 {
    letter-spacing: 3px;
    line-height: 1.8;
    font-size: 20px;
    color: #3a453c;
    margin-bottom: -50px; 
    margin-top: 30px; 
  }

  
.image {
  position: relative;
  width: 40%;
    width: auto;
}


.image__overlay {
  position: absolute;
  top: 6px;
  left: 6px;
  width: 261px;
  height: 180px;
  background: rgba(72, 71, 71, 0.3);
  color: #ffffff;
  font-family: 'Quicksand', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: opacity 0.25s;
  opacity: 0;
  
}

.image__overlay:hover {
  opacity: 1;
}

.image__overlay--blur {
  backdrop-filter: blur(5px);
}

.image__overlay--solid {
  background: #fefdfd;
}

.image__overlay div {
  margin-top: -25px;
}

#box {
  width: 1000px;
  height: 400px;
  margin: 5px auto; 
  display: flex; 
  justify-content: space-around;
  align-items: center;
  gap: 0.5px; 
 
}

#box1, #box2, #box3 {
  position: relative; 
}

#box img {
  margin: 7px;
  width: 260px;
  height: 160px;
}


.image__description-box {
  position: absolute;
  bottom: -130px; 
  width: 260px;
  height: 180px;
  background-color: white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  padding: 20px;
  left: 7px;
  box-sizing: border-box; 


  text-align: justify; 
  font-size: 10px; 
  letter-spacing: 2px; 
  line-height: 1.8; 
}

.image__description-box h3 {
  font-size: 13px; 
  color: #333; 
  margin-bottom: 30px; 
}



.box {
  width: 1000px;
  height: 400px;
  margin: 5px auto; 
  display: flex; 
  justify-content: space-around;
  align-items: center;
  gap: 0.5px; 
  margin-bottom: 120px;
}

.box1,
.box2,
.box3 {
  position: relative; 
}

.box img {
  margin: 7px;
  width: 260px;
  height: 160px;
}






   /* 3 */
   #protection {
    position: relative;
    overflow: hidden; 
  }
  

.carousel-container {  
  position: relative;  
  width: 100%;  
  height: 300px; 
  overflow: hidden;  
  
}  
.carousel-slide {  
  width: 100%;  
  height: 100%;  
  background-size: cover;  
  background-position: center;  
  position: relative;  
  
}  
.carousel-text {
  position: absolute;
  top: 0;
  left: 5px;
  padding: 60px;
  color: white;
  text-align: left;
}

.carousel-text h2 {
  font-size: 28px;
  margin: 0;
}

.carousel-text p {
  font-size: 12px;
  margin: 10px 0 0 0;
  line-height: 1.8; 
  letter-spacing: 1px; 
}


.carousel-indicators {  
  position: absolute;  
  top: 280px; 
  left: 50%;  
  transform: translateX(-50%); 
  display: flex;  
  gap: 10px;  
  list-style-type: none;  
  padding: 0;  
  margin: 0;  
}  
  
.carousel-indicator {  
  width: 10px;  
  height: 10px;  
  background-color: gray;  
  border-radius: 50%;  
  cursor: pointer;  
  
}

.carousel-indicator.active {
  background-color: white;
}




.section-group {
  display: flex;

}


.image-group {
  display: flex;
}
.right-images {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}


.text-group {
  flex: 1;
  padding-left: 60px;
  text-align: left; 
  position: relative;
  margin-right: 15px;
  top: 20px;
}

.text-group h2 {
  position: relative;
  top: 20px; 
}

.text-group p {
  text-align: left; 
  line-height: 1.8; 
  letter-spacing: 1px; 
  font-size: 10px;
  color: rgb(137, 138, 137);
  
}

.green-dot {
  color: green;
  font-size: 25px; 
  margin-right: 10px; 
  display: inline-block;
  vertical-align: middle;
}


.text-group ul.keyword-list li {
  text-align: left;
  line-height: normal;
  font-size: 12px;
  display: inline-block;
  letter-spacing: 2px;
}

.text-group ul li::after {
  content: "\00A0\00A0\00A0\00A0\00A0"; 
}

.new-text-group, new-text-group-3, new-text-group-4, new-text-group-5{
  margin-top: 40px; 
}
</style>