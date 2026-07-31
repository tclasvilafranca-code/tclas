(function () {
  "use strict";

  var data = window.__BRAND__ || {};
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  var $ = function (sel, scope) { return (scope || document).querySelector(sel); };
  var $$ = function (sel, scope) { return Array.prototype.slice.call((scope || document).querySelectorAll(sel)); };
  var escHTML = function (s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  };
  function safe(fn, name) {
    try { fn(); } catch (e) { console.warn("[" + name + "]", e); }
  }

  /* ---------- Mounts (idempotent) ---------- */

  function mountBadges() {
    var target = $("[data-badges]");
    if (!target || target.children.length > 0 || !data.founder || !data.founder.badges) return;
    target.innerHTML = data.founder.badges.map(function (b) {
      return "<li>" + escHTML(b) + "</li>";
    }).join("");
  }

  function mountTimeline() {
    var target = $("[data-timeline]");
    if (!target || target.children.length > 0 || !data.timeline) return;
    target.innerHTML = data.timeline.map(function (item) {
      return (
        '<li class="timeline-item">' +
          '<p class="timeline-year">' + escHTML(item.year) + "</p>" +
          "<div>" +
            '<h3 class="timeline-title">' + escHTML(item.title) + "</h3>" +
            '<p class="timeline-text">' + escHTML(item.text) + "</p>" +
          "</div>" +
        "</li>"
      );
    }).join("");
  }

  /* ---------- Splash ---------- */

  function initSplash() {
    var splash = $("[data-splash]");
    if (!splash) return;
    var hide = function () { splash.classList.add("is-out"); };
    if (document.readyState === "complete") setTimeout(hide, 500);
    else window.addEventListener("load", function () { setTimeout(hide, 400); });
    setTimeout(hide, 2200);
  }

  /* ---------- Nav ---------- */

  function initNav() {
    var nav = $("[data-nav]");
    if (!nav) return;
    var solid = false;
    window.addEventListener("scroll", function () {
      var shouldBeSolid = window.scrollY > 40;
      if (shouldBeSolid !== solid) {
        solid = shouldBeSolid;
        nav.style.background = solid
          ? "rgba(10,10,13,.92)"
          : "linear-gradient(180deg, rgba(10,10,13,.85) 0%, rgba(10,10,13,0) 100%)";
      }
    }, { passive: true });
  }

  /* ---------- Smooth anchor scroll (native) ---------- */

  function setupSmoothScroll() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (!a) return;
      var id = a.getAttribute("href");
      if (!id || id === "#") return;
      var el = document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      var navOffset = 76;
      window.scrollTo({
        top: el.getBoundingClientRect().top + window.scrollY - navOffset,
        behavior: reduced ? "auto" : "smooth"
      });
    });
  }

  /* ---------- Split text (preserves <br> and <em>) ---------- */

  function splitWords(el) {
    el.setAttribute("aria-label", el.textContent.trim().replace(/\s+/g, " "));
    var wrap = function (text) {
      return text.split(/(\s+)/).map(function (w) {
        return /^\s+$/.test(w) || w === "" ? w : '<span class="split-word">' + escHTML(w) + "</span>";
      }).join("");
    };
    var html = Array.prototype.map.call(el.childNodes, function (node) {
      if (node.nodeType === 3) return wrap(node.textContent);
      if (node.nodeName === "BR") return "<br>";
      if (node.nodeType === 1) {
        var tag = node.tagName.toLowerCase();
        return "<" + tag + ">" + wrap(node.textContent) + "</" + tag + ">";
      }
      return "";
    }).join("");
    el.innerHTML = html;
    return el.querySelectorAll(".split-word");
  }

  function initSplitText() {
    $$("[data-split]").forEach(function (el) {
      var words = splitWords(el);
      var delay = 0;
      words.forEach(function (w) {
        w.style.transitionDelay = delay + "ms";
        delay += 35;
      });
    });
  }

  /* ---------- Reveal on scroll ---------- */

  function initReveals() {
    var targets = $$(".reveal, [data-split], .timeline-item");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        entry.target.classList.add("is-split-visible");
        io.unobserve(entry.target);
      });
    }, { threshold: 0.01, rootMargin: "0px 0px -2% 0px" });

    targets.forEach(function (t) { io.observe(t); });

    setTimeout(function () {
      $$(".reveal:not(.is-visible), [data-split]:not(.is-split-visible), .timeline-item:not(.is-visible)").forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight) {
          el.classList.add("is-visible");
          el.classList.add("is-split-visible");
        }
      });
    }, 6000);
  }

  /* ---------- Count-up stats ---------- */

  function initCountUp() {
    var nodes = $$("[data-count-to]");
    if (!nodes.length) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        var el = entry.target;
        var target = parseInt(el.getAttribute("data-count-to"), 10) || 0;
        if (reduced) { el.textContent = target; return; }
        var start = null;
        var duration = 1400;
        function step(ts) {
          if (!start) start = ts;
          var progress = Math.min((ts - start) / duration, 1);
          var eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.round(eased * target);
          if (progress < 1) requestAnimationFrame(step);
          else el.textContent = target;
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.05 });
    nodes.forEach(function (n) { io.observe(n); });
    // Note: HTML already shows the final value by default (no-JS fallback),
    // so no extra safety timeout is needed here — the animation just restarts
    // the count from 0 once the element scrolls into view.
  }

  /* ---------- Pinned horizontal showcase ---------- */

  function initShowcase() {
    var showcase = $("[data-showcase]");
    var track = $("[data-showcase-track]");
    if (!showcase || !track || !window.gsap || !window.ScrollTrigger) return;
    if (matchMedia("(max-width: 719px)").matches) return; // let mobile scroll natively

    var distance = function () { return track.scrollWidth - showcase.clientWidth; };

    gsap.to(track, {
      x: function () { return -distance(); },
      ease: "none",
      scrollTrigger: {
        trigger: showcase,
        start: "top top",
        end: function () { return "+=" + (distance() + window.innerHeight); },
        pin: true,
        scrub: 0.6,
        invalidateOnRefresh: true
      }
    });
  }

  /* ---------- Footer year ---------- */

  function setFooterYear() {
    var el = $("[data-year]");
    if (!el) return;
    el.textContent = String(new Date().getFullYear());
  }

  /* ---------- Boot ---------- */

  function boot() {
    safe(mountBadges, "mountBadges");
    safe(mountTimeline, "mountTimeline");

    safe(initSplash, "initSplash");
    safe(initNav, "initNav");
    safe(setupSmoothScroll, "setupSmoothScroll");
    safe(initSplitText, "initSplitText");
    safe(initReveals, "initReveals");
    safe(initCountUp, "initCountUp");
    safe(setFooterYear, "setFooterYear");

    if (window.gsap && window.ScrollTrigger) {
      try { gsap.registerPlugin(ScrollTrigger); } catch (_) {}
      safe(initShowcase, "initShowcase");
    }

    document.documentElement.classList.add("is-ready");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
