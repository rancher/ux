(function(){
  var sel=document.getElementById('theme');
  var saved=localStorage.getItem('rds-theme')||'light';
  document.documentElement.setAttribute('data-theme',saved);
  if(sel){sel.value=saved;sel.addEventListener('change',function(){
    document.documentElement.setAttribute('data-theme',sel.value);
    localStorage.setItem('rds-theme',sel.value);
  });}
})();
