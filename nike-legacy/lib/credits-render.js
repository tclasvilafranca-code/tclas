(function () {
  "use strict";

  function escHTML(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function render(credits) {
    var list = document.querySelector("[data-credits]");
    if (!list) return;
    list.innerHTML = Object.keys(credits).map(function (id) {
      var c = credits[id];
      return (
        "<li>" +
          '<strong>' + escHTML(c.title) + "</strong> — " +
          (c.creator_url
            ? '<a href="' + escHTML(c.creator_url) + '" target="_blank" rel="noopener">' + escHTML(c.creator) + "</a>"
            : escHTML(c.creator)) +
          " (" + escHTML(c.source) + ") · " +
          '<a href="' + escHTML(c.license_url) + '" target="_blank" rel="noopener">' +
            escHTML(c.license.toUpperCase()) + " " + escHTML(c.license_version || "") +
          "</a> · " +
          '<a href="' + escHTML(c.foreign_landing_url) + '" target="_blank" rel="noopener">Ver original ↗</a>' +
        "</li>"
      );
    }).join("");
  }

  fetch("assets/credits.json")
    .then(function (r) { return r.json(); })
    .then(render)
    .catch(function (e) { console.warn("[credits]", e); });
})();
