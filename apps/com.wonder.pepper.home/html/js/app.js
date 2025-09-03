(function(){
  function byId(id){ return document.getElementById(id); }
  function byClass(cls){ return document.getElementsByClassName(cls); }

  /* ——— 时钟 ——— */
  function pad(n){ return (n<10?'0':'') + n; }
  function tick(){
    var d = new Date();
    byId('clock').innerHTML = pad(d.getHours()) + ':' + pad(d.getMinutes());
  }

  /* ——— 多页管理 ——— */
  var cur = 0, pages, dotsBox;

  function renderDots(n){
    var i, html='';
    for(i=0;i<n;i++){ html += '<span class="dot'+(i===cur?' active':'')+'"></span>'; }
    dotsBox.innerHTML = html;
    // 让点可点击
    var ds = dotsBox.getElementsByClassName('dot');
    for(i=0;i<ds.length;i++){
      (function(idx){
        ds[idx].onclick = function(){ go(idx); return false; };
      })(i);
    }
  }

  function go(n){
    if(n<0) n = pages.length-1;
    if(n>=pages.length) n = 0;
    pages[cur].className = 'page';
    cur = n;
    pages[cur].className = 'page current';
    renderDots(pages.length);
  }

  function bindPager(){
    byId('prev').onclick = function(e){ if(e&&e.preventDefault)e.preventDefault(); go(cur-1); return false; };
    byId('next').onclick = function(e){ if(e&&e.preventDefault)e.preventDefault(); go(cur+1); return false; };
  }

  /* ——— 轻量滑动切页（左右滑） ——— */
  function bindSwipe(el){
    var sx=0, dx=0, touching=false;
    el.addEventListener('touchstart', function(ev){
      if(!ev.touches || !ev.touches.length) return;
      touching = true; sx = ev.touches[0].clientX; dx = 0;
    }, false);
    el.addEventListener('touchmove', function(ev){
      if(!touching) return;
      dx = ev.touches[0].clientX - sx;
    }, false);
    el.addEventListener('touchend', function(){
      if(!touching) return;
      touching = false;
      if(Math.abs(dx) > 60){ go(cur + (dx<0?1:-1)); }
    }, false);
  }

  /* ——— 点击 App：若可用则通过 ALMemory 上报 ——— */
  var session = null, mem = null;

  function connectPepper(){
    // Pepper 平板到本体固定走 198.18.0.1:80
    function ready(){ if(window.QiSession){ try{
        session = new QiSession('ws://198.18.0.1:80');
        session.service('ALMemory').then(function(m){ mem = m; });
      }catch(e){} } }
    if(window.QiSession){ ready(); return; }
    var s = document.createElement('script');
    s.src = 'http://198.18.0.1/libs/qimessaging/2/qimessaging.js';
    s.onload = ready;
    document.getElementsByTagName('head')[0].appendChild(s);
  }

  function bindApps(){
    var links = document.getElementsByTagName('a');
    var i, app;
    for(i=0;i<links.length;i++){
      app = links[i].getAttribute('data-app');
      if(!app) continue;
      links[i].onclick = (function(a){
        return function(e){
          if(e&&e.preventDefault) e.preventDefault();
          // 有 Pepper 桥就发事件，否则弹提示
          if(mem){
            mem.raiseEvent('tablet/app/open', a);
          }else{
            alert('Open: '+a);
          }
          return false;
        };
      })(app);
    }
  }

  /* ——— 启动 ——— */
  window.onload = function(){
    tick(); setInterval(tick, 30000);

    pages = byId('pages').getElementsByClassName('page');
    dotsBox = byId('dots');
    renderDots(pages.length);
    bindPager();
    bindSwipe(byId('pages'));
    bindApps();
    connectPepper();
  };
})();
