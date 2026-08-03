(function () {
  "use strict";

  var data = window.__BRAND__ || {};
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = matchMedia("(hover: hover) and (pointer: fine)").matches;

  var $ = function (sel, scope) { return (scope || document).querySelector(sel); };
  var $$ = function (sel, scope) { return Array.prototype.slice.call((scope || document).querySelectorAll(sel)); };
  var clamp = function (v, min, max) { return Math.max(min, Math.min(max, v)); };
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

  /* ---------- Nav background on scroll ---------- */

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
      var target;
      // #iconos is a pinned ScrollTrigger section: its layout position and
      // the scroll distance needed to reach it are two different things
      // once pinning is active, so ask the trigger directly instead of
      // measuring getBoundingClientRect (which only reflects pre-pin layout).
      if (id === "#iconos" && window.__showcaseST) {
        target = window.__showcaseST.start;
      } else {
        target = el.getBoundingClientRect().top + window.scrollY - navOffset;
      }
      var max = document.documentElement.scrollHeight - window.innerHeight;
      target = clamp(target, 0, Math.max(max, 0));
      window.scrollTo({ top: target, behavior: reduced ? "auto" : "smooth" });
    });
  }

  /* ---------- Split text (preserves <br> and <em>) ---------- */

  function splitInline(el, mode) {
    el.setAttribute("aria-label", el.textContent.trim().replace(/\s+/g, " "));
    var cls = mode === "chars" ? "split-char" : "split-word";

    var wrapWords = function (text) {
      return text.split(/(\s+)/).map(function (w) {
        return /^\s+$/.test(w) || w === "" ? w : '<span class="' + cls + '">' + escHTML(w) + "</span>";
      }).join("");
    };
    var wrapChars = function (text) {
      return text.split("").map(function (ch) {
        return ch === " " ? " " : '<span class="' + cls + '">' + escHTML(ch) + "</span>";
      }).join("");
    };
    var wrap = mode === "chars" ? wrapChars : wrapWords;

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
    return el.querySelectorAll("." + cls);
  }

  function initSplitText() {
    $$("[data-split]").forEach(function (el) {
      var mode = el.getAttribute("data-split");
      var units = splitInline(el, mode);
      var delay = 0;
      var step = mode === "chars" ? 18 : 35;
      units.forEach(function (w) {
        w.style.transitionDelay = delay + "ms";
        delay += step;
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

  /* ---------- Footer year ---------- */

  function setFooterYear() {
    var el = $("[data-year]");
    if (!el) return;
    el.textContent = String(new Date().getFullYear());
  }

  /* ================================================================
     Premium interaction layer — cursor, magnetism, tilt, progress,
     section spy, hero parallax, showcase controls.
     All gated to fine-pointer devices where relevant; none of this
     is required content, so a failure here never hides anything.
     ================================================================ */

  /* ---------- Custom cursor (dot + trailing swoosh) ---------- */

  function initCursor() {
    if (!fine) return;
    var cursor = $("[data-cursor]");
    var dot = $(".cursor-dot", cursor);
    var swoosh = $(".cursor-swoosh", cursor);
    if (!cursor || !dot || !swoosh) return;

    document.documentElement.classList.add("cursor-ready");

    var mx = 0, my = 0;      // raw target position
    var sx = 0, sy = 0;      // eased swoosh position
    var ready = false;

    window.addEventListener("mousemove", function (e) {
      mx = e.clientX; my = e.clientY;
      dot.style.transform = "translate3d(" + mx + "px," + my + "px,0)";
      if (!ready) {
        ready = true;
        sx = mx; sy = my;
        swoosh.style.transform = "translate3d(" + sx + "px," + sy + "px,0)";
        cursor.classList.add("is-ready");
      }
    });

    function loop() {
      sx += (mx - sx) * 0.18;
      sy += (my - sy) * 0.18;
      swoosh.style.transform = "translate3d(" + sx + "px," + sy + "px,0)";
      requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);

    var hoverSelector = 'a, button, .icon-card, [data-tilt], [data-magnetic]';
    document.addEventListener("mouseover", function (e) {
      if (e.target.closest && e.target.closest(hoverSelector)) cursor.classList.add("is-hovering");
    });
    document.addEventListener("mouseout", function (e) {
      var stillInside = e.target.closest && e.target.closest(hoverSelector);
      if (stillInside && (!e.relatedTarget || !stillInside.contains(e.relatedTarget))) {
        cursor.classList.remove("is-hovering");
      }
    });
  }

  /* ---------- Scroll progress bar ---------- */

  function initScrollProgress() {
    var bar = $("[data-scroll-progress]");
    if (!bar) return;
    var ticking = false;
    function update() {
      ticking = false;
      var max = document.documentElement.scrollHeight - window.innerHeight;
      var ratio = max > 0 ? clamp(window.scrollY / max, 0, 1) : 0;
      bar.style.transform = "scaleX(" + ratio + ")";
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  /* ---------- Section spy: nav links + dot nav ---------- */

  function initSectionSpy() {
    var sections = $$("main [id], .hero[id]");
    var navLinks = $$("[data-nav-link]");
    var dots = $$("[data-dot]");
    if (!sections.length) return;

    function setActive(id) {
      navLinks.forEach(function (a) {
        a.classList.toggle("is-active", a.getAttribute("data-nav-link") === id);
      });
      dots.forEach(function (a) {
        a.classList.toggle("is-active", a.getAttribute("data-dot") === id);
      });
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    }, { rootMargin: "-45% 0px -45% 0px", threshold: 0 });

    sections.forEach(function (s) { io.observe(s); });
    setActive("top");
  }

  /* ---------- Magnetic elements ---------- */

  function initMagnetic() {
    if (!fine) return;
    $$("[data-magnetic]").forEach(function (el) {
      var strength = parseFloat(el.getAttribute("data-magnetic-strength")) || 0.3;
      el.addEventListener("mousemove", function (e) {
        var rect = el.getBoundingClientRect();
        var x = (e.clientX - rect.left - rect.width / 2) * strength;
        var y = (e.clientY - rect.top - rect.height / 2) * strength;
        el.style.transform = "translate3d(" + x + "px," + y + "px,0)";
      });
      el.addEventListener("mouseout", function (e) {
        if (!el.contains(e.relatedTarget)) el.style.transform = "";
      });
    });
  }

  /* ---------- 3D tilt with cursor-tracked glow ---------- */

  function initTilt() {
    if (!fine) return;
    $$("[data-tilt]").forEach(function (el) {
      var strength = parseFloat(el.getAttribute("data-tilt-strength")) || 10;
      el.addEventListener("mousemove", function (e) {
        var rect = el.getBoundingClientRect();
        var px = (e.clientX - rect.left) / rect.width;
        var py = (e.clientY - rect.top) / rect.height;
        var rx = (0.5 - py) * strength;
        var ry = (px - 0.5) * strength;
        el.style.transform =
          "perspective(900px) rotateX(" + rx + "deg) rotateY(" + ry + "deg) translateY(-6px)";
        el.style.setProperty("--gx", (px * 100) + "%");
        el.style.setProperty("--gy", (py * 100) + "%");
        el.classList.add("is-glowing");
      });
      el.addEventListener("mouseout", function (e) {
        if (el.contains(e.relatedTarget)) return;
        el.style.transform = "";
        el.classList.remove("is-glowing");
      });
    });
  }

  /* ---------- Hero mouse parallax ---------- */

  function initHeroParallax() {
    if (!fine || reduced) return;
    var hero = $(".hero");
    var inner = $(".hero-inner");
    var streaks = $(".hero-streaks");
    if (!hero || !inner) return;
    hero.addEventListener("mousemove", function (e) {
      var rect = hero.getBoundingClientRect();
      var px = (e.clientX - rect.left) / rect.width - 0.5;
      var py = (e.clientY - rect.top) / rect.height - 0.5;
      inner.style.transform = "translate3d(" + (px * -14) + "px," + (py * -10) + "px,0)";
      if (streaks) streaks.style.transform = "translate3d(" + (px * 20) + "px," + (py * 14) + "px,0)";
    });
    hero.addEventListener("mouseleave", function () {
      inner.style.transform = "";
      if (streaks) streaks.style.transform = "";
    });
  }

  /* ---------- Icons showcase: pinned horizontal scroll + controls ---------- */

  function initShowcase() {
    var section = $("#iconos");
    var showcase = $("[data-showcase]");
    var track = $("[data-showcase-track]");
    var cards = $$("[data-icon-card]");
    var countEl = $("[data-showcase-count]");
    var totalEl = $("[data-showcase-total]");
    var fillEl = $("[data-showcase-fill]");
    var prevBtn = $("[data-showcase-prev]");
    var nextBtn = $("[data-showcase-next]");
    var hint = $("[data-showcase-hint]");
    var fade = $("[data-showcase-fade]");
    if (!section || !showcase || !track || !cards.length) return;

    var total = cards.length;
    if (totalEl) totalEl.textContent = total < 10 ? "0" + total : String(total);

    var currentIndex = 0;
    var dismissHint = function () { if (hint) hint.classList.add("is-done"); };

    function renderProgress(ratio, index) {
      ratio = clamp(ratio, 0, 1);
      if (fillEl) fillEl.style.width = (10 + ratio * 90) + "%";
      if (countEl) countEl.textContent = (index + 1) < 10 ? "0" + (index + 1) : String(index + 1);
      if (fade) fade.classList.toggle("is-hidden", ratio > 0.96);
      if (prevBtn) prevBtn.disabled = index <= 0;
      if (nextBtn) nextBtn.disabled = index >= total - 1;
      currentIndex = index;
    }

    var usePin = window.gsap && window.ScrollTrigger && !matchMedia("(max-width: 719px)").matches;

    if (usePin) {
      var distance = function () { return track.scrollWidth - showcase.clientWidth; };
      var st;
      var tween = gsap.to(track, {
        x: function () { return -distance(); },
        ease: "none",
        scrollTrigger: {
          trigger: section,
          start: "top top",
          end: function () { return "+=" + (distance() + window.innerHeight); },
          pin: true,
          scrub: 0.6,
          invalidateOnRefresh: true,
          onUpdate: function (self) {
            var d = distance();
            var ratio = d > 0 ? clamp((-gsap.getProperty(track, "x")) / d, 0, 1) : 0;
            var index = Math.round(ratio * (total - 1));
            renderProgress(ratio, index);
            if (self.progress > 0.02) dismissHint();
          }
        }
      });
      st = tween.scrollTrigger;
      window.__showcaseST = st;

      function goTo(index) {
        index = clamp(index, 0, total - 1);
        if (!st) return;
        var ratio = total > 1 ? index / (total - 1) : 0;
        var target = st.start + ratio * (st.end - st.start);
        window.scrollTo({ top: target, behavior: reduced ? "auto" : "smooth" });
        dismissHint();
      }

      if (prevBtn) prevBtn.addEventListener("click", function () { goTo(currentIndex - 1); });
      if (nextBtn) nextBtn.addEventListener("click", function () { goTo(currentIndex + 1); });
      renderProgress(0, 0);
    } else {
      // Mobile / no-GSAP fallback: native horizontal scroll drives the same UI.
      var cardStep = function () {
        var second = cards[1];
        return second ? (second.offsetLeft - cards[0].offsetLeft) : showcase.clientWidth;
      };
      function updateFromScroll() {
        var max = track.scrollWidth - showcase.clientWidth;
        var ratio = max > 0 ? clamp(showcase.scrollLeft / max, 0, 1) : 0;
        var index = Math.round(ratio * (total - 1));
        renderProgress(ratio, index);
        if (showcase.scrollLeft > 8) dismissHint();
      }
      showcase.addEventListener("scroll", function () {
        requestAnimationFrame(updateFromScroll);
      }, { passive: true });
      showcase.addEventListener("touchstart", dismissHint, { passive: true });

      function goTo(index) {
        index = clamp(index, 0, total - 1);
        showcase.scrollTo({ left: cardStep() * index, behavior: reduced ? "auto" : "smooth" });
        dismissHint();
      }
      if (prevBtn) prevBtn.addEventListener("click", function () { goTo(currentIndex - 1); });
      if (nextBtn) nextBtn.addEventListener("click", function () { goTo(currentIndex + 1); });
      renderProgress(0, 0);
    }
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

    safe(initCursor, "initCursor");
    safe(initScrollProgress, "initScrollProgress");
    safe(initSectionSpy, "initSectionSpy");
    safe(initMagnetic, "initMagnetic");
    safe(initTilt, "initTilt");
    safe(initHeroParallax, "initHeroParallax");

    if (window.gsap && window.ScrollTrigger) {
      try { gsap.registerPlugin(ScrollTrigger); } catch (_) {}
    }
    safe(initShowcase, "initShowcase");

    // Webfonts and late image/layout settling can change section heights
    // after ScrollTrigger's first measurement — resync once things settle
    // so pinned sections and anchor links stay in sync.
    if (window.ScrollTrigger) {
      var refresh = function () { try { ScrollTrigger.refresh(); } catch (_) {} };
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(refresh);
      window.addEventListener("load", function () { setTimeout(refresh, 300); });
    }

    document.documentElement.classList.add("is-ready");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
