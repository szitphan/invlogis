/* Invlogis landing — JS tối thiểu: menu mobile, demo "AI đọc chứng từ", form giả (front-end). */
(function () {
  'use strict';
  var d = document;

  // Menu mobile
  var burger = d.querySelector('.burger'), nav = d.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var o = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Demo: chứng từ -> hồ sơ. Mặc định (không JS / giảm chuyển động) hiện sẵn trạng thái cuối.
  var demo = d.getElementById('demo');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (demo && !reduce) {
    var fields = [].slice.call(demo.querySelectorAll('.f'));
    var rows = [].slice.call(demo.querySelectorAll('.r'));
    var scan = demo.querySelector('.scan'), doc = demo.querySelector('.doc');
    var count = demo.querySelector('[data-count]'), save = demo.querySelector('.save');
    var T = { read: demo.dataset.read, ready: demo.dataset.ready, saved: demo.dataset.saved, save: demo.dataset.save, wait: demo.dataset.wait };
    var timers = [], running = false, loops = 0, paused = false, MAX = 3;
    var pp = demo.querySelector('.pp'); pp.hidden = false;
    var later = function (fn, ms) { timers.push(setTimeout(fn, ms)); };
    var reset = function () {
      timers.forEach(clearTimeout); timers = [];
      fields.forEach(function (f) { f.classList.remove('hl'); });
      rows.forEach(function (r) { r.classList.remove('in'); });
      scan.classList.remove('on'); scan.style.transform = '';
      count.textContent = T.wait; save.textContent = T.save; save.classList.remove('done');
    };
    var finish = function (ended) {
      timers.forEach(clearTimeout); timers = [];
      fields.forEach(function (f) { f.classList.remove('hl'); });
      rows.forEach(function (r) { r.classList.add('in'); });
      scan.classList.remove('on'); count.textContent = T.ready; save.textContent = T.saved; save.classList.add('done');
      paused = true; pp.textContent = ended ? demo.dataset.replay : demo.dataset.play; pp.setAttribute('aria-pressed', 'true');
    };
    var play = function () {
      reset(); demo.classList.add('js');
      var t = 500;
      fields.forEach(function (f, i) {
        later(function () {
          var top = f.offsetTop - 6;
          scan.classList.add('on'); scan.style.transform = 'translateY(' + top + 'px)';
          fields.forEach(function (x) { x.classList.remove('hl'); }); f.classList.add('hl');
        }, t);
        later(function () { rows[i].classList.add('in'); count.textContent = T.read.replace('{n}', i + 1).replace('{m}', fields.length); }, t + 650);
        t += 1050;
      });
      later(function () { fields.forEach(function (x) { x.classList.remove('hl'); }); scan.classList.remove('on'); count.textContent = T.ready; }, t + 200);
      later(function () { save.textContent = T.saved; save.classList.add('done'); }, t + 1600);
      later(function () { loops++; if (loops >= MAX) { finish(true); } else { play(); } }, t + 5200);
    };
    pp.addEventListener('click', function () {
      if (paused) { paused = false; loops = 0; pp.textContent = demo.dataset.pause; pp.setAttribute('aria-pressed', 'false'); play(); }
      else { finish(false); }
    });
    var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (en) {
      en.forEach(function (e) {
        if (e.isIntersecting && !running) { running = true; if (!paused && loops < MAX) play(); }
        else if (!e.isIntersecting && running) { running = false; if (!paused) { reset(); demo.classList.remove('js'); } }
      });
    }, { threshold: 0.35 }) : null;
    if (io) io.observe(demo); else { running = true; play(); }
  }

  // Form: chỉ front-end
  var form = d.getElementById('lead-form'), thanks = d.getElementById('thanks');
  if (form && thanks) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      form.style.display = 'none'; thanks.classList.add('show'); thanks.focus();
    });
  }
})();
